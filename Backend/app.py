from gameManager import gameManager, toJson
from game import Game
from random import choice
from piece import Piece
from coord import Coord
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = False
api = Api(app)

import pyrebase

config = {
  "apiKey": "Xv6EiKf2UxUcnJ8fevAg1Igdl4oNjdLseOpJgDVP",
  "authDomain": "ssehc-1.firebaseapp.com",
  "databaseURL": "https://ssehc-1-default-rtdb.firebaseio.com/",
  "storageBucket": "ssehc-1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
# print(db.child("Games").get().val()["ping"])

manager = gameManager()

WORDS = open("wordlist.txt").read().splitlines()

class apiHandler(Resource):

    def get(self):
        game_id = request.headers["game"]
        if(game_id not in manager.games.keys()):
            return {"error": "game not found"}
        else:
            return toJson(manager.games[game_id])

    def put(self):
        game_id = request.headers["game"]
        print("ID: ",game_id)
        if(game_id in manager.games.keys()):
            try:
                print(request.headers)
                if request.headers["override"] != "1":
                    print("Override not allowed")
                    raise Exception("No override")
                manager.games[game_id] = Game()
                # payload = {game_id:toJson(manager.games[game_id])}
                db.child("Games").child(game_id).set(toJson(manager.games[game_id]))
                return {"done":True, "overwritten":"true"}
            except:
                return {"error": "already started"}
        else:
            manager.addGame(game_id)
            db.child("Games").child(game_id).set(toJson(manager.games[game_id]))
            return {"done":True}

    def post(self):
        headers = request.headers
        game_id = headers["game"]
        if(game_id not in manager.games.keys()):
            return {"error": "game not in game manager"}
        g = manager.getGame(game_id)
        if(headers["action"] == "move"):
            fromC = Coord(headers["x1"],headers["y1"])
            toC = Coord(headers["x2"],headers["y2"])
            try:
                g.makeMove(fromC, toC)
                db.child("Games").child(game_id).set(toJson(manager.games[game_id]))
                return {"done":True}
            except Exception as e:
                return {"error": "error at moving, message included.", "message":str(e)}
        if(headers["action"] == "getMoves"):
            fromC = Coord(headers["x1"],headers["y1"])
            try:
                valids = g.getValidMoves(fromC)
            except Exception as e:
                return {"error":str(e)}
            print([str(c) for c in valids])
            out = {"coords":[]}
            # ind = 0
            for c in valids:
                out["coords"].append({"x":c.x, "y":c.y})
                # ind+=1
            return out
        g.debugPrint()
        # payload = {game_id:toJson(g)}
        # db.child("Games").set(payload)
        


    def delete(self):
        headers = request.headers
        game_id = headers["game"]

        db.child("Games").child(game_id).update({})

@app.route('/alive', methods=['GET'])
def working():
    return "Working!"

@app.route('/firebaseTest', methods=['GET'])
def testDb():
    return db.get().val()
    
@app.route('/generateId', methods=['GET'])
def makeID():
    out = ""
    delim = ""
    for _ in range(4):
        out+=delim+choice(WORDS)
        delim = "-"
    return out

api.add_resource(apiHandler, '/')


if __name__ == "__main__":
    app.run(host = "0.0.0.0",ssl_context='adhoc')