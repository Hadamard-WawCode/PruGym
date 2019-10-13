var mymap = L.map('mapid')
var mylat;
var mylng;
var myMarkers = L.layerGroup();

var gym = L.icon({
    iconUrl: 'static/pics/gym.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var person = L.icon({
    iconUrl: 'static/pics/person.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var bike = L.icon({
    iconUrl: 'static/pics/bike.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var swim = L.icon({
    iconUrl: 'static/pics/swim.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var forest = L.icon({
    iconUrl: 'static/pics/forest.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});

var pitch = L.icon({
    iconUrl: 'static/pics/pitch.svg',
    iconSize: [20, 40],
    iconAnchor: [10, 0],
    popupAnchor: [0, 0],
});



//Filtry
L.easyButton('fas fa-dumbbell', function(button, map){show('Siłownia')} ).addTo(mymap);
L.easyButton('fas fa-futbol', function(button, map){show('Boisko')} ).addTo(mymap);
L.easyButton('fas fa-swimmer', function(button, map){show('Basen')} ).addTo(mymap);
L.easyButton('fas fa-bicycle', function(button, map){show('Rowery')} ).addTo(mymap);
//L.easyButton('fas fa-tree', function(button, map){show('Park')} ).addTo(mymap);
L.easyButton('fas fa-redo', function(button, map){show(null)} ).addTo(mymap);
L.easyButton('fas fa-male', function(button, map){myView()} ).addTo(mymap);


//Wypisywanie obiektow
function show(filter){
        mymap.removeLayer(myMarkers);
        myMarkers = L.layerGroup();
        for(var i = 0; i < objects.length; i++) {
            var obj = objects[i];
            var type = obj[0];

            if(filter != null && type != filter){
                continue;
            } else{
                var name = obj[1];
                var lat = obj[4];
                var lng = obj[5];
                var desc = "aa";
                switch (type) {
                    case 'Siłownia':
                        addMarker(gym, lat, lng, desc)
                        break;
                    case 'Boisko':
                        addMarker(pitch, lat, lng, desc)
                        break;
                    case 'Rowery':
                        addMarker(bike, lat, lng, desc)
                        break;
                    case 'Basen':
                        addMarker(swim, lat, lng, desc)
                        break;
                    case 'Park':
                        addMarker(forest, lat, lng, desc)
                        break;
                    default:
                        addMarker(gym, lat, lng, desc)
                        break;
            }  
        }
             
    } 
    myMarkers.addTo(mymap);  
}




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
    show('Siłownia');
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
      var res = "";
      if (dist < 1) {
          res = (dist * 1000).toFixed(0) + "m";
      }
      else {
          res = dist.toFixed(2) + "km";
      }
      return res;
  }

function addMarker(type, lat, lng, desc) {
    var dist = distance(lat, lng, "K");
    var marker = L.marker([lat, lng], {icon: type}).bindPopup(desc + "\nOdległość: " + dist).addTo(myMarkers);
}

function myView() {
    mymap.panTo([mylat, mylng]);
    mymap.setZoom(16);  
}

