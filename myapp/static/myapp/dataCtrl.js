 var mainApp=angular.module('mainApp', []);

 mainApp.controller('dataCtrl', function($scope,$http) {

     $scope.onClickSubmit=function () {
     	console.log("hello inside");
      if($scope.title !="" && $scope.description != "" && $scope.state != "" && $scope.district != ""){
      	$http.post('/api/data/',{
      	type: "subsidy",
      area: "both",
      title: $scope.title,
      description: $scope.description,
      date: "2012-04-23",
      state: $scope.state,
      district: $scope.district,
      for_whom: "all"}).success(function(data,status){
      		Data = angular.fromJson(data)
      		if(status == 201){
      			alert("done!");
      		}
      		else{
      			alert("invalid username and password");
      		}
      	})
      }
     }
console.log("hello");

 });

 