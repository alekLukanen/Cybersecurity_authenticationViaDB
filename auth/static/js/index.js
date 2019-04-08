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



// var Session = __class__ ('Session', [Object], {
//     get __init__ () {return __get__ (this, function (self, token_url) {
//       self.token_url = token_url;});
//     }});