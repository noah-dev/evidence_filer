'use strict';

var app = angular.module('aaw')
app.controller('sideNavController', function ($location) {
    var _this = this;
    _this.navigate = navigate
    _this.selected = [true, false, false];

    function navigate(id,url){
        _this.selected = [false, false, false];
        _this.selected[id] = true;
        $location.path(url);
    }
});
