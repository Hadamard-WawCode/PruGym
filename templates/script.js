var mymap = L.map('mapid')
var mylat;
var mylng;

var dumbbell = L.icon({
    iconUrl: 'pic/dumbbell-solid.svg',
    iconSize: [38, 40],
    iconAnchor: [0, 0],
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

    var marker = L.marker([mylat, mylng], {icon: dumbbell}).addTo(mymap);
});

function myView() {
    /*
    if(mylat === null or mylng === null){
        console.log("Brak danych o lokalizacji!");
    }
    */
    
    mymap.panTo([mylat, mylng]);
    // mymap.setZoom(16);  
}