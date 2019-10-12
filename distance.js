function distance(lat2, lon2, unit) {
      var lat1 = position.coords.latitude;
      var lon1 = position.coords.longitude;
    	var radlat1 = Math.PI * lat1/180
    	var radlat2 = Math.PI * lat2/180
    	var theta = lon1-lon2
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

    var data = [{
        "code": "0001",
        "lat": "1.28210155945393",
        "lng": "103.81722480263163",
        "location": "Stop 1"
    }, {
        "code": "0003",
        "lat": "1.2777380589964",
        "lng": "103.83749709165197",
        "location": "Stop 2"
    }, {
        "code": "0002",
        "lat": "1.27832046633393",
        "lng": "103.83762574759974",
        "location": "Stop 3"
    }];

    var html = "";
    var poslat = 1.28210155945393;
    var poslng = 103.81722480263163;


    for (var i = 0; i < data.length; i++) {
        // if this location is within 0.1KM of the user, add it to the list
        if (distance(data[i].lat, data[i].lng, "K") <= 0.1) {
            html += '<p>' + data[i].location + ' - ' + data[i].code + '</p>';
        }
    }

    $('#nearbystops').append(html);
