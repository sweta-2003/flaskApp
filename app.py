from flask import Flaskflaskapp.sweta-2003.repl.co
app=Flask(__name__)

@app.route("/")
def hellow():
  return "<p>hellow world</p>"

if __name__=="__main__":
   app.run(host='0.0.0.0',debug=True)
