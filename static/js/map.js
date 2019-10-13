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
            var type = obj[1];

            if(filter != null && type != filter){
                continue;
            } else{
                var id = obj[0];
                var lat = obj[2];
                var lng = obj[3];
                switch (type) {
                    case 'Siłownia':
                        addMarker(gym, lat, lng, id)
                        break;
                    case 'Boisko':
                        addMarker(pitch, lat, lng, id)
                        break;
                    case 'Rowery':
                        addMarker(bike, lat, lng, id)
                        break;
                    case 'Basen':
                        addMarker(swim, lat, lng, id)
                        break;
                    case 'Park':
                        addMarker(forest, lat, lng, id)
                        break;
                    default:
                        addMarker(gym, lat, lng, id)
                        break;
            }  
        }
             
    } 
    myMarkers.addTo(mymap);  
}




navigator.geolocation.getCurrentPosition(position => addCurrentLocation(position.coords.latitude, position.coords.longitude),
					 error => addCurrentLocation(52.219761, 21.002734));

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

function encodeQueryData(data) {
   const ret = [];
   for (let d in data)
     ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(data[d]));
   return ret.join('&');
}

function addMarker(type, lat, lng, id) {
    var dist = distance(lat, lng, "K");

    var marker = L.marker([lat, lng], {icon: type})
    var data = {'id' : id};
    marker.url = '/gym?'+encodeQueryData(data);
    marker.on('click', function(){
        window.location = (this.url);
    });
    marker.addTo(myMarkers);
}

function myView() {
    mymap.panTo([mylat, mylng]);
    mymap.setZoom(16);  
}

