/**
 * Created by lalitnitrr on 14/8/16.
 */
 var mainApp=angular.module('mainApp', []);

 mainApp.controller('signUpCtrl', function($scope,$http) {

     $scope.onClickRegister=function () {
     	console.log("hello inside");
      if(($scope.userName !="" && $scope.password != "" && $scope.confpassword != "")&&( $scope.password == $scope.confpassword )){
      	$http.post('/api/signUp/',{username : $scope.userName,password:$scope.password}).success(function(data,status){
      		Data = angular.fromJson(data)
      		if(status == 201){
      			window.location.href="/";
      		}
      		else{
      			alert("error");
      		}
      	})
      }
     }
console.log("hello");

 });