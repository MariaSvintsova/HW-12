import logging

from flask import Flask, request, render_template, send_from_directory
from functions import *
from main.views import messages_blueprint
from loader.views import new_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(messages_blueprint)
app.register_blueprint(new_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)



@app.route("/uploads/<path:path>")
def static_dir(path):
    """gives permission for using directory uploads"""
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run()

