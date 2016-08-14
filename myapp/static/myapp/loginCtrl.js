
 var mainApp=angular.module('mainApp', ['ngRoute']);

 mainApp.controller('loginCtrl', function($scope,$http) {
     $scope.onClickLogin=function () {
     	console.log("hello inside");
      if($scope.userName !="" && $scope.password != ""){
      	$http.post('/login/',{username : $scope.userName,password:$scope.password}).success(function(data,status){
      		Data = angular.fromJson(data)
      		if(Data.status == 0){
      			window.location.href="/dataEntry/";
      		}
      		else{
      			alert("invalid username and password");
      		}
      	})
      }
     }
console.log("hello");

 });