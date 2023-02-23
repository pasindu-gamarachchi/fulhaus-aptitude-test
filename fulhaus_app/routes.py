import os

from fulhaus_app import app
from flask import request
from werkzeug.utils import secure_filename
import logging
from fulhaus_app.app_helper.app_helper import AppHelper


@app.route("/")
def home():
    return {"Status": "Started"}, 200


@app.route("/get_results", methods=["POST"])
def get_results():
    logging.info(f"Get results called")
    helper = AppHelper()
    if request.method == "POST":
        try:
            image_file = request.files['file']
            if image_file.filename == "":
                filename = helper.gen_filename()
                helper.save_image(image_file, filename, False)
            else:
                helper.save_image(image_file, image_file.filename)
        except Exception as err:
            logging.error(f"{err} getting results.")
            return {"is_error": True}, 400

    return {}, 200
