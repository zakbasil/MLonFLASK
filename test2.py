
import numpy as np
import pickle
from sklearn.preprocessing import LabelBinarizer
from keras.preprocessing.image import img_to_array
import cv2

x1 = open("c.pkl","rb")
model = pickle.load(x1)
lbt = pickle.load(open("l.pkl","rb"))
default_image_size = tuple((256,256))


def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None


def predict_disease(image):
    image_array = convert_image_to_array(image)
    image_d4 = np.array([image_array], dtype=np.float16) / 225.0
    result = model.predict(image_d4)
    Class = lbt.inverse_transform(result)[0]
    return(Class)

predict_disease("uploaded_images/02808b3e-ae88-4259-9b2c-f9096db336e4___RS_HL 1827.jpeg")

