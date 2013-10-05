//http://code.google.com/p/jquery-ui-map/
$(function() {
              $('#map_canvas').gmap().bind('init', function(event, map) {
                  $('#map_canvas').gmap('addMarker', { /*id:'m_1',*/ 'position': '48.0001730, 37.8571290', 'bounds': true });
                      var zoom = $('#map_canvas').gmap('option', 'zoom', 17);
        });
});
