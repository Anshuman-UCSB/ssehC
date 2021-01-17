from gameManager import gameManager, toJson
from game import Game
from piece import Piece
from coord import Coord
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = False
api = Api(app)

import pyrebase

config = {
  "apiKey": "AIzaSyAERXuIBK-DbKa3ORHrABp5NwjCLHPIBkE",
  "authDomain": "ssehc-1.firebaseapp.com",
  "databaseURL": "https://ssehc-1-default-rtdb.firebaseio.com/",
  "storageBucket": "ssehc-1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
# print(db.child("Games").get().val()["ping"])

manager = gameManager()

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
            return {"error": "already started"}
        else:
            manager.addGame(game_id)
            payload = {game_id:toJson(manager.games[game_id])}
            db.child("Games").set(payload)
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
            except Exception as e:
                return {"error": "error at moving, message included.", "message":e}
        if(headers["action"] == "getMoves"):
            fromC = Coord(headers["x1"],headers["y1"])
            valids = g.getValidMoves(fromC)
            print([str(c) for c in valids])
            out = {"coords":[]}
            # ind = 0
            for c in valids:
                out["coords"].append({"x":c.x, "y":c.y})
                # ind+=1
            return out
        g.debugPrint()
        payload = {game_id:toJson(g)}
        db.child("Games").set(payload)
        
        print(headers)


@app.route('/alive', methods=['GET'])
def working():
    return "Working!"

@app.route('/firebaseTest', methods=['GET'])
def testDb():
    return db.get().val()
    
api.add_resource(apiHandler, '/')



if __name__ == "__main__":
    app.run(host = "0.0.0.0")