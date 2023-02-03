from keras.models import load_model, model_from_json
import json, os, numpy, pandas
from components.config import MODEL_PATH, DATASET_PATH

def extract_weights(name, model):
    weight_layer = model.get_layer(name)
    weights = weight_layer.get_weights()[0]
    weights = weights / numpy.linalg.norm(weights,axis=1).reshape((-1,1))
    return weights

def open_file(name):
    with open(os.path.join(MODEL_PATH, name)) as f:
        return f.read()

loaded_model_json = open_file("model.json")
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(os.path.join(MODEL_PATH, "anime_model.h5"))
# loaded_model = load_model(os.path.join(MODEL_PATH, "anime_model.h5"))

anime_weights = extract_weights('anime_embedding', loaded_model)
user_weights = extract_weights('user_embedding', loaded_model)

anime_encoded2anime = json.loads(open_file("anime_encoded2anime.json"))
anime2anime_encoded = json.loads(open_file("anime2anime_encoded.json"))
user_encoded2user = json.loads(open_file("user_encoded2user.json"))
user2user_encoded = json.loads(open_file("user2user_encoded.json"))

df_anime = pandas.read_csv(os.path.join(DATASET_PATH, "anime.csv"))