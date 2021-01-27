import pandas as pd
import numpy as np
from .basedata import user_item_mat
from .basedata import ITEM_ITEM_SIMMAT


# 基于物品的协同过滤推荐算法
class ItemBasedCFModel(object):

    def __init(self):
        pass

    def recommend_by_userid(self, uid):
        """通过用户id，返回推荐列表
        1. 找到用户评分最高的5部电影。
        2. 找到每部电影的10部相似电影。
        3. 为召回电影列表排序。
        """
        itemids = user_item_mat.columns.values
        user_movie_scores = user_item_mat.loc[str(uid)]
        user_favirate_top5_movie_scores = user_movie_scores.sort_values(ascending=False)[:5]
        user_favirate_top5_movieids = user_favirate_top5_movie_scores.index.values
        reco_movies = np.array([]) # 存储每部推荐电影的id
        sort_weights = np.array([]) # 存储每部推荐电影的权重（当前用户对相似电影的评分）
        for i, itemid in enumerate(user_favirate_top5_movieids):
            movie_list = self.sim_items_recall(itemid, 10)
            movie_weight_list = np.full(len(movie_list), user_favirate_top5_movie_scores.iloc[i])
            reco_movies = np.append(reco_movies, movie_list)
            sort_weights = np.append(sort_weights, movie_weight_list)

        # 去除已经看过的电影
        final_reco_movie_list = self.items_sort(reco_movies, sort_weights)
        return final_reco_movie_list

    def sim_items_recall(self, itemid, topN):
        """
        根据ItemId找到最相似topN个电影
        """
        similar_items = ITEM_ITEM_SIMMAT.loc[itemid].sort_values().index
        return similar_items[:topN].values

    def items_sort(self, itemids, weights):
        """
        计算每部电影的推荐度：电影的平均分 * 电影推荐度权重
        itemIds:
        	为当前用户推荐的电影Id列表
        weights:
        	每部推荐的电影的推荐度权重列表
        """
        itemids = np.array(itemids, dtype='f8')
        weights = np.array(weights, dtype='f8')
        reco_coef_list = np.array([], dtype='f8')  # 存储每部电影的推荐度系数
        all_itemids = ITEM_ITEM_SIMMAT.index.values
        for i, itemid in enumerate(itemids):
            index = np.where(all_itemids == itemid)[0]
            reco_coef_list = np.append(
                reco_coef_list,
                ITEM_ITEM_SIMMAT.values[index].mean() * weights[i])
        # 排序所有电影的推荐度
        print(reco_coef_list[reco_coef_list.argsort()[::-1]])
        sorted_movieids = all_itemids[reco_coef_list.argsort()[::-1]]
        return sorted_movieids


class PersonaRecommendModel(object):
    # 用户画像推荐模型

    def recommend_by_userid(self, uid):
        pass
    
    def recommend(self, pensona_tags, i, uid):
        pass


if __name__ == '__main__':
    ibcf_model = ItemBasedCFModel()
    print(ibcf_model.recommend_by_userid(0))