import uuid
import os
import logging


class AppHelper:

    def gen_filename(self):
        return uuid.uuid4().replace("-", "_")

    def save_image(self, image, filename, has_ext=True):
        """
        Save image to folder or cloud storage TODO
        :param image_file:
        :return:
        """
        if not has_ext:
            default_ext = os.getenv("DEFAULT_IMAGE_EXT", ".png")
            filename = f"{filename}{default_ext}"
        logging.info(f"OS path : {os.path}")
        image.save(f'fulhaus_app/images/{filename}')
        logging.info(f"Saved {filename}")
        logging.info(f"{os.listdir('/fulhaus_app/images/')}")
