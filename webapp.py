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
  get_Arms(data)
  return render_template('page1.html', numMentalIllness = count_individuals("Factors", "Mental-Illness", True, data), numWithoutMentalIllness = count_individuals("Factors", "Mental-Illness", False, data),
                         numKnife = count_individuals("Factors", "Armed", "knife", data), numGun= count_individuals("Factors", "Armed", "gun", data), numArmsUnknown= count_individuals("Factors", "Armed", "unknown", data), numUnarmed= count_individuals("Factors", "Armed", "unarmed", data),
                         numMale = count_individuals("Person", "Gender", "Male", data) , numFemale = count_individuals("Person", "Gender", "Female", data), numGenderUnknown = count_individuals("Person", "Gender", "Unknown", data),
                         numWhite = count_individuals("Person", "Race", "White", data), numBlack = count_individuals("Person", "Race", "African American", data), numAsian = count_individuals("Person", "Race", "Asian", data), numNA = count_individuals("Person", "Race", "Native American", data), numHispanic = count_individuals("Person", "Race", "Hispanic", data), numOther = count_individuals("Person", "Race", "Other", data), numUnknown = count_individuals("Person", "Race", "Unknown", data))

def count_individuals(category, specificCategory, target, data):
  toReturn = 0
  for incident in data:
    if incident[category][specificCategory] == target:
      toReturn +=1
  return toReturn

def get_Arms(data):
  list = {}
  for incident in data:
    if incident["Factors"]["Armed"] not in list:
      list[incident["Factors"]["Armed"]]=1
    else:
      list[incident["Factors"]["Armed"]]+=1
  smallerList ={}
  smallerList["weapons"]["other"]=0
  for weapon in list:
    if list["weapons"][weapon]<10:
      smallerList["weapons"]["other"] +=1
    else:
      smallerList["weapons"][weapon]=list["weapons"][weapon]
  print(list)
  print(smallerList)
  
if __name__=="__main__":
    app.run(debug=False)
