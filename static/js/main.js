var stop_sound = new Audio('static/sound/stop.wav')
var start_sound = new Audio('static/sound/start.wav')
$(document).ready(function() {
// On refresh check if there are values selected
  if (localStorage.selectVal) {
    // Select the value stored
    $('select').val(localStorage.selectVal);
  }

  else {
    var prsntVal = $('#timer_value').val();
    localStorage.setItem('selectVal', prsntVal );
  }
});

// On change store the value
$('select').on('change', function(){
  var currentVal = $(this).val();
  localStorage.setItem('selectVal', currentVal );
});

function getOption() {
  start_sound.play();
  if (localStorage.selectVal) {
    var option_selected = localStorage.selectVal;
  }
  else {
    option_selected = $('#timer_value').val();
  }
  timeleft = option_selected;
}

                         

function timer_func()
{      
  var timer = setInterval(function(){
      if(timeleft <= 0){
        clearInterval(timer);
        document.getElementById("countdown").innerHTML = "TIME UP";
        stop_sound.play();
      } else {
        var t = timeleft;
        var minutes = Math.floor(t / 60);
        var seconds = t - minutes * 60;
        document.getElementById("countdown").innerHTML = minutes + "m :" + seconds + "s";
      }
      timeleft -= 1;
    }, 1000);
}
              
// function generate_timer(){

getOption();
timer_func();

