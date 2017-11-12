app = angular.module('indexApp',['ngMaterial'])
.config(($mdThemingProvider) => {
    $mdThemingProvider.theme('default')
        .dark()
        .primaryPalette('blue')
        .accentPalette('amber');
})
.controller('indexController', indexController);


function indexController ($http) {

};
