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

export function postRequest(username, password){
  var xhr = new XMLHttpRequest();

  xhr.open("POST", token_url, true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
  xhr.setRequestHeader('Accept', 'application/JSON');
  xhr.send(JSON.stringify({ username: password}));

  xhr.onreadystatechange = function(){
    if(this.readyState != 4) return;

    if (this.status == 200){
       var data = JSON.parse(this.responseText);  
       console.log(data);
    }
  }

}

////////////////////////////////////////////////////////////


$.ajax({
  asynch: false,
  url: location.protocol + "//" + location.host + "/http://127.0.0.1:8000/api/users/o/token/" + username,
  method: "GET",
  headers: { "Athurization": ""},
  success: function (data) {

    for (var i = 0; i < data.d.UserProfileProperties.results.length; i++){
      
      if (data.d.UserProfileProperties.results[i].key === "FirstName") { firstName = data.d.UserProfileProperties.results[i].Value;}
      if (data.d.UserProfileProperties.results[i].key === "LastName") { lastName = data.d.UserProfileProperties.results[i].Value;}
      if (data.d.UserProfileProperties.results[i].key === "Email") { email = data.d.UserProfileProperties.results[i].Value;}

    }
  },

  dataType: 'JSON',
  data: JSON.stringify(application.JSON),

  error: function(x, y, z){ 
    alert(JSON.stringify(x) + JSON.stringify(y) + JSON.stringify(z));
  }  

});

$.ajax({
  asynch: false,
  url: location.protocol + "//" + location.host + "/http://127.0.0.1:8000/api/users/myprofile/" + username,
  method: "POST",
  headers: { "Athurization": "postRequest()"}, 
  success: function (data) {

    for (var i = 0; i < data.d.UserProfileProperties.results.length; i++){
      
      if (data.d.UserProfileProperties.results[i].key === "FirstName") { firstName = data.d.UserProfileProperties.results[i].Value;}
      if (data.d.UserProfileProperties.results[i].key === "LastName") { lastName = data.d.UserProfileProperties.results[i].Value;}
      if (data.d.UserProfileProperties.results[i].key === "Email") { email = data.d.UserProfileProperties.results[i].Value;}

    }
  },
  dataType: 'JSON',
  data: {json:JSON.stringify(application.JSON)},
  parsed_data: JSON.parse(data),

  cookie: setCookie("access_data", data["access_token"],1),
  cookie: setCookie("refresh_data", data["refresh_token"],1),

  error: function(x, y, z){ 
    alert(JSON.stringify(x) + JSON.stringify(y) + JSON.stringify(z));
  }  

});
 
////////////////////////////////////////////////////////////

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


function doesCookieExist(cookieName){
  str = getCookie(cookieName);
  if (str.length>0){
      return true;
  }else{
      return false;
  }
}

/////////////////////////////////////////////////////////////

function ifAdmin(admin_status){

    if(admin_status == true){
      print

    };

}