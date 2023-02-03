import os, json
import numpy as np, pandas as pd
import components.model_variables as modelvar
from collections import defaultdict


def find_similar_animes(id, n=10, return_dist=False, neg=False):
    try:
        encoded_index = modelvar.anime2anime_encoded.get(str(id))
        weights = modelvar.anime_weights
        dists = np.dot(weights, weights[encoded_index])
        sorted_dists = np.argsort(dists)
        n = n + 1
        if neg:
            closest = sorted_dists[:n]
        else:
            closest = sorted_dists[-n:]

        if return_dist:
            return [True, dists, closest]
        
        result_arr = []
        for close in closest:
            decoded_id = modelvar.anime_encoded2anime.get(str(close))
            similarity = dists[close]
            result_arr.append({"id": decoded_id, "similarity": str(similarity)})
            
        return [True, result_arr]

    except Exception as e:
        print[False, str(e)]
        
        
def find_similar_users(item_input, n=10, return_dist=False, neg=False):
    try:
        index = item_input
        encoded_index = modelvar.user2user_encoded.get(str(index))
        weights = modelvar.user_weights
    
        dists = np.dot(weights, weights[encoded_index])
        sorted_dists = np.argsort(dists)
        n = n + 1
        
        if neg: closest = sorted_dists[:n]
        else: closest = sorted_dists[-n:]
        if return_dist:
            return [True, dists, closest]
        
        result_arr = []
        for close in closest:
            similarity = dists[close]
            if isinstance(item_input, int):
                decoded_id = modelvar.user_encoded2user.get(str(close))
                result_arr.append({"user": decoded_id, "similarity": similarity})
        
        return [True, result_arr]
    
    except Exception as e:
        return [False, str(e)]
    
    
# def get_user_preferences(user_id, plot=False, verbose=0):
#     animes_watched_by_user = rating_df[rating_df.user_id==user_id]
#     user_rating_percentile = np.percentile(animes_watched_by_user.rating, 75)
#     animes_watched_by_user = animes_watched_by_user[animes_watched_by_user.rating >= user_rating_percentile]
#     top_animes_user = (
#         animes_watched_by_user.sort_values(by="rating", ascending=False)#.head(10)
#         .anime_id.values
#     )
    
#     anime_df_rows = df[df["anime_id"].isin(top_animes_user)]
#     anime_df_rows = anime_df_rows[["eng_version", "Genres"]]
    
#     if verbose != 0:
#         print("> User #{} has rated {} movies (avg. rating = {:.1f})".format(
#           user_id, len(animes_watched_by_user),
#           animes_watched_by_user['rating'].mean(),
#         ))
    
#         print('> preferred genres')
          
#     return anime_df_rows#.eng_version.values