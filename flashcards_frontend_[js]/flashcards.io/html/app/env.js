class Settings {

	static domain = 'http://0.0.0.0:1987'
	static login_endpoint = '/flashcards/login/'
	static register_endpoint = '/flashcards/register/'
	static get_profile_pic_endpoint = '/flashcards/get_profile_pic/'
	static signup_endpoint = '/flashcards/signup/'
	static post_profile_pic_endpoint = '/flashcards/post_profile_pic/'
	static delete_user_endpoint = '/flashcards/delete_user/'
	static delete_deck_endpoint = '/flashcards/delete_deck/'
	static delete_card_endpoint = '/flashcards/delete_card/'
	static add_deck_endpoint = '/flashcards/add_deck/'
	static edit_deck_endpoint = '/flashcards/edit_deck/'
	static edit_user_endpoint = '/flashcards/edit_user/'
	static add_card_endpoint = '/flashcards/add_card/'
	static post_deck_cover_endpoint = '/flashcards/post_deck_cover/'
	static get_all_decks_endpoint = '/flashcards/get_all_decks/'
	static get_deck_cover_endpoint = '/flashcards/get_deck_cover'
	static post_deck_pic_endpoint = '/flashcards/post_deck_pic'
	static get_queue_endpoint = '/flashcards/get_queue/'
	static get_all_cards_endpoint = '/flashcards/get_all_cards'
	static get_card_pic_endpoint = '/flashcards/get_card_pic'
	static update_deck_activity_endpoint = '/flashcards/update_deck_activity'
	static get_last_card_endpoint = '/flashcards/get_last_card'
	static copy_example_deck_endpoint = '/flashcards/copy_example_deck'
	static move_card_endpoint = '/flashcards/move_card'
	static check_connection_endpoint = '/flashcards/check_connection'

	static title = 'flashcards'

	static getTitle() {
		return Settings.title
	}

	static getFullUrl(endpoint){
		return Settings.domain+endpoint
	}
}



