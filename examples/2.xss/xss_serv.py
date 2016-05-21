from __future__ import print_function

import sqlite3
from flask import Flask, request, make_response, render_template
from wtforms import Form, BooleanField, TextField, PasswordField, validators


app = Flask(__name__)


class CommentForm(Form):
    comment = TextField('Comment', [validators.Required()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CommentForm(request.form)
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    
    if request.method == 'POST' and form.validate():
        try:
            cur.execute("INSERT INTO comments VALUES (?)", (form.comment.data,))
            con.commit()
            
        except Exception as e:
            print("Exception: %s" % e)

    cur.execute("SELECT msg FROM comments")
    comments = [i[0] for i in cur.fetchall()]
    con.close()

    resp = make_response(render_template('comments.html', form=form, comments=comments))
    resp.set_cookie('Authorization', value='tajne_haslo')
    return resp


@app.route('/image')
def reflected_xss():
    # invoke with
    # http://127.0.0.1:5000/image?src=cat.img"><script>alert("XSS")</script>
    img_src = request.args.get('src')
    return render_template('image.html', img_src=img_src)


if __name__ == '__main__':  
    app.run(debug=True)
