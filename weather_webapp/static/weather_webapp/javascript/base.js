/*
* Shows alert to sign up when anonymous user tries to change units
*/
unit_bnt = document.querySelector("#change-unit")
if (unit_bnt != null) {
    unit_bnt.onclick = function () {
        alert("Sign up to change units")
    }
}

/*
* Alert message function
*/
function alertMsg(message) {
    alert(message)
}

/*
* Gets user location, then fetches data from openweather api and updates the current location weather
*/
function getLocation() {
    navigator.geolocation.getCurrentPosition(showPosition)
}

function showPosition(position) {
    fetch(window.location.href, {
        method: "POST",
        body: JSON.stringify({
            location: [position.coords.latitude, position.coords.longitude]
        }),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            'X-CSRFToken': CSRF_TOKEN
        }
    })
}