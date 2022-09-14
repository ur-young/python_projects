from http.client import HTTPResponse

import sys
print(sys.executable)
import os
from pathlib import Path
BASE_PATH = Path(__file__).resolve().parent.parent


from django.shortcuts import render,HttpResponse,redirect,render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from gensim.models import Word2Vec
from pytz import timezone
from recommend_app.models import Post, Board 
from datetime import date,datetime,timedelta
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt


num = 0
keyword = []

light_song = pd.read_json(BASE_PATH/'.static_root/data/texts/song_meta_light_str.json')
topics = [{'id':1,'title': '만든 사람','body' : '윤혜영, 장윤식, 조경희, 김빈'},
{'id':2,'title':'이 앱에 대하여','body':'.. 쏼라 쏼라'},
{'id':3,'title':'Thanks TO','body':'부모님'},
{'id':4,'title':'show Data','body':'사용자님이 주신 소중한 데이터들'},
{'id':5,'title':'게시판','body':'게시글쓰기'}]
keyword_model = Word2Vec().wv.load(str(BASE_PATH/'.static_root/data/keyword_final'))
play_list_model = Word2Vec().wv.load(str(BASE_PATH/'.static_root/data/word2vec_playlist'))

def index(request):
    article = '''
        <h2>곡 추천 어플리케이션</h2>
    사용자에게 곡을 추천을 해주는 앱입니다.
    '''
    return render(request,'recommend_app/index.html',{'topics':topics})

def read(request,id):
    global topics
    article = ''
    topic = topics[int(id)-1]
    if id =='1':
        return render(request,'recommend_app/who_made.html')
    elif id =='2':
        return render(request,'recommend_app/page_info.html')
    elif id =='3':
        return render(request,"recommend_app/thanks_to.html")
    elif id == '4':
        return redirect('/data/')
    elif id == '5':
        data_list = Board.objects.all()
        print(data_list)
        _list = []
        for i in data_list:
            _dict = {"id":i.id,"user_name":i.user_name, "title":i.title,"create_at" : i.create_at}
            _list.append(_dict)
        return render(request,'recommend_app/test.html',{'Board_list' : _list})


@csrf_exempt
def recommend(request):
    print('request.method', request.method)
    if request.method == "GET":
        return render(request,'recommend_app/recommend.html',{'topics':topics})
    elif request.method == "POST":
        global keyword
        global num
        num = request.POST['num']
        keyword = []
        keyword.append(request.POST['genre'])
        keyword.append(request.POST['emotion'])
        keyword.append(request.POST['mood'])
        url = '/show/'
        return redirect(url)

@csrf_exempt
def show(request):
    if request.method == "GET":
        global keyword
        global keyword_model
        global play_list_model
        global tag_df
        global light_song
        global topics
        keyword_similar = keyword_model.most_similar(keyword,topn=len(list(keyword_model.index_to_key)))
        keyword_similar = dict(keyword_similar)
        for i in keyword:
            keyword_similar[i] = 10
        test = make_score_column(keyword_similar,tag_df)
        song_id = test.iloc[0].name
        similar_song = play_list_model.most_similar(str(song_id), topn= int(num))
        song_num = [(int(i[0].strip())) for i in similar_song]
        # article = light_song.loc[song_num][['artist_name_basket','song_name']].reset_index(drop=True).to_html()
        
        # return render(request,"recommend_app/show.html",{'topics':topics,'keyword':keyword,'recommend_data':article})
        recommend_keyword_model = zip(range(1,int(num)+1), light_song.loc[list(test[:int(num)].index)].song_name, light_song.loc[list(test[:int(num)].index)].artist_name_basket)
        recommend_song_model = zip(range(1,int(num)+1), light_song.loc[song_num].song_name, light_song.loc[song_num].artist_name_basket)

        return render(request,"recommend_app/show.html",{'topics':topics,'keyword':keyword,'recommend_song_data':recommend_song_model,'recommend_keyword_data':recommend_keyword_model})
    elif request.method == "POST":
        grade = int(request.POST['grade'])
        Post.objects.create(ip=str(get_client_ip(request)),tag=keyword, satisfaction=grade)
        return redirect('/show/')

def data(request): 
    global topics
    test = Post.objects.filter(postdate__gte=date.today()-timedelta(days=30)).values().all().order_by('-postdate')
    KST = timezone('Asia/Seoul')
    format_data = "%Y-%m-%d %H:%M:%S.%f%z"
    _list = []
    for i in test:
        temp = []
        time = i['postdate'].astimezone(KST)
        time = datetime.strptime(str(time), format_data)

        tags = i['tag'][2:-2].replace("'",'').replace(",",'').split()
        tags = ', '.join(tags)
        temp.append(i['ip'])
        temp.append(tags)
        temp.append(i['satisfaction'])
        temp.append(time.strftime("%Y년 %m월 %d일 %H시 %S분"))
        _list.append(temp)

    #워드클라우드 코드
    test = Post.objects.filter(postdate__gte=date.today() - timedelta(days=30)).values('tag').all()
    tag_list = [i['tag'][2:-2].replace("'", '').replace(",", '').split() for i in test]
    tag_list = sum(tag_list, [])
    frequency_d = collections.Counter(tag_list)
    font_path = BASE_PATH/'.static_root/data/BATANG.TTC'
    wc = WordCloud(width=1000, font_path=str(font_path), height=600, background_color="white", random_state=0)
    wc.generate_from_frequencies(frequency_d)
    wc.to_file(str(BASE_PATH/'.static_root/data/image/wordcloud.png'))
    return render(request,'recommend_app/data.html',{'topics':topics,'datas':_list[:50]})

@csrf_exempt
def write(request):
    print('request.method', request.method)
    if request.method == "GET":



        return render(request,'recommend_app/write.html')
        
    elif request.method == "POST":
        
        title = request.POST['title']
        username = request.POST['username']
        content = request.POST['content']
        pwd = request.POST['pwd']

        Board.objects.create(title=title,contents=content,user_name=username,password=pwd)

        url = '/read/5/'

        return redirect(url)


def read_post(request,id):
    data = Board.objects.get(id=id)
    
    return render(request,'recommend_app/show_board.html',{'data': data})


















def make_score_new(_dict,_list):
  temp = []
  for i in _list:
      temp.append(_dict[i])
  try:
    score = sum(temp)/(len(temp))
  except:
    score = 0
  return score

def make_score_column(_dict,df):
  df['score'] = df.final_tags.apply(lambda x : make_score_new(_dict,x))
  sort_df = df.sort_values('score',ascending=False)
  return sort_df

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip