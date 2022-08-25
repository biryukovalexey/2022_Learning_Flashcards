from fastapi.responses import JSONResponse
import json
from api.internal.db_controller import Mysql_handler
from fastapi import APIRouter, Query, Depends, status, HTTPException, Body
from fastapi.responses import JSONResponse
from core.config import settings

import mysql.connector

import shutil
import os
import math

class Request_handler():

	def __init__(self):
		self.mysql_handler = Mysql_handler()


	def authenticate(self, data):

		try:

			result = self.mysql_handler.get_password(data.get(b'name'))

			if result == 'user does not found':
				return {'content': 'user does not found', 'code': status.HTTP_404_NOT_FOUND}

			if data.get(b'password') == result:
				print('AUTHENTICATED')
				
				return {'content': 'AUTHENTICATED', 'code': status.HTTP_200_OK}
			else:
				print('DOES NOT AUTHENTICATED')
				return {'content': 'incorrect password', 'code': status.HTTP_401_UNAUTHORIZED}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def get_profile_picture(self, data):

		try:
			
			full_path = settings.PROJECT_PATH + r"/storage/profile_pictures/"
			full_path += self.mysql_handler.get_profile_pic_path(data.get(b'name'))
			return full_path

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def add_user(self, data):

		try:

			if self.mysql_handler.does_user_exist(data.get(b'name')):
				return  {'content': 'e_this name has already taken', 'code': status.HTTP_406_NOT_ACCEPTABLE}

			if data.get(b'name') == '':
				return  {'content': 'e_please, input a name', 'code': status.HTTP_400_BAD_REQUEST}

			if data.get(b'password') == '':
				return  {'content': 'e_please, input a password', 'code': status.HTTP_400_BAD_REQUEST}

			profile_pic_name = data.get(b'profile_pic_name')

			if data.get(b'profile_pic_name') == None:
				profile_pic_name = 'default.jpg'

			result = self.mysql_handler.add_user(data, profile_pic_name)

			old_path = settings.PROJECT_PATH + "/storage/default/fun with flags"
			new_path = settings.PROJECT_PATH + "/storage/data/" + data.get(b'name') + "/fun with flags"

			shutil.copytree(old_path, new_path)

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}



	def copy_example_deck(self, data):

		try:

			user_name = data.get(b'user_name')

			self.mysql_handler.copy_example_deck(user_name)

			return True

		except Exception as exception:
			print(exception)
			return {'content': True, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}



	def delete_user(self, data):

		try:

			name = data.get(b'name')

			profile_pic_path = self.mysql_handler.get_profile_pic_path(name)

			result = self.mysql_handler.delete_user(name)

			if profile_pic_path != 'default.jpg':
				os.remove(settings.PROJECT_PATH + '/storage/profile_pictures/' + profile_pic_path)
			shutil.rmtree(settings.PROJECT_PATH + '/storage/data/' + name)

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def delete_deck(self, data):

		try:

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))

			deck_name = deck.get('name')
			deck_user = deck.get('user')

			self.mysql_handler.delete_deck(deck_name, deck_user)

			shutil.rmtree(settings.PROJECT_PATH + '/storage/data/' + deck_user + '/' + deck_name)

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def update_deck_activity(self, data):

		try:

			deck = self.mysql_handler.update_deck_activity(data.get(b'deck_uuid'))

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def add_deck(self, data):

		try:

			if self.mysql_handler.does_deck_exist(data.get(b'name'), data.get(b'user')):
				return  {'content': 'e_this name has already used', 'code': status.HTTP_406_NOT_ACCEPTABLE}

			result = self.mysql_handler.add_deck(data)

			os.mkdir(settings.PROJECT_PATH + '/storage/data/' + data.get(b'user') + '/' + data.get(b'name'))

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}



	def get_all_decks(self, data):

		try:
			
			result = self.mysql_handler.get_all_decks(data.get(b'user'))

			return result

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}



	def get_all_cards(self, data):

		try:
			
			result = self.mysql_handler.get_all_cards(data)
			return result

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}



	def get_deck_cover(self, data):

		try:

			full_path = ''

			if self.mysql_handler.does_have_custom_cover(data.get(b'cover_uuid')) == 0: 
				full_path = settings.PROJECT_PATH + '/storage/default/default_deck_cover.jpg'
			else:
				deck = self.mysql_handler.get_deck_by_uuid(data.get(b'cover_uuid'))
				full_path = settings.PROJECT_PATH + '/storage/data/' + deck.get('user') + '/' + deck.get('name')  + '/cover.jpg'

			return full_path

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def get_card_pic(self, data):

		try:

			pic_name = self.mysql_handler.get_card_pic_name(data.get(b'card_uuid'), data.get(b'request'))

			card = self.mysql_handler.get_card_by_uuid(data.get(b'card_uuid'))

			full_path = settings.PROJECT_PATH + '/storage/data/' + card.get('user') + '/' + card.get('deck')  + '/' + pic_name

			return full_path

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def get_queue(self, data):

		try:

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))

			cards_number = self.mysql_handler.get_cards_number(deck.get('name'), data.get(b'user'))
			return cards_number+1

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def get_last_card(self, data):

		try:

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))
			card = self.mysql_handler.get_last_card(deck.get('name'), data.get(b'user'))
			return card

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def add_card(self, data):

		try:

			result = self.mysql_handler.add_card(data)
			return  {'content': result, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def delete_card(self, data):

		try:

			result = self.mysql_handler.delete_card(data.get(b'card_id'))

			if result.get('f_pic1_name') != '': self.delete_file(settings.PROJECT_PATH + '/storage/data/' + result.get('user') + '/' + result.get('deck_name') + '/' + result.get('f_pic1_name'))
			if result.get('f_pic2_name') != '': self.delete_file(settings.PROJECT_PATH + '/storage/data/' + result.get('user') + '/' + result.get('deck_name') + '/' + result.get('f_pic2_name'))
			if result.get('b_pic1_name') != '': self.delete_file(settings.PROJECT_PATH + '/storage/data/' + result.get('user') + '/' + result.get('deck_name') + '/' + result.get('b_pic1_name'))
			if result.get('b_pic2_name') != '': self.delete_file(settings.PROJECT_PATH + '/storage/data/' + result.get('user') + '/' + result.get('deck_name') + '/' + result.get('b_pic2_name'))

			return  {'content': result.get('UUID'), 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def delete_file(self, path):

		try:
			
			os.remove(path)

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def get_new_queue(self, cards_number, rate):

		if rate == 1:
			return 2
		if rate == 2:
			return math.floor(cards_number * 0.25)
		if rate == 3:
			return math.floor(cards_number * 0.5)
		if rate == 4:
			return math.floor(cards_number * 0.75)
		if rate == 5:
			return cards_number
		

	def move_card(self, data):

		try:

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))
			deck_name = deck.get('name')

			cards_number = self.get_queue( {b'deck_uuid': data.get(b'deck_uuid'), b'user': data.get(b'user')} )-1

			new_queue = self.get_new_queue(cards_number, data.get(b'rate'))

			result = self.mysql_handler.move_card(new_queue, deck_name, data.get(b'user'))

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def edit_deck(self, data):

		try:

			if ((data.get(b'name') == '') and (data.get(b'custom_cover') is None)):
				return True

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))
			deck_name = deck.get('name')

			result = self.mysql_handler.edit_deck(data, deck_name)

			if (data.get(b'name') != ''):

				from_dir = settings.PROJECT_PATH + "/storage/data/" + data.get(b'user') + "/" + deck_name
				to_dir = settings.PROJECT_PATH + "/storage/data/" + data.get(b'user') + "/" + data.get(b'name')

				os.mkdir(to_dir)

				for file in os.listdir(from_dir):
				    shutil.move(os.path.join(from_dir, file), to_dir)

				shutil.rmtree(from_dir)

			if (data.get(b'custom_cover') is not None):
				deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))
				deck_name = deck.get('name')
				cover_path = settings.PROJECT_PATH + "/storage/data/" + data.get(b'user') + "/" + deck_name + "/cover.jpg"
				if os.path.isfile(cover_path):
					os.remove(cover_path)

			deck = self.mysql_handler.get_deck_by_uuid(data.get(b'deck_uuid'))
			deck_name = deck.get('name')
			return deck_name

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}


	def edit_user(self, data):

		try:

			if ((data.get(b'name') == '') and (data.get(b'password') == '') and (data.get(b'profile_pic_path') is None)):
				return True

			result = self.mysql_handler.edit_user(data)

			old_profile_picture = result.get('profile_pic_path')

			if (data.get(b'name') != ''):

				from_dir = settings.PROJECT_PATH + "/storage/data/" + data.get(b'old_user_name')
				to_dir = settings.PROJECT_PATH + "/storage/data/" + data.get(b'name')

				os.mkdir(to_dir)

				for file in os.listdir(from_dir):
				    shutil.move(os.path.join(from_dir, file), to_dir)

				shutil.rmtree(from_dir)

			if ( data.get(b'profile_pic_path') is not None ):

				if old_profile_picture != 'default.jpg':

					old_profile_picture_path = settings.PROJECT_PATH + "/storage/profile_pictures/" + old_profile_picture

					if os.path.isfile(old_profile_picture_path):
						os.remove(old_profile_picture_path)

			return  {'content': True, 'code': status.HTTP_200_OK}

		except Exception as exception:
			print(exception)
			return {'content': False, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR}