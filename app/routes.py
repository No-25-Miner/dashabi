from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
#1个视图函数
def index():
	user = {'username':'Miguel'}
	posts = [
		{
			'author':{'username':'John'},
			'body':'Beautiful day in Portland'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html',title='Home',user=user,posts=posts)

