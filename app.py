#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request, render_template
from konltk.tokenizer import asp 
import json
from flask_jsonpify import jsonify
from konltk.tokenizer import wordcount
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
@app.route('/success/autospacing/<text>')
def success_autospacing(text):
       q = asp.KltAsp()
       q.dic_init('/usr/local/asp_dic')
       str_ = q.asp(text.encode("utf8"))
       it= json.dumps(str_, ensure_ascii=False, encoding ='utf-8') 
       return it

@app.route('/success/wordcounting/<text>')
def success_wordcounting(text):
       q = wordcount.WordCount()
       str_ = q.wordcount(text.encode('utf8'))
       it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
       return it

@app.route('/success/wordcounting/sort/<text>')
def success_wordcounting_sort(text):
       q = wordcount.WordCount()
       str_ = q.wordcount(text.encode('utf8'))
       str_.sort(key=lambda t:t[1])
       it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
       return it 

@app.route('/success/wordcounting/sort_reverse/<text>')
def success_wordcounting_reverse(text):
       q = wordcount.WordCount()
       str_ = q.wordcount(text.encode('utf8'))
       str_.sort(key=lambda t:t[1])
       str_.reverse()
       it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
       return it 

@app.route('/nltk/autospacing',methods = ['POST','GET'])
def get_text_autospacing():
       if request.method=='POST':
             user = request.form['space']
             return redirect(url_for('success_autospacing', text = user))
       else :
             user = request.args.get('space')
             return redirect(url_for('success_autospacing',text= user))
@app.route('/nltk/wordcounting', methods = ['POST','GET'])
def get_text_wordcounting():
       if request.method == 'POST':
             user = request.form['count']
             return redirect(url_for('success_wordcounting' , text = user))
       else :
             user = request.args.get('count')
             return redirect(url_for('success_wordcounting',text = user))

@app.route('/nltk/wordcounting/sort', methods = ['POST','GET'])
def get_text_wordcounting_sort():
       if request.method == 'POST':
             user1 = request.form['count_sort']
             return redirect(url_for('success_wordcounting_sort' , text = user1))
       else :
             user1 = request.args.get('count_sort')
             return redirect(url_for('success_wordcounting_sort',text = user1))

@app.route('/nltk/wordcounting/reverse', methods = ['POST','GET'])
def get_text_wordcounting_reverse():
       if request.method == 'POST':
             user1 = request.form['count_sort']
             return redirect(url_for('success_wordcounting_reverse' , text = user1))
       else :
             user1 = request.args.get('count_sort')
             return redirect(url_for('success_wordcounting_reverse',text = user1))
@app.route('/')
def index():
       return render_template('index2.html')
if __name__ == '__main__' :
       app.run(host='0.0.0.0',port=8888, debug=True)
