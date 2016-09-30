function createMap(data, center){

    L.mapbox.accessToken = 'pk.eyJ1IjoibWlsbHpwYXVnaCIsImEiOiJjaWxzbWtzdHYwMDJndTlrcmZzZHNlMjBuIn0.Zw-IWCL1tBvlh5NKKKlTsg';

    var markers = data

    var map = L.mapbox.map('map', 'mapbox.streets')
    .setView(center, 12)

    var myLayer = L.mapbox.featureLayer().addTo(map);

    myLayer.setGeoJSON(markers);

    var info = document.getElementById('info');

    myLayer.eachLayer(function(marker) {
        var link = info.appendChild(document.createElement('a'));
        link.className = 'item';
        link.href = '#';

        // Populate content from each markers object.
        link.innerHTML = marker.feature.properties.title +
        '<br /><small>' + marker.feature.properties.description + '</small>';
        link.onclick = function() {
        if (/active/.test(this.className)) {
          this.className = this.className.replace(/active/, '').replace(/\s\s*$/, '');
        } else {
          var siblings = info.getElementsByTagName('a');
          for (var i = 0; i < siblings.length; i++) {
            siblings[i].className = siblings[i].className
              .replace(/active/, '').replace(/\s\s*$/, '');
          };
          this.className += ' active';
        }
        return false;
        };
    });
}

function createMarkerMap(data, center){

    L.mapbox.accessToken = 'pk.eyJ1IjoibWlsbHpwYXVnaCIsImEiOiJjaWxzbWtzdHYwMDJndTlrcmZzZHNlMjBuIn0.Zw-IWCL1tBvlh5NKKKlTsg';

    var markers = data

    var map = L.mapbox.map('map', 'mapbox.streets')
    .setView(center, 16)

    var geojson = data 

    var myLayer = L.mapbox.featureLayer().setGeoJSON(geojson).addTo(map);
    map.scrollWheelZoom.disable();

    var myLegendLayer = L.mapbox.featureLayer().addTo(map);

    var info = document.getElementById('info');

    myLayer.eachLayer(function(marker) {
        var link = info.appendChild(document.createElement('a'));
        link.className = 'item';
        link.href = '#';

        // Populate content from each markers object.
        link.innerHTML = marker.feature.properties.title +
        '<br /><small>' + marker.feature.properties.description + '</small>';
        link.onclick = function() {
        if (/active/.test(this.className)) {
          this.className = this.className.replace(/active/, '').replace(/\s\s*$/, '');
        } else {
          var siblings = info.getElementsByTagName('a');
          for (var i = 0; i < siblings.length; i++) {
            siblings[i].className = siblings[i].className
              .replace(/active/, '').replace(/\s\s*$/, '');
          };
          this.className += ' active';
        }
        return false;
        };
    });


}






