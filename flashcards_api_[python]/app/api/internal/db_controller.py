import mysql.connector
import uuid
from core.config import settings
from fastapi import APIRouter, Query, Depends, status, HTTPException, Body
import json
import random
import os
import time

class Mysql_handler():


	def __init__(self):

		self.db = mysql.connector.connect(
			host=settings.MYSQL_HOST,
			user=settings.MYSQL_USER,
			password=settings.MYSQL_PASSWORD,
			database=settings.MYSQL_DB)


	def get_password(self, name):

		try:
		
			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute("SELECT password FROM users WHERE name = '" + name + "';")
			result = {}
			result = dictCursor.fetchall()
			if dictCursor.rowcount == 0:

				return 'user does not found'
			return result[0].get('password')

		except Exception as exception:
			print(exception)
			return False


	def copy_example_deck(self, user_name):

		try:

			query = "INSERT INTO decks (UUID, name, user, custom_cover, last_activity) VALUES ('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 1, " + str(time.time()) + ");"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 7, '2d8a6a7b-17e0-4ae9-b3e3-ec0acb8d2755.png', '0140419b-95e3-44d1-8495-7a4cba664061.png', 'Name the country', '', '', 'Greenland');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 10, '', '', 'How many human legs are on a Sicily flag?', '74eec214-4acd-4b86-8712-2d3f73370629.png', '609705f2-8279-4428-b566-e8647ce7cb96.png', '3 legs');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 3, '', '', 'The only flag in the world that does not have a rectangular shape', '98cc0e1d-90b3-4908-811d-fe16fcbbe10d.png', '81a60fc4-43a2-4ec9-bd5b-45925c258e7b.png', 'The flag of Nepal');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 4, '549a6435-05e1-41dc-885c-1127ebf71458.png', '', 'Name the country', '01aac522-435e-44cf-b7dd-196ae481055c.png', '609705f2-8279-4428-b566-e8647ce7cb96.png', 'Kyrgyzstan');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 5, '89890c99-5f60-4e82-b458-ea794d181217.png', '6b4fd2e3-b97d-4a54-93e2-3a0fae1c9c7e.png', 'Name the continent', '', '', 'Africa');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 6, '', '', 'Which flag is designed by Lafayette?', '81c3bb42-f1d8-4423-97c5-bfe0e550e708.png', '', 'France flag');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 1, '', '', 'Which flag has a red dragon? (name the country)', '418a014c-b10d-4b8d-8dff-d5f0bbae2bbc.png', '7d411c45-7c18-4438-b0d9-80c8e0705fcd.png', 'Wales');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 8, 'a76f0650-296f-41cb-b810-5085683e4c55.png', '', 'Name the country', '281f1eae-7089-4fed-92fb-c63343a41797.png', 'b493c2af-e209-4184-8aac-f97a55646161.jpg', 'Quatar');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 9, '541c7cc6-79f1-4217-82ae-b87ad72e108d.png', '0e763d8d-1d4a-4992-8930-80b5dab1d104.png', 'Name the continent', '', '', 'South America');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path , b_pic2_path, b_text) VALUES "
			query += "('" + str(uuid.uuid4()) +"', 'fun with flags', '" + user_name + "', 2, 'c3326784-d8cd-4485-a0ea-200919473824.png', '', 'What is the traditional English name for the flags flown to identify a pirate ship about to attack?', '', '', 'Jolly Roger');"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False


	def get_profile_pic_path(self, name):

		try:

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute("SELECT profile_pic_path FROM users WHERE name = '" + name + "';")

			result = {}
			result = dictCursor.fetchall()
			
			return result[0].get('profile_pic_path')
			
		except Exception as exception:
			print(exception)
			return False



	def does_user_exist(self, name):
		dictCursor = self.db.cursor(dictionary=True)
		dictCursor.execute("SELECT name FROM users WHERE name = '" + name + "';")
		result = {}
		result = dictCursor.fetchall()
		if dictCursor.rowcount == 0:
			return False
		return True

	def does_deck_exist(self, name, user):
		dictCursor = self.db.cursor(dictionary=True)
		dictCursor.execute("SELECT name FROM decks WHERE name = '" + name + "' AND user = '" + user + "';")
		result = {}
		result = dictCursor.fetchall()
		if dictCursor.rowcount == 0:
			return False
		return True


	def add_user(self, data, profile_pic_name):

		try:

			original_pic_name = data.get(b'original_pic_name')

			if (original_pic_name is not None): 
				filename, file_extension = os.path.splitext(original_pic_name)
				profile_pic_name += '.jpg'


			query = "INSERT INTO users (UUID, name, password, profile_pic_path) VALUES ('" 
			query += str(uuid.uuid4()) +"', '" + data.get(b'name') + "', '"
			query += data.get(b'password') + "', '" + profile_pic_name + "')"

			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False


	def add_deck(self, data):

		try:

			if (data.get(b'custom_cover') == 'false'): 
				custom_cover = '0'
			else: 
				custom_cover = '1'

			query = "INSERT INTO decks (UUID, name, user, custom_cover, last_activity) VALUES ('" + str(uuid.uuid4()) +"', '" + data.get(b'name') + "', '" + data.get(b'user') + "', '" + custom_cover + "', '" + str(time.time()) +"')"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			return True

		except Exception as exception:
			print(exception)
			return False


	def delete_user(self, name):

		try:
			
			cursor = self.db.cursor()
			cursor.execute("DELETE FROM users WHERE name = '" + name + "';")
			self.db.commit()

			cursor.execute("DELETE FROM decks WHERE user = '" + name + "';")
			self.db.commit()

			cursor.execute("DELETE FROM cards WHERE user = '" + name + "';")
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False



	def get_all_decks(self, user):

		try:

			query = "SELECT * FROM decks WHERE user = '" + user + "' ORDER BY last_activity DESC;"

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute(query)

			result = {}
			result = dictCursor.fetchall()

			print(result)
			print(dictCursor.rowcount)

			if dictCursor.rowcount == 0:
				return []

			records = []
			record = {}

			for item in result:
				record = {'UUID': item['UUID'], 'name': item['name'], 'user': item['user'], 'custom_cover': item['custom_cover'], 'last_activity': item['last_activity']}
				records.append(record)

			return records

		except Exception as exception:
			print(exception)
			return False


	def get_all_cards(self, data):

		try:

			deck = self.get_deck_by_uuid(data.get(b'deck'))
			deck_name = deck.get('name')

			query = "SELECT * FROM cards WHERE user = '" + data.get(b'user') + "' AND deck = '" + deck_name + "' ORDER BY queue;"

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute(query)

			result = {}
			result = dictCursor.fetchall()

			if dictCursor.rowcount == 0:
				return []

			records = []
			record = {}

			for item in result:
				record = {'UUID': item['UUID'], 'deck': item['deck'], 'user': item['user'], 'queue': item['queue'], 'f_pic1_path': item['f_pic1_path'], 'f_pic2_path': item['f_pic2_path'], 'f_text': item['f_text'], 'b_pic1_path': item['b_pic1_path'], 'b_pic2_path': item['b_pic2_path'], 'b_text': item['b_text']}
				records.append(record)

			return records

		except Exception as exception:
			print(exception)
			return False


	def does_have_custom_cover(self, data):

		dictCursor = self.db.cursor(dictionary=True)
		dictCursor.execute("SELECT custom_cover FROM decks WHERE UUID = '" + data + "';")

		result = {}
		result = dictCursor.fetchall()

		return result[0].get('custom_cover')


	def get_deck_by_uuid(self, uuid):

		try:

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute("SELECT * FROM decks WHERE UUID = '" + uuid + "';")
			result = {}
			result = dictCursor.fetchall()

			return result[0]

		except Exception as exception:
			print(exception)
			return False


	def get_last_card(self, deck, user):

		try:

			queue = "SELECT * FROM cards WHERE deck = '" + deck + "' AND user = '" + user + "' AND queue = 1;"

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute(queue)

			result = {}
			result = dictCursor.fetchall()

			return result[0]

		except Exception as exception:
			print(exception)
			return False

	
	def get_card_by_uuid(self, uuid):

		try:

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute("SELECT * FROM cards WHERE UUID = '" + uuid + "';")
			result = {}
			result = dictCursor.fetchall()

			return result[0]

		except Exception as exception:
			print(exception)
			return False


	def get_cards_number(self, deck, user):

		try:

			query = "SELECT * FROM cards WHERE deck = '" + deck + "' AND user = '" + user + "';"

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute(query)

			result = {}
			result = dictCursor.fetchall()

			return dictCursor.rowcount

		except Exception as exception:
			print(exception)
			return False


	def get_card_pic_name(self, card_uuid, request):

		try:

			query = "SELECT * FROM cards WHERE UUID = '" + card_uuid + "';"

			dictCursor = self.db.cursor(dictionary=True)
			dictCursor.execute(query)

			result = {}
			result = dictCursor.fetchall()

			return result[0].get(request)

		except Exception as exception:
			print(exception)
			return False	


	def add_card(self, data):

		try:

			deck = self.get_deck_by_uuid(data.get(b'deck'))

			f_pic1_path = self.get_deck_cover_new_name(data.get(b'imginput_f1_original_name'), data.get(b'imginput_f1_name'))
			f_pic2_path = self.get_deck_cover_new_name(data.get(b'imginput_f2_original_name'), data.get(b'imginput_f2_name'))
			b_pic1_path = self.get_deck_cover_new_name(data.get(b'imginput_b1_original_name'), data.get(b'imginput_b1_name')) 
			b_pic2_path = self.get_deck_cover_new_name(data.get(b'imginput_b2_original_name'), data.get(b'imginput_b2_name'))

			query = "UPDATE cards SET queue = queue+1 WHERE user = '" + data.get(b'user') + "' AND deck = '" + deck.get('name') + "';"
			cursor = self.db.cursor()
			cursor.execute(query)

			query = "INSERT INTO cards (UUID, deck, user, queue, f_pic1_path, f_pic2_path, f_text,b_pic1_path, b_pic2_path, b_text) VALUES ('" + str(uuid.uuid4()) +"', '" + deck.get('name') + "', '" + data.get(b'user') + "', " + str(1) + ", '" + f_pic1_path + "', '" + f_pic2_path + "', '" + data.get(b'text_f') + "', '" + b_pic1_path + "', '" + b_pic2_path + "', '" + data.get(b'text_b') + "')"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			thisdict = {
				"f_pic1_path": f_pic1_path,
				"f_pic2_path": f_pic2_path,
				"b_pic1_path": b_pic1_path,
				"b_pic2_path": b_pic2_path
			}

			return thisdict

		except Exception as exception:
			print(exception)
			return False


	def get_deck_cover_new_name(self, original_pic_name, uuid_for_pic = ''):
		if (original_pic_name is None):
			return ""
		else:
			filename, file_extension = os.path.splitext(original_pic_name)
			uuid_for_pic += file_extension
			return uuid_for_pic
			

	def delete_deck(self, deck_name, deck_user):

		try:

			query = "DELETE FROM decks WHERE name = '" + deck_name + "' AND user = '" + deck_user + "';"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			query = "DELETE FROM cards WHERE deck = '" + deck_name + "' AND user = '" + deck_user + "';"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()
			return True

		except Exception as exception:
			print(exception)
			return False


	def delete_card(self, card_id):

		try:

			dictCursor = self.db.cursor(dictionary=True)
			query = "SELECT * FROM cards WHERE UUID = '" + card_id + "'"
			dictCursor.execute(query)
			result = {}
			result = dictCursor.fetchall()

			return_data = {
				"deck_uuid": result[0].get('UUID'),
				"deck_name": result[0].get('deck'),
				"user": result[0].get('user'),
				"f_pic1_name": result[0].get('f_pic1_path'),
				"f_pic2_name": result[0].get('f_pic2_path'),
				"b_pic1_name": result[0].get('b_pic1_path'),
				"b_pic2_name": result[0].get('b_pic2_path')
			}

			query = "UPDATE cards SET queue = queue-1 WHERE user = '" + result[0].get('user') + "' AND deck = '" + result[0].get('deck') + "' AND queue > " + str(result[0].get('queue')) + ";"
			cursor = self.db.cursor()
			cursor.execute(query)

			query = "DELETE FROM cards WHERE UUID = '" + card_id + "'"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return return_data

		except Exception as exception:
			print(exception)
			return False


	def update_deck_activity(self, deck_uuid):

		try:

			query = "UPDATE decks SET last_activity = '" + str(time.time()) + "' WHERE UUID = '" + deck_uuid + "';"
			
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False


	def move_card(self, new_queue, deck_name, user):

		try:

			query = "UPDATE cards SET queue = queue-1 WHERE queue <= " + str(new_queue) + " AND deck = '" + deck_name + "' AND user = '" + user + "';"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			query = "UPDATE cards SET queue = " + str(new_queue) + " WHERE queue = 0 AND deck = '" + deck_name + "' AND user = '" + user + "';"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False




	def edit_deck(self, data, old_deck_name):

		try:

			new_deck_name = data.get(b'name')

			if (new_deck_name == old_deck_name):
				new_deck_name = ''

			if (data.get(b'custom_cover') == 'false'):
				custom_cover = '0'
			elif (data.get(b'custom_cover') == 'true'): 
				custom_cover = '1'
			else:
				custom_cover = None
			name_inputted = False

			query = "UPDATE decks SET "
			if (new_deck_name != ''):
				query += "name = '"
				query += new_deck_name
				query += "'"
				name_inputted = True
				query_cards = "UPDATE cards SET deck = '" + new_deck_name + "' WHERE deck = '" + old_deck_name + "' AND user = '" + data.get(b'user') + "';"
				cursor = self.db.cursor()
				cursor.execute(query_cards)
				self.db.commit()

			if (custom_cover is not None):
				if (name_inputted): query += ", "
				query += "custom_cover = '"
				query += custom_cover
				query += "'"

			query += " WHERE UUID = '" + data.get(b'deck_uuid') + "';"
			cursor = self.db.cursor()
			cursor.execute(query)
			self.db.commit()

			return True

		except Exception as exception:
			print(exception)
			return False


	def edit_user(self, data):

		try:

			dictCursor = self.db.cursor(dictionary=True)
			query_select = "SELECT * FROM users WHERE name = '" + data.get(b'old_user_name') + "';"
			dictCursor.execute(query_select)
			result = {}
			result = dictCursor.fetchall()

			full_user = result[0]

			old_profile_pic_name = result[0].get('profile_pic_path')

			new_user_name = data.get(b'name')
			old_user_name = data.get(b'old_user_name')

			if (new_user_name == old_user_name):
				new_user_name = ''

			name_inputted = False
			password_inputted = False

			query_user = "UPDATE users SET "

			if (new_user_name != ''):
				query_user += "name = '"
				query_user += new_user_name
				query_user += "'"
				name_inputted = True
				query_decks = "UPDATE decks SET user = '" + new_user_name + "' WHERE user = '" + old_user_name + "';"
				cursor = self.db.cursor()
				cursor.execute(query_decks)
				self.db.commit()

				query_cards = "UPDATE cards SET user = '" + new_user_name + "' WHERE user = '" + old_user_name + "';"
				cursor = self.db.cursor()
				cursor.execute(query_cards)
				self.db.commit()

			password = data.get(b'password')

			if (password != ''):
				password_inputted = True
				if (name_inputted): query_user += ", "
				query_user += "password = '"
				query_user += password
				query_user += "'"

			custom_profile_pic = data.get(b'profile_pic_path')

			if (custom_profile_pic is not None):
				if (name_inputted or password_inputted): query_user += ", "
				query_user += "profile_pic_path = '"
				query_user += custom_profile_pic
				query_user += "'"

			query_user += " WHERE name = '" + old_user_name + "';"
			cursor = self.db.cursor()
			cursor.execute(query_user)
			self.db.commit()

			return full_user

		except Exception as exception:
			print(exception)
			return False