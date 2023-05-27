$(document).ready(function () {
    var defaultLatLng = {lat: -34.397, lng: 150.644};  // Set a default center point

    var mapOptions = {
        zoom: 8,
        center: defaultLatLng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("id_location-map-canvas"), mapOptions);

    var marker;
    google.maps.event.addListener(map, 'click', function (event) {
        placeMarker(event.latLng);
        geocodeLatLng(event.latLng);
    });

    function placeMarker(location) {
        if (marker) {
            marker.setPosition(location);
        } else {
            marker = new google.maps.Marker({
                position: location,
                map: map
            });
        }
    }

    function geocodeLatLng(latLng) {
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({'location': latLng}, function (results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
                if (results[0]) {
                    var address = results[0].formatted_address;
                    $('#id_location').val(address);
                } else {
                    console.log('No results found');
                }
            } else {
                console.log('Geocoder failed due to: ' + status);
            }
        });
    }
});
