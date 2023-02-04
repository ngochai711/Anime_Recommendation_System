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
        
        
def find_similar_users(userid, n=10, return_dist=False, neg=False):
    try:
        index = userid
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
            if isinstance(userid, int):
                decoded_id = modelvar.user_encoded2user.get(str(close))
                if decoded_id != userid:
                    result_arr.append({"user": decoded_id, "similarity": similarity})
        return [True, result_arr]
    
    except Exception as e:
        return [False, str(e)]
    
    
def get_user_preferences(userid):
    animes_watched_by_user = modelvar.rating_df[modelvar.rating_df.user_id==userid]
    user_rating_percentile = np.percentile(animes_watched_by_user.rating, 75)
    animes_watched_by_user = animes_watched_by_user[animes_watched_by_user.rating >= user_rating_percentile]
    top_animes_user = (
        animes_watched_by_user.sort_values(by="rating", ascending=False)#.head(10)
        .anime_id.values
    )
    return top_animes_user


def get_recommended_animes(userid, n=10):
    anime_list = []
    user_pref = []
    similar_users = []
    
    user_pref = get_user_preferences(userid)
    
    output = find_similar_users(userid, n=5, neg=False)
    if output[0]: similar_users = output[1]
    
    for user_id in similar_users:
        pref_list = get_user_preferences(int(user_id), verbose=0)
        pref_list = pref_list[~ pref_list.isin(user_pref)]
        anime_list.append(pref_list)
        
    return anime_list
        
    # anime_list = pd.DataFrame(anime_list)
    # sorted_list = pd.DataFrame(pd.Series(anime_list.values.ravel()).value_counts()).head(n)
    
    # for i, anime_name in enumerate(sorted_list.index):        
    #     n_user_pref = sorted_list[sorted_list.index == anime_name].values[0][0]
    #     if isinstance(anime_name, str):
    #         try:
    #             anime_id = frame.anime_id.values[0]
    #             genre = frame.Genres.values[0]
    #             sypnopsis = getSynopsis(int(anime_id))
    #             recommended_animes.append({#"anime_id": anime_id ,
    #                                         "n": n_user_pref,
    #                                         "anime_name": anime_name, 
    #                                         "Genres": genre, 
    #                                         "sypnopsis": sypnopsis})
    #         except:
    #             pass
    
    # return pd.DataFrame(recommended_animes)