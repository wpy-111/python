"""
    电影推荐
    1.整理用户与用户的相似度矩阵
    2.获取当前用户的相似用户列表，排序
    3.观察每个相似用户都看过什么电影，把那些当前用户没看过的电影，排序，组成推荐列表
"""
import json
import numpy as np
with open('ratings.json','r') as f:
    ratings = json.loads(f.read())
users = list(ratings.keys())
#双层for循环遍历用户数据，计算每个用户之间的相似度，并构建相似度矩阵
scmat = []
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        #计算user1和user2的相似度，找到两个人都看过的电影，计算欧式距离得分
        for movie in ratings[user1].keys():
            if movie in ratings[user2].keys():
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        vct1,vct2=[],[]
        for mov in movies:
            vct1.append(ratings[user1][mov])
            vct2.append(ratings[user2][mov])
        #欧式距离得分
        vct1,vct2 = np.array(vct1),np.array(vct2)
        # score = 1 / (1 + np.sqrt(((vct1-vct2)**2).sum()))
        #corrcoef返回相关矩阵  corrcoef(x，y)[0,1]
        score = np.corrcoef(vct1,vct2)[0,1]
        scrow.append(score)
    scmat.append(scrow)

ary = np.round(scmat,3)
users = np.array(users)
#召回推荐电影列表
#找到每个用户的相似用户列表（保留正相关的用户）,针对每个用户的相似度得分列表
scmat = np.array(scmat)
for i,user in enumerate(users):
    #获取当前用户user的相似用户列表，以及针对每个相似用户的得分列表
    sorted_index = np.argsort(scmat[i])[::-1]
    sorted_index = sorted_index[sorted_index!=i]
    sorted_score = scmat[i][sorted_index]
    sorted_users = users[sorted_index]
    sim_users = sorted_users[sorted_score>0]
    sim_score = sorted_score[sorted_score>0]
    #遍历每个相似用户，看一下相似用户看过的电影，而当前用户没有看过的电影，加入推荐字典
    movies = {}
    for sim_user in sim_users:
        for movie,score in ratings[sim_user].items():
            if movie not in ratings[user].keys():
                if movie not in movies.keys():
                    movies[movie] = [score]
                movies[movie].append(score)
    #进行排序操作，按照每部电影的平均分对字典进行排序
    print(user)
    movie_list = sorted(movies.items(), key=lambda x: np.average(x[1]), reverse=True)
    print(movie_list)





