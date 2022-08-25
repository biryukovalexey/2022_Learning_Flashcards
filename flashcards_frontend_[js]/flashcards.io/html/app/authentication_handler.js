"use strict"

class Authentication_handler {

	constructor() {
		let request_handler = new Request_handler
	}

	log_into_current_user() {
		if (Cookie.getCookie("current_user_name") != 'unauthorized' && Cookie.getCookie("current_user_name") !== undefined) location.href = "views/decks.html"

	}
	
	login(form) {
		let result = request_handler.login(form)
	
		return result
	}

	signup(form) {
		let result = request_handler.signup(form)
	
		return result
	}

	log_out() {
		Cookie.setCookie("current_user_name", 'unauthorized')
		location.href = "../index.html"
	}
}