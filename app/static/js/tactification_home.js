$(document).ready(function(){console.log("here");$("#mainPost").css({"background-size":"100%"});});$(function(){console.log("postPic");$('#fbId').width(100);$('#fbId').height(25);});$(function(){console.log("postPic");$('#twId').width(100);$('#twId').height(25);});function updateStatusCallback(response){console.log('statusChangeCallback');console.log(response);if(response.status==='connected'){console.alert('Its connected');}else{console.alert('Its not authorized');}}
$(document).ready(function(){$.ajaxSetup({cache:true});$.getScript('//connect.facebook.net/en_US/sdk.js',function(){FB.init({appId:'613455148848789',version:'v2.7'});$('#loginbutton,#feedbutton').removeAttr('disabled');FB.getLoginStatus(updateStatusCallback);});});$(document).ready(function(){$("#myModal").on("shown.bs.modal",function(){$('#myModal').removeClass('in');})})
$("#myModal").on('hidden.bs.modal',function(e){$("#myModal iframe").attr("src",$("#myModal iframe").attr("src"));});function inspireVideo(vId){var iframe=document.getElementById("iframeYoutube");iframe.src="https://www.youtube.com/embed/"+vId+"?html5=1";$("#myModal").modal("show");}