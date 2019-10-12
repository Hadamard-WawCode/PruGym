var mymap = L.map('mapid')
var mylat;
var mylng;
var myMarkers = L.layerGroup();

var gym = L.icon({
    iconUrl: 'pic/gym.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var person = L.icon({
    iconUrl: 'pic/person.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var bike = L.icon({
    iconUrl: 'pic/bike.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var swim = L.icon({
    iconUrl: 'pic/swim.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var forest = L.icon({
    iconUrl: 'pic/forest.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

navigator.geolocation.getCurrentPosition(function(position) {

    mylat = position.coords.latitude;
    mylng = position.coords.longitude;

    mymap.setView([mylat, mylng], 16);

    L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=GGI0R7Kfcu3Y6cnYhFLB', {
        attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>',
        maxZoom: 20,    
        id: 'mapbox.streets',
    }).addTo(mymap);

    var marker = L.marker([mylat, mylng], {icon: person}).bindPopup("Tu jesteś").addTo(mymap);
});

function distance(lat2, lon2, unit) {
      var radlat1 = Math.PI * mylat/180
      var radlat2 = Math.PI * lat2/180
      var theta = mylng-lon2
      var radtheta = Math.PI * theta/180
      var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
      if (dist > 1) {
          dist = 1;
      }
      dist = Math.acos(dist)
      dist = dist * 180/Math.PI
      dist = dist * 60 * 1.1515
      if (unit=="K") { dist = dist * 1.609344 }
      if (unit=="N") { dist = dist * 0.8684 }
      return dist
  }

function addMarker(type, lat, lng, desc) {
    var dist = distance(lat, lng, "K");
    var marker = L.marker([lat, lng], {icon: type}).bindPopup(desc + "\nOdległość: " + dist + "km").addTo(myMarkers);
}

function myView() {
    mymap.panTo([mylat, mylng]);
    mymap.setZoom(16);  
}

