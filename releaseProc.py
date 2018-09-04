from flask import Flask,url_for,render_template,request,redirect,make_response
from werkzeug.utils import secure_filename
from MongoDA.HandleObjects import MachineScript

app=Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    msList=MachineScript.returnAllData()
    return render_template('index.html',msList=msList)

@app.route('/upload',methods=["POST"])
def upload():
    if request.method=='POST':
        f=request.files['the_file']
        f.save("uploads/"+secure_filename(f.filename));
    return redirect(url_for('hello_world',name=None))

@app.route('/insertNewScriptItem',methods=["POST"])
def insertNewScriptItem():
    ms=MachineScript(branch_name=request.form['branchName'],
                     machine_name=request.form['machineName'],
                     ip_address=request.form['ipAddress'],
                     username=request.form['userName'],
                     password=request.form['userPWD'],
                     script=request.form['scriptPath'],
                     usage=request.form['Usage'],
                     id=0,
                     program=request.form['program']
                    )
    ms.insert();
    return index();

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)