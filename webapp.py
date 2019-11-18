from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
  with open('police_shootings (1).json') as shooting_data:
    counties = json.load(shooting_data)
  return render_template('home.html')

@app.route("/p1")
def render_p1():
  with open('police_shootings (1).json') as shooting_data:
    counties = json.load(shooting_data)
  return render_template('page1.html', numWhite = 20)
    
  
if __name__=="__main__":
    app.run(debug=False)
