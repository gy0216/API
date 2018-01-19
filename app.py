#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request
import konlp.asp.asp as AS
import json
from flask_jsonpify import jsonify
import konlp.tokenizer.wordcount as WC

app = Flask(__name__)

@app.route('/success/autospacing/<text>')
def success_autospacing(text):
       q = AS.KltAsp()
       q.dic_init('/usr/local/asp_dic')
       str_ = q.asp(text.encode("utf8"))
       it= json.dumps(str_, ensure_ascii=False, encoding ='utf-8') 
       return it

@app.route('/success/wordcounting/<text>')
def success_wordcounting(text):
       q = WC.WordCount()
       str_ = q.wordcount(text.encode('utf8'))
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
             user = request.args.get('space')
             return redirect(url_for('success_wordcounting',text = user))

if __name__ == '__main__' :
       app.run(host='0.0.0.0', debug=True)
