from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
   'id':1,
    'title':'Data Scientist',
    'Salary':'Rs.1000000',
    'location':'Bangalore, India'
  },
   {
   'id':2,
    'title':'Backend Engineer',
   
    'location':'Remote'
  },
   {
   'id':3,
    'title':'Frontend Engineer',
    'Salary':'$800000',
    'location':'Canada'
  },
   {
   'id':4,
    'title':'Data Analyst',
    'Salary':'$700000',
    'location':'Japan'
  }
]
@app.route("/")
def hellow():
  return  render_template("home.html",jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def json_list():
  return jsonify(JOBS)
if __name__=="__main__":
   app.run(host='0.0.0.0',debug=True)
