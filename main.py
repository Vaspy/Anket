from flask import Flask, render_template
from forms import *
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	form1=AnketForm()
	return render_template('forms.html', form1=form1)

if __name__=='__main__':
	app.run(debug=True)