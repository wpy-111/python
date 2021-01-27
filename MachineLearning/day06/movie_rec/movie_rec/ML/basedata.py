"""
当前模块提供电影推荐所有资源数据。
"""
import pandas as pd
import numpy as np
import time
import os

def init_movie_data():
    """加载所有电影数据"""
    data = pd.read_csv(
        'basedata/m_all_info.csv', names=[
            'movie_id', 'title', 'director', 'scriptwriter', 'actors', 'genres',
            'place', 'languages', 'time', 'duration', 'other_names', '_'],
        sep=r',\s*', engine='python', encoding='utf-8')
    return data


def init_rating_data():
    """加载电影评分数据"""
    data = pd.read_csv('basedata/u_score.csv', names=[
        'movie_id', 'user_id', 'rating'], usecols=(0, 1, 2))
    return data


def init_user_item_mat():
    """
    初始化User对Item的评分矩阵。并全局存储。
    """
    # 获取不重复的user_id列表与movie_id列表作为矩阵行索引标签与列索引标签
    unique_movieids = rating_data['movie_id'].unique()
    unique_userids = rating_data['user_id'].unique()
    user_item_mat = pd.DataFrame(
        0, index=unique_userids, columns=unique_movieids)
    # 遍历rating_data中的每一行数据，充实评分矩阵的内容
    for index, row in rating_data.iterrows():
        user_item_mat[row['movie_id']][row['user_id']] = row['rating']
    return user_item_mat


def init_item_item_simmat():
    t1 = time.time() * 1000
    itemids = user_item_mat.columns
    ITEM_ITEM_SIMMAT = pd.DataFrame(0.0, index=itemids, columns=itemids, dtype='f8')
    """
    通过导演、演员、电影类型、语言、时间整理item与item的相似度矩阵
    """
    # 整理用于描述电影的特征向量字段名列表，并存储
    # 不重复的导演
    director_series = movie_data['director']
    directors = []
    for names in director_series.values:
        directors = directors + names.split(' / ')
    unique_directors = pd.Series(directors).unique()
    # 不重复的演员
    actor_series = movie_data['actors']
    actors = []
    for names in actor_series.values:
        actors = actors + names.split(' / ')
    unique_actors = pd.Series(actors).unique()
    # 不重复的电影类型
    genres_series = movie_data['genres']
    genres = []
    for names in genres_series.values:
        genres = genres + names.split(' / ')
    unique_genres = pd.Series(genres).unique()
    # 不重复的语言
    languages_series = movie_data['languages']
    languages = []
    for names in languages_series.values:
        languages = languages + names.split(' / ')
    unique_languages = pd.Series(languages).unique()

    MOVIE_VEC_COLUMNS = pd.unique(np.hstack((unique_directors, unique_actors, unique_genres, unique_languages)))
    for i, itemA in enumerate(itemids):
        vecA = init_vec_by_itemid(itemA, MOVIE_VEC_COLUMNS)
        col = pd.Series(0, index=itemids, dtype='f8')
        for itemB in itemids:
            vecB = init_vec_by_itemid(itemB, MOVIE_VEC_COLUMNS)
            # 计算两个电影向量的欧氏距离
            sim_score = 1 / (1+np.sqrt(((vecA - vecB) ** 2)).sum())
            col.loc[itemB] = sim_score
        ITEM_ITEM_SIMMAT[itemA] = col
        print(i, itemA, itemB)
    ITEM_ITEM_SIMMAT.to_csv('basedata/ITEM_ITEM_SIMMAT.csv')
    return ITEM_ITEM_SIMMAT


def init_vec_by_itemid(movie_id, MOVIE_VEC_COLUMNS):
    """
    返回itemId电影的特征向量
    导演       演员              电影类型         语言
    000001000 0000000101010111 00111011001110  101110
    """
    movie = movie_data[movie_data['movie_id'] == movie_id][:1]
    # 整理用于描述电影的特征向量
    vec = np.zeros(len(MOVIE_VEC_COLUMNS), dtype='f8')
    features = []
    for val in movie.values.ravel():
        features = features + str(val).split(' / ')
    vec[pd.Index(pd.unique(features)).get_indexer(MOVIE_VEC_COLUMNS) >= 0] = 1
    return vec


movie_data = init_movie_data()
rating_data = init_rating_data()
user_item_mat = init_user_item_mat()
ITEM_ITEM_SIMMAT = None
if not os.path.exists('basedata/ITEM_ITEM_SIMMAT.csv'):
    print('train model ITEM_ITEM_SIMMAT')
    ITEM_ITEM_SIMMAT = init_item_item_simmat()
else:
    print('load model ITEM_ITEM_SIMMAT')
    ITEM_ITEM_SIMMAT = pd.read_csv('basedata/ITEM_ITEM_SIMMAT.csv', index_col=0, header=0)
