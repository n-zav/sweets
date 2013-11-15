//http://code.google.com/p/jquery-ui-map/
$('#map_canvas').gmap('closeInfoWindow');
$(function() {
              $('#map_canvas').gmap().bind('init', function(event, map) {
                  $('#map_canvas').gmap('addMarker', { /*id:'m_1',*/ 'position': '48.018951,37.859035', 'bounds': true }).click(function() {
                  $('#map_canvas').gmap('openInfoWindow',
                    { 'content':  '<a href = "http://goo.gl/maps/3GgzU">Магазин "Умейка"</a> ' +
                        '<p>ул. Кадиеская 6, Донецк</p>', 'maxWidth': '300'}, this);
                  });
                  var zoom = $('#map_canvas').gmap('option', 'zoom', 17);
                });
              });
