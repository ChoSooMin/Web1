'use strict';
$(document).ready(function () {

  // Accordion
  var all_panels = $('.templatemo-accordion > li > ul').hide();
  
  // Product detail
  $('.product-links-wap a').click(function () {
    var this_src = $(this).children('img').attr('src');
    $('#product-detail').attr('src', this_src);
    return false;
  });
  // End roduct detail

});