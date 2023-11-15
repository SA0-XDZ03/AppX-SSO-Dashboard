// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13);

// Add a base map layer (e.g., OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Create an empty markers layer group
var markers = L.layerGroup().addTo(map);

// Function to add a custom marker with popup content
function addCustomMarker(lat, lon, title, description, reference) {
    var customIcon = L.divIcon({
        className: 'custom-marker',
        // Define an empty popup content for now
        html: ''
    });

/*
    '<div class="marker-title">' + title + '</div>' +
    '<div class="marker-description">' + description + '</div>' +
    '<div class="marker-reference"><a href="' + reference + '" target="_blank">More info</a></div>'
*/

    var marker = L.marker([lat, lon], { icon: customIcon }).addTo(markers);

    // Create a popup for each marker
    var popup = L.popup({ minWidth: 250 });
    
    // Bind the popup to the marker
    marker.bindPopup(popup);

    // Add a click event to open the popup and set the content
    marker.on('click', function () {
        popup.setContent(
            '<div class="marker-title">' + title + '</div>' +
            '<div class="marker-description">' + description + '</div>' +
            '<div class="marker-reference"><a href="' + reference + '" target="_blank">More info</a></div>'
        ).openPopup();
    });
}

// Example: Add a custom marker dynamically
addCustomMarker(51.5, -0.09, 'Custom Marker 1', 'This is the first custom marker.', 'https://example.com/more-info-1');
addCustomMarker(51.51, -0.1, 'Custom Marker 2', 'This is the second custom marker.', 'https://example.com/more-info-2');
