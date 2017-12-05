'use strict';

var app = angular.module('aaw')
app.controller('taxonomyController', function ($http) {
    var _this = this;
    _this.by_year = [];
    _this.by_dept = [];
    _this.by_hlc = [];

    _this.populate = populate;

    init()
    function init(){
        $http.get("/api/taxonomy/").then(res=>{
            _this.populate(res.data);
        })
    }
    function populate(data){
        var by_year_dict = data.by_year;
        var by_dept_dict = data.by_dept;
        var by_hlc_dict = data.by_hlc;

        var by_year = [];
        var by_dept = [];
        var by_hlc = [];

        for(var key in by_year_dict) {
            var value = by_year_dict[key];
            by_year.push({year: key, count: value});
        }
        for(var key in by_dept_dict) {
            var value = by_dept_dict[key];
            by_dept.push({year: key, count: value});
        }
        for(var key in by_hlc_dict) {
            var value = by_hlc_dict[key];
            by_hlc.push({year: key, count: value});
        }

        _this.by_year = by_year;
        _this.by_dept = by_dept;
        _this.by_hlc = by_hlc;
    }
});


function statsController ($http) {
    var _this = this;
    _this.by_year = [];
    _this.by_dept = [];
    _this.by_hlc = [];

    _this.populate = populate;

    init()
    function init(){
        $http.get("/api/taxonomy/").then(res=>{
            console.log(res.data)
            _this.populate(res.data);
        })
    }
    function populate(data){
        var by_year_dict = data.by_year;
        var by_dept_dict = data.by_dept;
        var by_hlc_dict = data.by_hlc;

        var by_year = [];
        var by_dept = [];
        var by_hlc = [];

        for(var key in by_year_dict) {
            var value = by_year_dict[key];
            by_year.push({year: key, count: value});
        }
        for(var key in by_dept_dict) {
            var value = by_dept_dict[key];
            by_dept.push({year: key, count: value});
        }
        for(var key in by_hlc_dict) {
            var value = by_hlc_dict[key];
            by_hlc.push({year: key, count: value});
        }

        _this.by_year = by_year;
        _this.by_dept = by_dept;
        _this.by_hlc = by_hlc;
    }
};
