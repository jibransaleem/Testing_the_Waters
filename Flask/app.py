from flask import Flask,redirect,url_for,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fail/<int:marks>')
def res1(marks):
    return render_template('fail.html')

@app.route('/pass/<int:marks>') #extra space causes error
def res2(marks):
    res = ''
    if marks >= 50 :
        res = 'PASS'
    else:
        res = "FAIL"
    return render_template('sucess.html',result=res)

@app.route('/result/<int:value>') # extra space causes error
def res(value):
    rslt = ''
    if value>60:
        rslt = 'res1' # if value > 50 call the function res1 
    else:
        rslt = 'res2'
    return redirect(url_for(rslt,marks=value))# you have name parameter marks in pass and fail thats why marks = value 

@app.route('/submit',methods=["POST","GET"])
def submit():
    total_Score = 0 
    if request.method == "POST":
        Mathematics = float(request.form['mathematics'])
        phy = float(request.form['physics'])
        chem = float(request.form['chemistry'])
        bio = float(request.form['biology'])
        total_Score = (Mathematics+phy+chem+bio)/4 
    result =  ''
    if total_Score>=50:
        res='res2'
    else:
        res='res1'
    return redirect(url_for(res,marks=total_Score))


if __name__ == "__main__":
    app.run(debug=True)