function adjustHeights() {
  if($('#main-hero').outerHeight() + $('#link-container').outerHeight() < $(window).height()) {
    $('#body').css('max-height', '100vh');
    $('#link-container').css('height', `${$(window).height() - $('#main-hero').outerHeight()}px`)
  } else {
    $('#body').css('max-height', `${$('#main-hero').outerHeight() + $('#link-container').outerHeight()}px`);
    $('#link-container').css('height', 'unset');
  }
}

adjustHeights();

$(window).bind('resize', function () {
  adjustHeights();
});
