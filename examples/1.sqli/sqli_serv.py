from __future__ import print_function

import sqlite3
from flask import Flask, request, render_template, redirect, url_for
from wtforms import Form, TextField, PasswordField, validators


app = Flask(__name__)


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()

        try:
            #cur.execute(
            #    "SELECT 1 FROM users WHERE name=:name and pwd=:pwd",
            #    {"name": form.username.data, "pwd": form.password.data}
            #)
            cur.execute(
                "SELECT 1 FROM users WHERE name='" + form.username.data + "' and pwd='" + form.password.data + "'"
            )
        except Exception as e:
            print("Exception: %s" % e)
        
        record = cur.fetchone()
        if record:
            return redirect(url_for('validated'))
    
    return render_template('login.html', form=form)


@app.route('/validated', methods=['GET'])
def validated():
    return render_template('validated.html')


if __name__ == '__main__':  
    app.run(debug=True)
