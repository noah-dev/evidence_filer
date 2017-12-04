var aawApp = angular.module('aaw', ['ngMaterial', 'ngRoute', 'ngAnimate', 'ngMdIcons']);

aawApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
aawApp.config(function($routeProvider, $locationProvider, $mdThemingProvider) {
	$routeProvider
		.when('/aaw/', {
			templateUrl: 'static/aaw/views/upload.html',
			controller: 'uploadController',
			controllerAs: 'uc'
		})
		.when('/aaw/taxonomy', {
    		templateUrl: 'static/aaw/views/taxonomy.html',
			controller: 'taxonomyController',
			controllerAs: 'tc'
        })
        .when('/aaw/retrival', {
    		templateUrl: 'static/aaw/views/retrival.html',
			controller: 'retrivalController',
			controllerAs: 'rc'
		})
		
	$locationProvider.html5Mode(true)
	
    $mdThemingProvider.theme('default')
        .dark()
        .primaryPalette('blue')
		.accentPalette('green');
});