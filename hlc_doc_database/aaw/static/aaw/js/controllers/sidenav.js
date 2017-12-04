'use strict';

var app = angular.module('aaw')
app.controller('sideNavController', function ($location) {
    var _this = this;
    _this.navigate = navigate

    function navigate(url){
        $location.path(url);
    }
});
