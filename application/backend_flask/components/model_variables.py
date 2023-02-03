from keras.models import load_model
import json, os, numpy
from components.config import MODEL_PATH

def extract_weights(name, model):
    weight_layer = model.get_layer(name)
    weights = weight_layer.get_weights()[0]
    weights = weights / numpy.linalg.norm(weights,axis=1).reshape((-1,1))
    return weights

def open_file(name):
    with open(os.path.join(MODEL_PATH, name)) as json_file:
        return json.load(json_file)
    

loaded_model = load_model(os.path.join(MODEL_PATH, "anime_model.h5"))
anime_weights = extract_weights('anime_embedding', loaded_model)
user_weights = extract_weights('user_embedding', loaded_model)

anime_encoded2anime = open_file("anime_encoded2anime.json")
anime2anime_encoded = json.load("anime2anime_encoded.json")
user_encoded2user = json.load("user_encoded2user.json")
user2user_encoded = json.load("user2user_encoded.json")