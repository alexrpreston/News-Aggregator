
function pressMe(){
  var time = moment().tz('UTC').format('dddd, MMMM D YYYY, HH:mm:ss ZZ [UTC]');
  $('.time').document(10);
};


var updateTime = function () {
  var time = moment().tz('UTC').format('dddd, MMMM D YYYY, HH:mm:ss ZZ [UTC]');
  //document.getElementById("time").innerHTML = time;
  $('.time').html(10);
  setTimeout(updateTime, 500);
};

updateTime();

