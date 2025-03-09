TOGGLE_URL = 'http://127.0.0.1:5000/toggle_led'

function toggleLed() {
	fetch(TOGGLE_URL)
}

document.getElementById('toggle-btn').onclick = function() {
	toggleLed();
}