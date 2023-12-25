import pymongo
import json

client = pymongo.MongoClient('192.168.112.103')
database = client['22304']
games = database['korzhuk-games']
teams = database['korzhuk-teams']
#games.drop()
#teams.drop()

def choose_collection(name: str):
    if name == "teams":
        return teams
    if name != 'games':
        print(name)
        raise Exception("╨Э╨╡ ╤Б╤Г╤Й╨╡╤Б╤В╨▓╤Г╤О╤Й╨╕╨╣ ╨┤╨╛╨║╤Г╨╝╨╡╨╜╤В")
    return games


def add(key: str, value: str, document: dict) -> None:
    key = key.split(".")
    tmp = value
    try:
        tmp = int(value)
    except:
        try:
            tmp = json.loads(value)
            print(tmp)
        except:
            pass
    value = tmp
    print(value)
    if len(key) == 1:
        document[key[0]] = value
    else:
        if key[0] not in document.keys():
            document[key[0]] = {key[1]: value}
        else:
            document[key[0]][key[1]] = value


def save(document: dict, collection) -> dict:
    if len(document) > 0:
        collection.insert_one(document)
    return dict()


def get_documents(collection):
    return collection.find()


def search_document(collection: type(teams), key, comparison, value):
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
    print(query)

    return collection.find(query, )


def perform_aggregation(query_text, collection):
    try:

        pipeline = eval(query_text)
        print(pipeline)

        results = collection.aggregate(pipeline)

        return results

    except Exception as e:
        print(f"Ошибка: {str(e)}")


