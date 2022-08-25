"use strict"

class Display_handler {


	constructor() {
		let request_handler = new Request_handler
	}


	print_small_decks(data) {

		if (data.length == 0) {
			document.getElementById('no_decks_error').innerHTML = '<p>you have no decks</p><br>'
		}
		else {

			for (const deck of data) {
			
				document.getElementById('decks_div').innerHTML += '<div class="deck_small"><br><div id="cover_' + deck.UUID + '"></div><p> ' + deck.name + '</p><p id="' + deck.UUID + '" class="deck_button" onclick="request_handler.learn_deck_redirect(this.id)">learn</p> <p id="' + deck.UUID + `" class="deck_button" onclick="request_handler.add_card_redirect(this.id)">add</p><p id="` + deck.UUID + `" class="deck_button" onclick="request_handler.edit_deck_redirect(this.id)">edit</p> </div>`
				
				request_handler.get_deck_cover(deck.UUID)

			}
		}

	}


	print_full_card(data) {

		if (data.length == 0) {
			document.getElementById('no_cards_error').innerHTML = '<p>the deck is empty</p><br>'
		}
		else {

			for (const deck of data) {
			
				document.getElementById('cards_div').innerHTML += '<div class="white_space"><br><div id="' + 'f_pic1_' + deck.UUID + '"></div><div id="' + 'f_pic2_' + deck.UUID + '"></div> <p>' + deck.f_text + '</p> <br><hr><br> <div id="' + 'b_pic1_' + deck.UUID + '"></div><div id="' + 'b_pic2_' + deck.UUID + '"></div><p>' + deck.b_text + '</p> <p  id="' + deck.UUID + '" onclick="request_handler.delete_card(this.id)" class="card_delete_button">delete card</p></div><br>'
				
				if (deck.f_pic1_path != '') request_handler.print_full_card_pic(deck, 'f_pic1_path')
				if (deck.f_pic2_path != '') request_handler.print_full_card_pic(deck, 'f_pic2_path')
				if (deck.b_pic1_path != '') request_handler.print_full_card_pic(deck, 'b_pic1_path')
				if (deck.b_pic2_path != '') request_handler.print_full_card_pic(deck, 'b_pic2_path')

			}
		}

	}


	print_card_side(flip_side=false) {

		var object = {}
		object['user'] = Cookie.getCookie('current_user_name')
		object['deck_uuid'] = Cookie.getCookie('current_deck')

		var dataJsonString = JSON.stringify(object)

		const fetchOptions = {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"Accept": "application/json"
			},
			body: dataJsonString,
		};

		fetch(Settings.getFullUrl(Settings.get_last_card_endpoint), fetchOptions)
		.then(response => {
		 return response.json()
		})
		.then(data => {

			console.log('card: ', data)

			document.getElementById('cards_div').remove()
			document.getElementById('cards_div_outer').innerHTML = '<div id="cards_div"></div>'
			
			if (!flip_side) {

				console.log(1)

				document.getElementById('cards_div').innerHTML = '<div id="' + 'side_' + data.UUID + '"><div class="white_space"><div id="' + 'f_pic1_' + data.UUID + '"></div><div id="' + 'f_pic2_' + data.UUID + '"></div><br><div id="' + 'f_text_' + data.UUID + '"><p>' + data.f_text + '</p></div><br></div><br><br><button id="' + data.UUID + '" class="button_white" onclick="display_handler.print_card_side(true)"> flip card </button></div>'

				console.log(2)

				if (data.f_pic1_path != '') request_handler.print_learn_pic(data, 'f_pic1_path')
				if (data.f_pic2_path != '') request_handler.print_learn_pic(data, 'f_pic2_path')

			} 
			else {

				document.getElementById('cards_div').innerHTML = '<div id="' + 'side_' + data.UUID + '"><div class="white_space"><div id="' + 'b_pic1_' + data.UUID + '"></div><div id="' + 'b_pic2_' + data.UUID + '"></div><br><div id="' + 'f_text_' + data.UUID + '"><p>' + data.b_text + '</p></div><br></div><br><br>'

				document.getElementById('cards_div').innerHTML += '<p>how easy was it to recall the card? <br><br></p>'
				document.getElementById('cards_div').innerHTML += '<button id="' + data.UUID + '" class="button_white recall_rate_button" onclick="request_handler.move_card(this.id, 1)"> 1 </button>'
				document.getElementById('cards_div').innerHTML += '<button id="' + data.UUID + '" class="button_white recall_rate_button" onclick="request_handler.move_card(this.id, 2)"> 2 </button>'
				document.getElementById('cards_div').innerHTML += '<button id="' + data.UUID + '" class="button_white recall_rate_button" onclick="request_handler.move_card(this.id, 3)"> 3 </button>'
				document.getElementById('cards_div').innerHTML += '<button id="' + data.UUID + '" class="button_white recall_rate_button" onclick="request_handler.move_card(this.id, 4)"> 4 </button>'
				document.getElementById('cards_div').innerHTML += '<button id="' + data.UUID + '" class="button_white recall_rate_button" onclick="request_handler.move_card(this.id, 5)"> 5 </button>'
				document.getElementById('cards_div').innerHTML += '<br><p style="margin-right:92px; display: inline-block">very hard</p> <p style="margin-left:92px; display: inline-block">very easy</p><br>'
				document.getElementById('cards_div').innerHTML += '</div>'

				if (data.b_pic1_path != '') request_handler.print_learn_pic(data, 'b_pic1_path')
				if (data.b_pic2_path != '') request_handler.print_learn_pic(data, 'b_pic2_path')

			}

		})
		.catch(error => {
			console.log(error)
		})

	}

}