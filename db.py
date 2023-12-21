import pymongo
from football_classes import *

client = pymongo.MongoClient('192.168.112.103')
database = client['22304']
games = database['korzhuk-games']
teams = database['korzhuk-teams']


def choose_collection(name: str):
    if name == "teams":
        return teams
    if name != 'games':
        raise Exception("Не существующий документ")
    return games


def add(key: str, value, document: dict) -> None:
    key = key.split(".")
    value = value.replace("\"", "")
    tmp = value
    try:
        tmp = int(value)
    except:
        pass
    value = tmp
    print(value)
    if len(key) == 1:
        document[key[0]] = value
    else:
        if key not in document.keys():
            document[key[0]] = {key[1], value}
        else:
            document[key[0]][key[1]] = value


def save(document: dict, collection) -> dict:
    if len(document) > 0:
        collection.insert_one(document)
    return dict()


def get_documents(collection):
    return collection.find()


def search_document(collection, key, comparison, value):
    try:
        value = int(value)
    except:
        pass

    if comparison == '>':
        query = {key: {'$gt': value}}
    elif comparison == '>=':
        query = {key: {'$gte': value}}
    elif comparison == '=':
        query = {key: {'$eq': value}}
    elif comparison == '<=':
        query = {key: {'$lte': value}}
    elif comparison == '<':
        query = {key: {'$lt': value}}
    elif comparison == '!=':
        query = {key: {'$ne': value}}
    else:
        raise Exception()

    return collection.find(query)
