function toggleLed() {
    fetch('http://127.0.0.1:5000/toggle_led')
}

document.getElementById('toggle-btn').onclick = function() {
    toggleLed();
}