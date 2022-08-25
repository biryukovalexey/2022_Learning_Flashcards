"use strict"

class Utilities {

	static UUID4(){
		return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
		(c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
		);
	}


	static start_connection_checker() {

		var intervalID = window.setInterval(myCallback, 1000);

        function myCallback() {

			const fetchOptions = {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
					"Accept": "application/json"
				}
			};

			fetch(Settings.getFullUrl(Settings.check_connection_endpoint), fetchOptions)
			.then(response => {
			 return response.json()
			})
			.then(connection_lost => {
				console.log('connection_ok')
				document.getElementById('connection_lost').style.visibility = "hidden"
			})
			.catch(error => {
				console.log('connection_lost')
				document.getElementById('connection_lost').style.visibility = "visible"
			})

        }
	}

}