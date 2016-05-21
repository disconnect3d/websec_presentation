from __future__ import print_function

from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)

global votes
votes = 0

@app.route('/')
def index():
    global votes
    return render_template('index.html', votes=votes)


@app.route('/vote')
def vote():
    global votes
    votes += 1
    return redirect(url_for('index'))


if __name__ == '__main__':  
    app.run(debug=True)
