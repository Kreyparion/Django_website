$(window).scroll(function() {
    // Setting: Start fading halfway up the page
    var startPos = 0.3;
  
    // Cache window object
    var $w = $(window);
  
    // Basically, we go through each element and check its relative position within the viewport
    $("p, h1").each(function() {
  
      // Get current relative position in viewport, based on the top edge
      var pos = $(this).offset().top - $w.scrollTop();

  
      // Get viewport height
      var vh = $w.height();
  
      if (pos < vh * startPos) {
        // If element has past the starting threshold, we fade it
        $(this).css('opacity', ((pos-30) / (vh * startPos) * 1)**3);
      } else {
        $(this).css('opacity', 1);
      }
    });
  });