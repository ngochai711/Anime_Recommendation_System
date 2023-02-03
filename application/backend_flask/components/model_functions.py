import os, json
import numpy as np, pandas as pd
import components.model_variables as modelvar


def find_similar_animes(id, n=10, return_dist=False, neg=False):
    try:
        encoded_index = modelvar.anime2anime_encoded.get(str(id))
        weights = modelvar.anime_weights
        dists = np.dot(weights, weights[encoded_index])
        sorted_dists = np.argsort(dists)
        n = n + 1
        if neg: closest = sorted_dists[:n]
        else: closest = sorted_dists[-n:]
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
        # item_input ???
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
    
    
def get_user_preferences(ratings_dict):
    ratings = []
    for item in ratings_dict: ratings.append(item['Point'])
    user_rating_percentile = np.percentile(ratings, 75)
    result = []
    for item in ratings_dict:
        if item['Point'] >= user_rating_percentile: result.append(item['ID_Anime'])
    return result


# def get_recommended_animes(similar_users, n=10):
#     recommended_animes = []
#     anime_list = []
    
#     for user_id in similar_users.similar_users.values:
#         pref_list = get_user_preferences(int(user_id), verbose=0)
#         pref_list = pref_list[~ pref_list.eng_version.isin(user_pref.eng_version.values)]
#         anime_list.append(pref_list.eng_version.values)
        
#     anime_list = pd.DataFrame(anime_list)
#     sorted_list = pd.DataFrame(pd.Series(anime_list.values.ravel()).value_counts()).head(n)
    
#     for i, anime_name in enumerate(sorted_list.index):        
#         n_user_pref = sorted_list[sorted_list.index == anime_name].values[0][0]
#         if isinstance(anime_name, str):
#             try:
#                 frame = getAnimeFrame(anime_name)
#                 anime_id = frame.anime_id.values[0]
#                 genre = frame.Genres.values[0]
#                 sypnopsis = getSynopsis(int(anime_id))
#                 recommended_animes.append({#"anime_id": anime_id ,
#                                             "n": n_user_pref,
#                                             "anime_name": anime_name, 
#                                             "Genres": genre, 
#                                             "sypnopsis": sypnopsis})
#             except:
#                 pass
    
#     return pd.DataFrame(recommended_animes)