var panel = $('#panel');
var sliders = [];

$(function() {
  var numControls = 4;
  // ---
  for (var i=0;i<numControls;i++) {
    // Stick an input in the body
    var slider = $('<input />');
    $('<div class="col-xs-4 col-sm-2 col-md-1 col-lg-1"/>')
      .appendTo(panel)
      .append( $('<div class="well channel"></div>')
                  .append('<h4>['+i+']</h4>')
                  .append(slider)
      );
    // Style it up
    slider.slider({
      min: 0,
      max: 255,
      step: 5,
      orientation: 'vertical',
      selection: 'after',
      value: 255,
      tooltip: 'show',
      formater: renderTooltip,
    });
    slider.data('channel',i);
    //slider.on('slide',onChangeState);
    sliders.push(slider);
  }
  //window.tick = window.setTimeout(onTick,100);
});

// function onTick() {
//   window.clearTimeout(window.tick);
//   $.get('/poll',null,function(data) {
//     for (var i=0;i<data.channels.length;i++) {
//       var renderVal = 255-data.channels[i];
//       sliders[i].slider('setValue',renderVal);
//     }
//     window.setTimeout(window.onTick,100);
//   });
// }
// 
// function onChangeState(e) {
//   var target = $(e.delegateTarget);
//   var channel = parseInt(target.data('channel'));
//   var value = 255 - e.value;
//   $.post('/post/',{channel:channel,value:value});
// };
function renderTooltip(x) {
  x = 255-x;
  x = Math.round((100*x)/255);
  return x+'%';
};

