
var app=angular.module("FileDetails",[]);

var departmentName="";
var year="";
var documentName="";
var newDocName="";

app.controller("uploadfile",function ($scope,$http) {
    $scope.saveUploadedDetails=function () {

        departmentName = document.getElementById('deptname').value;
        year=document.getElementById('docyear').value;
        documentName=document.getElementById('docname').value;
        newDocName=departmentName + "_" + documentName + "_" + year;
        console.log(newDocName);
    }
})







