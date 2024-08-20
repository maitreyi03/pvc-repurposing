// Initialize Google Map
function initMap() {
    var locations = [
        {lat: -37.8136, lng: 144.9631}, // Example location 1
        {lat: -37.8150, lng: 144.9650}, // Example location 2
        {lat: -37.8160, lng: 144.9670}  // Example location 3
    ];
    
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: locations[0]
    });
    
    locations.forEach(function(location) {
        new google.maps.Marker({
            position: location,
            map: map
        });
    });
}

// Handle account creation form
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Account created successfully!');
});
