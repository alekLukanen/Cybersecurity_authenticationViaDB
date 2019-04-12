
var data = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer '+getCookie('access_token'),
      'Host': 'localhost:8000'
    },
  };

  fetch('/api/users/myprofile/', data).then(function(res) {
    return res.json();
  }).then(function(resJson) {
    console.log('resJson: ', resJson);
    document.getElementById('name').innerHTML = resJson['firstName'] + " " + resJson['lastName'];
    document.getElementById('email').innerHTML = resJson['owner']['email'];
    return resJson;
  });



//https://www.w3schools.com/js/js_cookies.asp //////////////
function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
////////////////////////////////////////////////////////////

function doesCookieExist(cookieName){
  str = getCookie(cookieName);
  if (str.length>0){
      return true;
  }else{
      return false;
  }
}

