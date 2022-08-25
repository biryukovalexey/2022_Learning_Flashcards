from fastapi import APIRouter, Body, Depends, Request, HTTPException, Form, FastAPI
from fastapi.responses import JSONResponse
from typing import List, Dict, Any, Optional, Union, AnyStr
import json
from pydantic import BaseModel
import mysql.connector
from api.internal.logic_controller import Request_handler
from api.internal.db_controller import Mysql_handler
from fastapi import File, UploadFile, Request
import shutil
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os


router = APIRouter()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@router.post("/login")
async def login(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.authenticate(data)
    return result


@router.post("/signup")
async def signup(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.add_user(data)
    return result


@router.post("/get_profile_pic")
async def get_profile_picture(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_profile_picture(data)
    return FileResponse(result)


@router.post("/post_profile_pic")
async def post_profile_pic(request: Request, file: UploadFile = File(...)):
    filename, file_extension = os.path.splitext(file.filename)
    file.filename = 'storage/profile_pictures/' + request.headers.get('uuid_name') + '.jpg'
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return True


@router.post("/delete_user")
async def delete_user(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.delete_user(data)
    return True


@router.post("/add_deck")
async def add_deck(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.add_deck(data)
    return result


@router.post("/post_deck_cover")
async def post_deck_cover(request: Request, file: UploadFile = File(...)):
    filename, file_extension = os.path.splitext(file.filename)
    file.filename = 'storage/data/' + request.headers.get('user_name') + '/' + request.headers.get('deck_name') + '/cover.jpg'
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return True


@router.post("/get_all_decks")
async def get_all_decks(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_all_decks(data)
    return result


@router.post("/get_deck_cover")
async def get_deck_cover(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_deck_cover(data)
    return FileResponse(result)


@router.post("/get_queue")
async def get_queue(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_queue(data)
    return result


@router.post("/add_card")
async def add_card_endpoint(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.add_card(data)
    return result


@router.post("/edit_deck")
async def edit_deck(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.edit_deck(data)
    return result


@router.post("/edit_user")
async def edit_deck(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.edit_user(data)
    return result


@router.post("/post_deck_pic")
async def post_deck_cover(request: Request, file: UploadFile = File(...)):
    mysql_handler = Mysql_handler()
    deck = mysql_handler.get_deck_by_uuid(request.headers.get('deck_uuid'))
    file.filename = 'storage/data/' + request.headers.get('user_name') + '/' + deck.get('name') + '/' + request.headers.get('img_pic_name')
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return True


@router.post("/get_all_cards")
async def get_all_cards(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_all_cards(data)
    return result


@router.post("/get_card_pic")
async def get_card_pic(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_card_pic(data)
    return FileResponse(result)


@router.post("/delete_card")
async def get_all_cards(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.delete_card(data)
    return result


@router.post("/delete_deck")
async def delete_deck(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.delete_deck(data)
    return result


@router.post("/update_deck_activity")
async def update_deck_activity(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.update_deck_activity(data)
    return True


@router.post("/get_last_card")
async def get_last_card(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.get_last_card(data)
    return result


@router.post("/copy_example_deck")
async def copy_example_deck(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.copy_example_deck(data)
    return result


@router.post("/move_card")
async def move_card(arbitrary_json: JSONStructure = None):
    data = arbitrary_json
    request_handler = Request_handler()
    result = request_handler.move_card(data)
    return result


@router.post("/check_connection")
async def check_connection():
    return True