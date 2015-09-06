// See post: http://asmaloney.com/2014/01/code/creating-an-interactive-map-with-leaflet-and-openstreetmap/
/*
var map = L.map( 'map', {
    center: [20.0, 5.0],
    minZoom: 2,
    zoom: 2
});*/

/*L.tileLayer( 'http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright" title="OpenStreetMap" target="_blank">OpenStreetMap</a> contributors | Tiles Courtesy of <a href="http://www.mapquest.com/" title="MapQuest" target="_blank">MapQuest</a> <img src="http://developer.mapquest.com/content/osm/mq_logo.png" width="16" height="16">',
    subdomains: ['otile1','otile2','otile3','otile4']
}).addTo( map );
*/
L.mapbox.accessToken = 'pk.eyJ1Ijoic29ybWF6YWJhbCIsImEiOiJkZTk1MzE1MmI2Mjk0YTg4MjUwMWY5NDlmYjk3ODkzMSJ9.X8cHVGNC_Onq0IdRV8jWVw';
// Create a map in the div #map
var map =L.mapbox.map('map', 'sormazabal.ff680016');

     // var map = L.map('map').setView([51.505, -0.09], 13); 
     L.tileLayer('https://{s}.tiles.mapbox.com/v4/<sormazabal.ff680016>/{z}/{x}/{y}.png?access_token=<pk.eyJ1Ijoic29ybWF6YWJhbCIsImEiOiJkZTk1MzE1MmI2Mjk0YTg4MjUwMWY5NDlmYjk3ODkzMSJ9.X8cHVGNC_Onq0IdRV8jWVw>').addTo(map);

for ( var i=0; i < 500; ++i ) 
{
   L.marker( [datos[i].latitude, datos[i].longitude]).addTo( map );
}