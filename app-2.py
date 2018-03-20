#-*- coding: utf-8 -*-
from flask_restful import Resource,Api
from flask import Flask, redirect, url_for, request, render_template
import json
import konltk
from konltk.tokenizer import asp
from flask_jsonpify import jsonify
from konltk.tokenizer import wordcount
from flask_oauthlib.provider import OAuth2Provider
from flask_restful import reqparse
from flask import Flask 
from flask import make_response
from flask import request
app = Flask(__name__)
api = Api(app)
#_userText = request.json['text']

class autospace(Resource):
	def post(self):
		try:
#			result = {
#				'text' : request.json['text']
#			}
#			return jsonify({'text': result})
#			parser = reqparse.RequestParser()
#			parser.add_argument('text', type=str)
#			args = parser.parse_args()

			_userText = request.json['text'] 
			print _userText
			q = asp.KltAsp()

			q.dic_init('/usr/local/asp_dic')
			str_ = q.asp(_userText.encode("utf8"))
			it = json.dumps(str_, ensure_ascii=False, encoding ='utf-8')
			print "before response:", str_
			print "it:", it
			return make_response(it)  
		except Exception as e:
			return {'error': str(e)}
api.add_resource(autospace, '/autospacing')

class wordcount(Resource):
	def post(self):
			_userText = request.json['text']
			q=konltk.tokenizer.wordcount.WordCount()
			str_=q.wordcount(_userText.encode("utf8"))
			it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
			return make_response(it)
api.add_resource(wordcount, '/wordcounting')

class wordcount_sort(Resource):
        def post(self):
                        _userText = request.json['text']
                        q=konltk.tokenizer.wordcount.WordCount()
                        str_=q.wordcount(_userText.encode("utf8"))
			str_.sort(key=lambda t:t[1])
                        it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
                        return make_response(it)
api.add_resource(wordcount_sort, '/wordcount_sort')

class wordcount_reverse(Resource):
        def post(self):
                        _userText = request.json['text']
                        q=konltk.tokenizer.wordcount.WordCount()
                        str_=q.wordcount(_userText.encode("utf8"))
                        str_.sort(key=lambda t:t[1])
			str_.reverse()
                        it = json.dumps(str_, ensure_ascii=False, encoding='utf-8')
                        return make_response(it)
api.add_resource(wordcount_reverse, '/wordcount_reverse')

#@app.route('/nltk/autospacing',methods = ['POST','GET'])
#def get_text_autospacing():
#	if request.method=='POST':
#		try:
#			parser = reqparse.RequestParser()
#			parser.add_argument('text', type=str)
#			args = parser.parse_args()

#			_userText = args['text']

#			q = asp.KltAsp()
#			q.dic_init('/usr/local/asp_dic')
#			str_ = q.asp(_userText.encode("utf8"))

#			return {'Text': str_}
#		except Exception as e:
#			return {'error': str(e)}
#		user = request.form['space']
#		return redirect(url_for('success_autospacing', text = user))
#	else :
#		user = request.args.get('space')
#		return redirect(url_for('success_autospacing',text= user))
 


#@app.route('/')
#def index():
#	return render_template('index.html')

if __name__ == '__main__' :
	app.run(host='0.0.0.0',debug=True)
