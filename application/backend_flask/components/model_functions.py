import os, json
import numpy as np, pandas as pd
from components.config import MODEL_PATH
import components.model_variables as modelvar


def find_similar_animes(id, n=10, return_dist=False, neg=False):
    try:
        encoded_index = modelvar.anime2anime_encoded.get(id)
        weights = modelvar.anime_weights
        dists = np.dot(weights, weights[encoded_index])
        sorted_dists = np.argsort(dists)
        n = n + 1
        if neg:
            closest = sorted_dists[:n]
        else:
            closest = sorted_dists[-n:]

        if return_dist:
            return dists, closest

        result_arr = []
        for close in closest:
            decoded_id = modelvar.anime_encoded2anime.get(close)
            similarity = dists[close]
            result_arr.append({"id": decoded_id, "similarity": similarity})
            
        return [True, result_arr]

    except Exception as e:
        print[False, str(e)]
        

