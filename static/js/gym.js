var mylat;
var mylng;

function saveLocation(lat, lng) {
  mylat = lat;
  mylng = lng;
}

navigator.geolocation.getCurrentPosition(position => saveLocation(52.219761, 21.002734));

console.log(mylat);
console.log(mylng);

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


console.log(gym_lng);

var dist = distance(gym_lat, gym_lng, "K");
document.getElementById("odleglosc").innerHTML = dist;
console.log(dist);