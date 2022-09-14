import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import django
django.setup()
from pytz import timezone
# from recommend_app.models import Post
# from recommend_app.views import get_client_ip
from datetime import date,datetime,timedelta
import pandas as pd
import pickle
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parent.parent
print((BASE_PATH/'.static_root/data'))
pd.read_json(BASE_PATH/'.static_root/data/texts/song_meta_light_str.json')
tag_df = pd.read_json(BASE_PATH/'.static_root/data/final_sesac_df.json')
# test = Post.objects.filter(postdate__gte=date.today()-timedelta(days=30)).values().all().order_by('-postdate')
# KST = timezone('Asia/Seoul')
# format_data = "%Y-%m-%d %H:%M:%S.%f%z"
# _list = []
# for i in test:
#     time = i['postdate'].astimezone(KST)
#     time = datetime.strptime(str(time), format_data)
#
#     tags = i['tag'][2:-2].replace("'",'').replace(",",'').split()
#     tags = ' '.join(tags)
#     _list.append(i['ip'])
#     _list.append(tags)
#     _list.append(i['satisfaction'])
#     _list.append(time.strftime("%Y년 %m월 %d일 %H시 %S분"))
#     print(_list)
# test = Post.objects.filter(postdate__gte=date.today()-timedelta(days=30)).values('tag').all()
# tag_list = [i['tag'][2:-2].replace("'",'').replace(",",'').split() for i in test]
# tag_list = sum(tag_list,[])
# frequency_d = collections.Counter(tag_list)
# print(frequency_d)
# font_path= 'C:/Windows/Fonts/HANBatang.ttf'
# wc = WordCloud(width=1000, font_path= font_path, height=600, background_color="white", random_state=0)
# wc.generate_from_frequencies(frequency_d)
# wc.to_file('C:/Users/qkrtj/Desktop/recomend_song/recommend_app/static/data/image/wordcloud.png')
# with open('C:/Users/user/Desktop/recomend_song_final/recommend_app/static/data/random_tags.pkl','rb') as f:
#     pk_list = pickle.load(f)
# from random import randrange
# for i in pk_list:
#     if len(i) == 0:
#         continue 
#     Post.objects.create(ip='127.0.0.1',tag=i, satisfaction=randrange(0,2))

