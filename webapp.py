from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
  with open('police_shootings (1).json') as shooting_data:
    data = json.load(shooting_data)
  return render_template('home.html')

@app.route("/p1")
def render_p1():
  with open('police_shootings (1).json') as shooting_data:
    data = json.load(shooting_data)
  return render_template('page1.html', numMentalIllness = count_individuals("Factors", "Mental-Illness", True, data), numWithoutMentalIllness = count_individuals("Factors", "Mental-Illness", False, data), numMale = 5 , numWomen = 5, numGenderUnknown = 5,numWhite = count_individuals("Person", "Race", "White", data), numBlack = count_individuals("Person", "Race", "African American", data), numAsian = count_individuals("Person", "Race", "Asian", data), numNA = count_individuals("Person", "Race", "Native American", data), numHispanic = count_individuals("Person", "Race", "Hispanic", data), numOther = count_individuals("Person", "Race", "Other", data), numUnknown = count_individuals("Person", "Race", "Unknown", data))

def count_individuals(category, specificCategory, target, data):
  toReturn = 0
  for incident in data:
    if incident[category][specificCategory] == target:
      toReturn +=1
  return toReturn

  
if __name__=="__main__":
    app.run(debug=False)
