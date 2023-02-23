import os
import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import logging

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout


class classifierNN:

    def __init__(self):
        model_path = os.getenv("MODEL_PATH", "fulhaus_app/static/furniture_classifier.h5")
        self.model = load_model(model_path, compile=False)

    def read_image(self, image_path):
        """
        Read image from file, and return resized image
        :param image_path:
        :return:
        """
        newimg = cv2.imread(image_path)
        newimg = tf.image.resize(newimg, (256, 256))
        return newimg

    def predict_furniture(self, img):
        """
        Predict furniture type
        :param img:
        :return:
        """
        yhat = self.model.predict(np.expand_dims(img / 255, 0))
        logging.info(f"Result : {yhat}")
        furniture_typ = np.argmax(yhat[0])
        logging.info(f"Furniture type : {furniture_typ}")
        furniture_typ = self.__map_results(furniture_typ)
        return furniture_typ

    def __map_results(self, yhat):
        """
        Map Results to original labels
        :param results:
        :return:
        """
        LABEL_MAPP =  {0:"Bed", 1:"Chair", 2:"Sofa"}
        res = LABEL_MAPP.get(yhat)
        return res

    def build_model(self):
        """
        Build  the Neural Network from the Training Data
        :return:
        """
        data_dir = os.getenv("DATA_DIR", "fulhaus_app/data_set")
        data = tf.keras.utils.image_dataset_from_directory(data_dir, batch_size=15, label_mode='categorical')
        data = data.map(lambda x, y: (x / 255, y))

        train_size = int(len(data) * 0.7)
        val_size = int(len(data) * 0.2)
        test_size = len(data) - train_size - val_size

        train_set = data.take(train_size)
        val_set = data.take(val_size)
        test_set = data.take(test_size)
        image_model = Sequential()
        image_model.add(Conv2D(16, (3, 3), 1, activation='relu', input_shape=(256, 256, 3)))
        image_model.add(MaxPooling2D())
        image_model.add(Conv2D(32, (3, 3), 1, activation='relu'))
        image_model.add(MaxPooling2D())
        image_model.add(Conv2D(16, (3, 3), 1, activation='relu'))
        image_model.add(MaxPooling2D())
        image_model.add(Flatten())
        image_model.add(Dense(256, activation='relu'))
        image_model.add(Dense(3, activation='softmax'))
        image_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        tb_callback = tf.keras.callbacks.TensorBoard(log_dir='fulhaus_app/model_training_logs')
        image_model.fit(train_set, epochs=20, validation_data=val_set, callbacks=[tb_callback])
        image_model.save(os.path.join('models','furniture_classifier.h5'))

