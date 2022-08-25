"use strict"

class Request_handler {


	async login(formElement) {

		const url = Settings.getFullUrl(Settings.login_endpoint)

		const data = new URLSearchParams();
		for (const pair of new FormData(formElement)) {
		    data.append(pair[0], pair[1]);
		}
	    
		var object = {};
		data.forEach(function(value, key){
		    object[key] = value;
		});
		var formDataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString,
		};
		
		fetch(url, fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			if (data.content == 'AUTHENTICATED') {
				Cookie.setCookie("current_user_name", object.name)
				location.href = "views/decks.html"
			}
				
			else document.getElementById('error_div').innerHTML = '<p id="error_p">' + data.content + '</p>'
	
		})
		.catch(error => {
			console.log(error)
		})
	}


	async signup(formElement, selector_id = '#imginput') {

		let fileInput = document.querySelector(selector_id)
		let formData = new FormData()

		let profile_pic_name = Utilities.UUID4()

		const url = Settings.getFullUrl(Settings.signup_endpoint)

		const data = new URLSearchParams();
		for (const pair of new FormData(formElement)) {
		    data.append(pair[0], pair[1]);
		}

		let file_inputted = false

		if (document.getElementById(selector_id.slice(1)).files.length !== 0) {
			data.append('profile_pic_name', profile_pic_name)
			data.append('original_pic_name', fileInput.files[0].name);
			file_inputted = true
		}
	    
		var object = {};
		data.forEach(function(value, key){
		    object[key] = value;
		});

		let user_name = object["name"]

		var formDataJsonString = JSON.stringify(object)

		if (object.password != object.rpassword) {
			document.getElementById('error_div').innerHTML = '<p id="error_p">passwords do not match</p>'
			return false
		}

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString,
		}
		
		fetch(url, fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			let content = data.content

			if (content == true) {

				if (file_inputted) {		

					formData.append('file', fileInput.files[0])

				    const options = {
				      method: 'POST',
				      headers: {
					      "uuid_name": profile_pic_name
					    },
				      body: formData
				    };
				    fetch(Settings.getFullUrl(Settings.post_profile_pic_endpoint), options)

				}

				this.copy_example_deck(user_name)
				alert('Welcome!')
				Cookie.setCookie('decks_message', 'try out the example deck:')
				location.href = "../index.html"
			}
			else {
				document.getElementById('error_div').innerHTML = '<p id="error_p">' + content.slice(2) + '</p>'
			}

			
	
		})
		.catch(error => {
			console.log(error)
		})
	}


	copy_example_deck(user_name) {

		var object = {}
		object['user_name'] = user_name

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		body: dataJsonString,
		}	
				
		fetch(Settings.getFullUrl(Settings.copy_example_deck_endpoint), fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log(data)
			
		})
		.catch(error => {
			console.log(error)
		})

	}


	add_card(formElement1, formElement2) {

		var object1 = {}
		object1['deck_uuid'] = Cookie.getCookie('current_deck')
		object1['user'] = Cookie.getCookie('current_user_name')

		var formDataJsonString1 = JSON.stringify(object1)

		console.log(formDataJsonString1)

		const fetchOptions1 = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString1
		}
		
		fetch(Settings.getFullUrl(Settings.get_queue_endpoint), fetchOptions1)
		.then(response1 => {
			return response1.json()
		})
		.then(data1 => {

			let imginput_f1_selector = '#imginput_f1'
			let imginput_f2_selector = '#imginput_f2'
			let imginput_b1_selector = '#imginput_b1'
			let imginput_b2_selector = '#imginput_b2'

			let imginput_f1 = document.querySelector(imginput_f1_selector)
			let imginput_f2 = document.querySelector(imginput_f2_selector)
			let imginput_b1 = document.querySelector(imginput_b1_selector)
			let imginput_b2 = document.querySelector(imginput_b2_selector)

			let imginput_f1_name = Utilities.UUID4()
			let imginput_f2_name = Utilities.UUID4()
			let imginput_b1_name = Utilities.UUID4()
			let imginput_b2_name = Utilities.UUID4()

			let imginput_f1_inputted = false
			let imginput_f2_inputted = false
			let imginput_b1_inputted = false
			let imginput_b2_inputted = false

			let formData = new FormData()

			const data = new URLSearchParams();
			for (const pair of new FormData(formElement1)) {
			    data.append(pair[0], pair[1]);
			}
			for (const pair of new FormData(formElement2)) {
			    data.append(pair[0], pair[1]);
			}

			data.append('user', Cookie.getCookie('current_user_name'))
			data.append('deck', Cookie.getCookie('current_deck'))

			data.append('queue', data1)

			if (document.getElementById(imginput_f1_selector.slice(1)).files.length !== 0) {
			data.append('imginput_f1_name', imginput_f1_name)
			data.append('imginput_f1_original_name', imginput_f1.files[0].name);
				imginput_f1_inputted = true
			}
			if (document.getElementById(imginput_f2_selector.slice(1)).files.length !== 0) {
				data.append('imginput_f2_name', imginput_f2_name)
				data.append('imginput_f2_original_name', imginput_f2.files[0].name);
				imginput_f2_inputted = true
			}
			if (document.getElementById(imginput_b1_selector.slice(1)).files.length !== 0) {
				data.append('imginput_b1_name', imginput_b1_name)
				data.append('imginput_b1_original_name', imginput_b1.files[0].name);
				imginput_b1_inputted = true
			}
			if (document.getElementById(imginput_b2_selector.slice(1)).files.length !== 0) {
				data.append('imginput_b2_name', imginput_b2_name)
				data.append('imginput_b2_original_name', imginput_b2.files[0].name);
				imginput_b2_inputted = true
			}
		    
			var object = {};
			data.forEach(function(value, key){
			    object[key] = value;
			});
			var formDataJsonString = JSON.stringify(object)


			console.log(formDataJsonString)

			const fetchOptions2 = {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
					"Accept": "application/json"
				},
				body: formDataJsonString
			}
			
			fetch(Settings.getFullUrl(Settings.add_card_endpoint), fetchOptions2)
			.then(response2 => {
			 return response2.json()
			})
			.then(data2 => {

				let content = data2.content

				if (imginput_f1_inputted) this.post_deck_pic(imginput_f1, content.f_pic1_path)
				if (imginput_f2_inputted) this.post_deck_pic(imginput_f2, content.f_pic2_path)
				if (imginput_b1_inputted) this.post_deck_pic(imginput_b1, content.b_pic1_path)
				if (imginput_b2_inputted) this.post_deck_pic(imginput_b2, content.b_pic2_path)

				alert('card created')
				location.href = 'add_card.html'

			})
			.catch(error => {
				console.log(error)
			})

		})
		.catch(error1 => {
			console.log(error1)
		})

	}


	post_deck_pic(file_input, img_pic_name) {

		let formData = new FormData()

		formData.append('file', file_input.files[0])

		const options = {
			method: 'POST',
			headers: {
				"user_name": Cookie.getCookie('current_user_name'),
				"deck_uuid": Cookie.getCookie('current_deck'),
				"img_pic_name": img_pic_name
			},
			body: formData
		};
		fetch(Settings.getFullUrl(Settings.post_deck_pic_endpoint), options)

	}


	get_all_cards() {

		var object = {}
		object['user'] = Cookie.getCookie('current_user_name')
		object['deck'] = Cookie.getCookie('current_deck')

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.get_all_cards_endpoint), fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log('data from get_all_cards')
			console.log(data)

			display_handler.print_full_card(data)

		})
		.catch(error => {
			console.log(error)
		})

	}


	get_profile_pic(preview_mode = false) {

		var object = {}
		object['name'] = Cookie.getCookie('current_user_name')

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.get_profile_pic_endpoint), fetchOptions)
		.then(response => response.blob())
		.then(imageBlob => {
			const imageObjectURL = URL.createObjectURL(imageBlob)
			if (preview_mode) {
				document.getElementById('full_header').innerHTML += '<a href="decks.html" id="title"><h1 >' + Settings.getTitle() + '</h1></a></div>'
				document.getElementById('profile_pic_preview_div').innerHTML += '<img class="preview_profile_pic" src="' + imageObjectURL + '"> <p style="font-size: 30px;">' + Cookie.getCookie('current_user_name') + '</p>'
			}
			else document.getElementById('full_header').innerHTML += '<a href="decks.html" id="title"><h1 >' + Settings.getTitle() +'</h1></a><p id="profile_name" onclick="location.href = `profile.html`">' + Cookie.getCookie('current_user_name') + '</p><img onclick="location.href = `profile.html`" class="icon" id="profile_pic" src="' + imageObjectURL + '"></div>'			
		    return true
		})
	}


	delete_card(card_id) {

		if (confirm('are you sure?')) {

			var object = {}
			object['card_id'] = card_id

			var dataJsonString = JSON.stringify(object)

			const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
			}
				
			fetch(Settings.getFullUrl(Settings.delete_card_endpoint), fetchOptions)
			.then(response => {
			 return response.json()
			})
			.then(data => {

				console.log(data)
				location.href = 'edit_deck.html'
			
			})
			.catch(error => {
				console.log(error)
			})

		}

	}


	learn_deck_redirect(deck_uuid) {

		Cookie.setCookie('current_deck', deck_uuid)

		var object = {}
		object['deck_uuid'] = Cookie.getCookie('current_deck')
		object['user'] = Cookie.getCookie('current_user_name')

		var formDataJsonString = JSON.stringify(object)

		console.log(formDataJsonString)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString
		}
		
		fetch(Settings.getFullUrl(Settings.get_queue_endpoint), fetchOptions)
		.then(response => {
			return response.json()
		})
		.then(data => {

			if (data-1 > 0) {
				
				this.update_deck_activity(deck_uuid)
				location.href='learn.html'
			}
			else {
				alert('this deck is empty')
			}

		})
		.catch(error => {
			console.log(error)
		})

	}


	add_card_redirect(deck_uuid) {

		Cookie.setCookie('current_deck', deck_uuid)

		this.update_deck_activity(deck_uuid)

		location.href='add_card.html'

	}


	edit_deck_redirect(deck_uuid) {

		Cookie.setCookie('current_deck', deck_uuid)

		this.update_deck_activity(deck_uuid)

		location.href = 'edit_deck.html'

	}


	update_deck_activity(deck_uuid) {

		var object = {}
		object['deck_uuid'] = deck_uuid

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		body: dataJsonString,
		}
		
		fetch(Settings.getFullUrl(Settings.update_deck_activity_endpoint), fetchOptions)
		.then(response => {
			 return response.json()
		})
		.then(data => {

			console.log(data)
				
		})
		.catch(error => {
			console.log(error)
		})

	}


	delete_deck() {
		
		if(confirm("are you sure?")) {
			
			var object = {}
			object['deck_uuid'] = Cookie.getCookie('current_deck')

			var dataJsonString = JSON.stringify(object)

			const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
			}
				
			fetch(Settings.getFullUrl(Settings.delete_deck_endpoint), fetchOptions)
			.then(response => {
			 return response.json()
			})
			.then(data => {

				console.log(data)

				alert('deck deleted')
				location.href ='decks.html'
			
			})
			.catch(error => {
				console.log(error)
			})

			return true
		}

	}


	delete_user() {
		console.log('delete user')

		while(true) {

			let current_user_name = Cookie.getCookie('current_user_name')
			let user_name_confirmation = prompt('to detete your account, type "' + current_user_name + '" to confirm:')

			if (user_name_confirmation === null) return false

			if (current_user_name == user_name_confirmation) {
				var object = {}
				object['name'] = current_user_name

				var dataJsonString = JSON.stringify(object)

				const fetchOptions = {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
					"Accept": "application/json"
				},
				body: dataJsonString,
				}
				
				fetch(Settings.getFullUrl(Settings.delete_user_endpoint), fetchOptions)
				.then(response => {
				 return response.json()
				})
				.then(data => {

					console.log(data)
			
				})
				.catch(error => {
					console.log(error)
				})

				Cookie.setCookie('current_user_name', 'unauthorized')
				location.href ='../index.html'

				return false
			}
			else alert('please, try again')

		}

	}


	edit_deck(formElement, selector_id = '#imginput') {

		let fileInput = document.querySelector(selector_id)
		let formData = new FormData()

		const url = Settings.getFullUrl(Settings.edit_deck_endpoint)

		const data = new URLSearchParams();
		for (const pair of new FormData(formElement)) {
		    data.append(pair[0], pair[1]);
		}

		data.append('user', Cookie.getCookie('current_user_name'))
		data.append('deck_uuid', Cookie.getCookie('current_deck'))

		let file_inputted = false
		let delete_cover = false

		if (document.getElementById(selector_id.slice(1)).files.length !== 0) {

			data.append('custom_cover', true)
			file_inputted = true
		}

		if (Cookie.getCookie('set_default_cover') == 'true') {

			data.append('custom_cover', false)
			delete_cover = true
		}
	    
		var object = {};
		data.forEach(function(value, key){
		    object[key] = value;
		});
		var formDataJsonString = JSON.stringify(object)

		console.log(formDataJsonString)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString
		}
		
		fetch(url, fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log(data)
			
			if (file_inputted) {	

				let formData1 = new FormData()
				formData1.append('file', fileInput.files[0])

				const options = {
		        method: 'POST',
		        headers: {
			        "user_name": Cookie.getCookie('current_user_name'),
			        "deck_name": data
			    },
		  	        body: formData1
				};
			    fetch(Settings.getFullUrl(Settings.post_deck_cover_endpoint), options)

			}
			
			alert('done')
			location.href = "decks.html"

		})
		.catch(error => {
			console.log(error)
		})

	}


	edit_user(formElement, selector_id = '#imginput') {

		let fileInput = document.querySelector(selector_id)
		let formData = new FormData()

		let new_profile_pic_name = Utilities.UUID4()
		const url = Settings.getFullUrl(Settings.edit_user_endpoint)

		const data = new URLSearchParams();
		for (const pair of new FormData(formElement)) {
		    data.append(pair[0], pair[1]);
		}

		let old_user_name = Cookie.getCookie('current_user_name')
		data.append('old_user_name', old_user_name)

		let file_inputted = false
		let delete_profile_pic = false

		if (document.getElementById(selector_id.slice(1)).files.length !== 0) {

			data.append('profile_pic_path', new_profile_pic_name+'.jpg')
			file_inputted = true
		}

		if (Cookie.getCookie('custom_profile_pic') == 'true') {

			data.append('profile_pic_path', 'default.jpg')
			delete_profile_pic = true
		}
	    
		var object = {};
		data.forEach(function(value, key){
		    object[key] = value;
		});
		var formDataJsonString = JSON.stringify(object)

		if (object['password'] != object['rpassword'])  {
			document.getElementById('error_div').innerHTML = '<p id="error_p">passwords does not match</p><br>'
			return false
		}

		let new_user_name = object['name']

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString
		}
		
		fetch(url, fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			if (file_inputted) {	

				let formData1 = new FormData()
				formData1.append('file', fileInput.files[0])

				    const options = {
				      method: 'POST',
				      headers: {
					      "uuid_name": new_profile_pic_name
					    },
				      body: formData1
				    };
				    fetch(Settings.getFullUrl(Settings.post_profile_pic_endpoint), options)
			}
			
			if (new_user_name != '') Cookie.setCookie("current_user_name", new_user_name)
			location.href = "decks.html"

		})
		.catch(error => {
			console.log(error)
		})

	}


	add_deck(formElement, selector_id = '#imginput') {

		let fileInput = document.querySelector(selector_id)
		let formData = new FormData()

		const url = Settings.getFullUrl(Settings.add_deck_endpoint)

		const data = new URLSearchParams();
		for (const pair of new FormData(formElement)) {
		    data.append(pair[0], pair[1]);
		}

		data.append('user', Cookie.getCookie('current_user_name'))

		let file_inputted = false

		if (document.getElementById(selector_id.slice(1)).files.length !== 0) {
			data.append('custom_cover', true)
			file_inputted = true
		}
		else {
			data.append('custom_cover', false)
		}
	    
		var object = {};
		data.forEach(function(value, key){
		    object[key] = value;
		});
		var formDataJsonString = JSON.stringify(object)


		if (object['name'] == '') {
			document.getElementById('error_div').innerHTML = '<p id="error_p">please, input name</p>'
			return false
		}

		console.log(formDataJsonString)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: formDataJsonString
		}
		
		fetch(url, fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log(data)

			let content = data.content

			if (content == true) {

				if (file_inputted) {		

					formData.append('file', fileInput.files[0])

				    const options = {
				      method: 'POST',
				      headers: {
					      "user_name": Cookie.getCookie('current_user_name'),
					      "deck_name": object['name']
					    },
				      body: formData
				    };
				    fetch(Settings.getFullUrl(Settings.post_deck_cover_endpoint), options)

				}
			}
			else {
				document.getElementById('error_div').innerHTML = '<p id="error_p">' + content.slice(2) + '</p>'
			}

			alert('created')
			location.href = "../index.html"

		})
		.catch(error => {
			console.log(error)
		})

	}


	get_all_decks() {

		var object = {}
		object['user'] = Cookie.getCookie('current_user_name')

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.get_all_decks_endpoint), fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log(data)

			display_handler.print_small_decks(data)

		})
		.catch(error => {
			console.log(error)
		})

	}


	get_deck_cover(cover_uuid, preview_mode = false) {

		var object = {}
		object['cover_uuid'] = cover_uuid

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.get_deck_cover_endpoint), fetchOptions)
		.then(response => response.blob())
		.then(imageBlob => {
			const imageObjectURL = URL.createObjectURL(imageBlob)
			if (preview_mode) {
				console_log('cover_preview_mode')
			}
			else document.getElementById('cover_' + cover_uuid).innerHTML = '<img class="deck_cover_small" src="' + imageObjectURL + '" ></img>'		
		    return true
		})
	}


	print_learn_pic(data, request) {

		var object = {}
		object['card_uuid'] = data.UUID
		object['request'] = request

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		let div_name = ''

		fetch(Settings.getFullUrl(Settings.get_card_pic_endpoint), fetchOptions)
		.then(response => response.blob())
		.then(imageBlob => {
			const imageObjectURL = URL.createObjectURL(imageBlob)

			div_name = request.slice(0,7) + data.UUID

			console.log(div_name)

			document.getElementById(div_name).innerHTML = '<br><br><img class="card_pic" src="' + imageObjectURL + '" ></img>'

		    return true
		})

	}


	move_card(card_uuid, rate) {

		var object = {}
		object['card_uuid'] = card_uuid
		object['deck_uuid'] = Cookie.getCookie('current_deck')
		object['user'] = Cookie.getCookie('current_user_name')
		object['rate'] = rate

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.move_card_endpoint), fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log(data)
			display_handler.print_card_side()

		})
		.catch(error => {
			console.log(error)
		})

	}


	print_full_card_pic(data, request) {

		var object = {}
		object['card_uuid'] = data.UUID
		object['request'] = request

		var dataJsonString = JSON.stringify(object)

		console.log("to send to get_card_pic_endpoint")
		console.log(dataJsonString)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		let div_name = ''

		fetch(Settings.getFullUrl(Settings.get_card_pic_endpoint), fetchOptions)
		.then(response => response.blob())
		.then(imageBlob => {
			const imageObjectURL = URL.createObjectURL(imageBlob)

			div_name = request.slice(0,7) + data.UUID

			console.log(div_name)

			document.getElementById(div_name).innerHTML = '<img class="card_pic" src="' + imageObjectURL + '" ></img>'

		    return true
		})

	}





}