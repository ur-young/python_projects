$(document).ready(function(){
    $("#get_header").load("/ #header")
    $("#get_footer").load("/ #footer")
});

function handleSubmit(event) {
    event.preventDefault()
    value = '' ;
  }

$(function(){
$('.tabcontent > div').hide();
$('.tabnav a').click(function () {
    $('.tabcontent > div').hide().filter(this.hash).fadeIn();
    $('.tabnav a').removeClass('active');
    $(this).addClass('active');
    return false;
}).filter(':eq(0)').click();
});