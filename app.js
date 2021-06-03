var clicked = true;

$(".dropDownMenu").click(function(){
  $(".navWrapper").toggleClass("toggle");
  clicked = !clicked;
});

$(window).resize(function(){
  if(window.innerWidth >= 600 && $(".navWrapper").hasClass("toggle")){
    $(".navWrapper").removeClass("toggle");
  }else if (window.innerWidth <= 600 && clicked) {
    $(".navWrapper").addClass("toggle");
  }
});
