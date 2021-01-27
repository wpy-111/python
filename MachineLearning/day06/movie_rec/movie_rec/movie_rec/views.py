from django.http import HttpResponse
import json
from ML import movie_recommender
import sys

def common(request, id):
    try:
        print('----------------start ItemBasedCFModel()', sys.path)
        ibcf_model = movie_recommender.ItemBasedCFModel()
        print('----------------end ItemBasedCFModel()')
        movies_id1 = ibcf_model.recommend_by_userid(id)
        print('----------------2', movies_id1)
        status = 200
        data = []
        for i in range(len(movies_id1)):
            data.append(int(movies_id1[i]))
        msg = "null"
        d = dict(status=status, data=data, msg=msg)
        r = json.dumps(d)
        return HttpResponse(r)
    except Exception as e:
        print(e.args)
        status = 201
        data = 'null'
        msg = '请输入合法ID'
        d = dict(status=status, data=data, msg=msg)
        r = json.dumps(d)
        return HttpResponse(r)

def persona(request, id):
    try:
        movies_rec = movie_recommender.PersonaRecommendModel()
        movies_id = movies_rec.recommend_by_userid(id)
        status = 200
        data = []
        for i in range(len(movies_id)):
            data.append(int(movies_id[i]))
        msg = "null"
        d = dict(status=status, data=data, msg=msg)
        r = json.dumps(d)
        return HttpResponse(r)
    except:
        status = 201
        data = 'null'
        msg = '请输入合法ID'
        d = dict(status=status, data=data, msg=msg)
        r = json.dumps(d)
        return HttpResponse(r)
