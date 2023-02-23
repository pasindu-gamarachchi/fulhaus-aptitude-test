import os

from fulhaus_app import app
from flask import request
from werkzeug.utils import secure_filename
import logging
from fulhaus_app.app_helper.app_helper import AppHelper
from fulhaus_app.classifier_nn.classifier_NN import classifierNN

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
                saved_file = helper.save_image(image_file, filename, False)
            else:
                saved_file = helper.save_image(image_file, image_file.filename)

            furnitureClassifier = classifierNN()
            saved_img = furnitureClassifier.read_image(saved_file)
            furniture_type = furnitureClassifier.predict_furniture(saved_img)
            result = f"That is a {furniture_type}"
        except Exception as err:
            logging.error(f"{err} getting results.")
            return {"is_error": True}, 400

    return {"Message": result}, 200
