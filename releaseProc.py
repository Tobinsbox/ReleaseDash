from flask import Flask,url_for,render_template,request,redirect,make_response
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=["POST"])
def upload():
    if request.method=='POST':
        f=request.files['the_file']
        f.save("uploads/"+secure_filename(f.filename));
    return redirect(url_for('hello_world',name=None))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)