$('DIV#toggle_header').click(function() {
  var cha = $('header');
  if (cha.hasClass('red')) {
      cha.removeClass('red').addClass('green');
  } else if (cha.hasClass('green')) {
      cha.removeClass('green').addClass('red');
  }
});
