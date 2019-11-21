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
  print( count_individuals("Person", "Gender", "Unknown", data))
  return render_template('page1.html', numMentalIllness = count_individuals("Factors", "Mental-Illness", True, data), numWithoutMentalIllness = count_individuals("Factors", "Mental-Illness", False, data),
                         numKnife = get_arms(data)['knife'] , numArmedOther = get_arms(data)['other'], numGun = get_arms(data)['gun'], numArmsUnknown = get_arms(data)['unknown'], numUnarmed = get_arms(data)['unarmed'], numToyWeapon = get_arms(data)['toy weapon'], numUndetermined = get_arms(data)['undetermined'] ,  numSword = get_arms(data)['sword'], numMachete = get_arms(data)['machete'],  numBoxCutter = get_arms(data)['box cutter'], numTaser= get_arms(data)['Taser'],  numUnknownWeapon = get_arms(data)['unknown weapon'], numGunAndKnife= get_arms(data)['gun and knife'], numAx = get_arms(data)['ax'], numBat= get_arms(data)['baseball bat'], numVehicle = get_arms(data)['vehicle'], 
                         numMale = count_individuals("Person", "Gender", "Male", data) , numFemale = count_individuals("Person", "Gender", "Female", data), numGenderUnknown = count_individuals("Person", "Gender", "Unknown", data),
                         numWhite = count_individuals("Person", "Race", "White", data), numBlack = count_individuals("Person", "Race", "African American", data), numAsian = count_individuals("Person", "Race", "Asian", data), numNA = count_individuals("Person", "Race", "Native American", data), numHispanic = count_individuals("Person", "Race", "Hispanic", data), numOther = count_individuals("Person", "Race", "Other", data), numUnknown = count_individuals("Person", "Race", "Unknown", data))

def count_individuals(category, specificCategory, target, data):
  toReturn = 0
  for incident in data:
    if incident[category][specificCategory] == target:
      toReturn +=1
  return toReturn

def get_arms(data):
  list = {}
  for incident in data:
    if incident["Factors"]["Armed"] not in list:
      list[incident["Factors"]["Armed"]]=1
    else:
      list[incident["Factors"]["Armed"]]+=1
      
  smallerList ={}
  smallerList["other"]=0
  for weapon in list:
    if list[weapon]<10:
      smallerList["other"] +=1
    else:
      smallerList[weapon]=list[weapon]
  print(list)
  print(smallerList)
  return smallerList
  
if __name__=="__main__":
    app.run(debug=True)
