from __future__ import print_function

from flask import Flask, render_template, url_for, redirect, request, make_response
from wtforms import Form, IntegerField, validators

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


class AdminVoteForm(Form):
    number = IntegerField('Number of votes', [validators.Required()])


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminVoteForm(request.form)
    
    if request.method == 'POST' and form.validate() and request.cookies.get('Authorization') == 'tajne_haslo':
        global votes
        votes += form.number.data
        return redirect(url_for('admin'))
    
    resp = make_response(render_template('admin_vote.html', form=form, votes=votes))
    resp.set_cookie('Authorization', value='tajne_haslo')
    return resp


if __name__ == '__main__':  
    app.run(debug=True)
