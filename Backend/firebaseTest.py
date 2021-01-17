import pyrebase

config = {
  "apiKey": "AIzaSyAERXuIBK-DbKa3ORHrABp5NwjCLHPIBkE",
  "authDomain": "ssehc-1.firebaseapp.com",
  "databaseURL": "https://ssehc-1-default-rtdb.firebaseio.com/",
  "storageBucket": "ssehc-1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

print(db.get().val())
value = {"test":"output"}
db.child("games").set(value)