$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});

////////////////////////////////////////////////////////////

var client_id = 'V2jR2iLiDW3irsLwdAHzetFn5r93MIHmHBe6td6f';
var client_secret = 'XXoFJQsagJSvYbWqyjZAHEoFj6WAjJ4ykGrN27K752HQlF51yJdFJWqGguo1OnuoqKugcWqyRY22vTi7egPhrUuHd4cNLEmUydaj3Qp5slOlBbNpro4QuvrTLHbtmyfz';

function get_token(){
  username = document.getElementById('username').value;
  password = document.getElementById('password').value;

  console.log('username: ', username);
  console.log('password: ', password);

  body_data = {
    'username': username,
    'password': password,
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'password'
  };

  console.log('body_data: ', body_data);
  console.log('params: ', queryParams(body_data));

  var data = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic ' + btoa(client_id + ':' + client_secret),
      'Host': 'localhost:8000'
    },
    body: queryParams(body_data)
  };

  fetch('/api/users/o/token/', data).then(function(res) {
    return res.json();
  }).then(function(resJson) {
    console.log('resJson: ', resJson);
    setCookie('access_token', resJson['access_token'], 1);
    setCookie('refresh_token', resJson['refresh_token'], 1);
    url_array = window.location.href.split('/');
    hostname = url_array[0]+'//'+url_array[2]+'/content/profile.html'
    window.location.replace(hostname);
    return resJson;
  });

}

function queryParams(params) {
  return Object.keys(params)
      .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
      .join('&');
}

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
