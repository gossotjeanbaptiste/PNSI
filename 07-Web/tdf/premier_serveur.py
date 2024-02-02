from flask import Flask
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

app = Flask(__name__)

@app.route("/")
def coucou():
    return "<h1>Salut ! yhvhbdlkgmkbkjgLe serveur fonctionne !!</h1>"
