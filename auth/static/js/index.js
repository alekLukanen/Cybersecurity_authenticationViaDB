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


function postRequest(username, password){
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




$.ajax({
  asynch: false,
  url: location.protocol + "//" + location.host + "/http://127.0.0.1:8000/api/users/myprofile/" + username,
  method: "GET",
  headers: { "Athurization": "postRequest()"},
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
  headers: { "Athurization": "Bearer ACCESS_TOKEN"},
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
  // console.log(parsed_data.success),

  error: function(x, y, z){ 
    alert(JSON.stringify(x) + JSON.stringify(y) + JSON.stringify(z));
  }  

});



