from flask import Flask, render_template, request, url_for
from cocktailList import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
	return render_template('home.html')
						   

@app.route('/cocktailList',methods=['GET','POST'])
def cocktailList():
	if request.method == 'POST':
		cocktail1 = []
		with open('output.txt', 'r') as f:
			for line in f.readlines():
				l = line.strip().split(',')
				cocktail1.append(l)
		
		return render_template('cocktailList.html',ItemList=cocktail1,cocktailname=request.form['cocktailName'],PreparationData=listToStringWithoutBrackets(getCocktailPreparation(request.form['cocktailName'])),IngredientData=listToStringWithoutBrackets(getCocktailIngredient(request.form['cocktailName'])))
	else:
		cocktail1 = []
		with open('output.txt', 'r') as f:
			for line in f.readlines():
				l = line.strip().split(',')
				cocktail1.append(l)
		return render_template('cocktailList.html',ItemList=cocktail1)
		

@app.route('/makeCocktail',methods=['GET','POST'])
def makeCocktail():
	if request.method == 'POST':
		fruits=request.form['fruit']
		vegetables=request.form['vegetable']
		alcoholicLiqueurs=request.form['alcoholicLiqueur']
		nonalcoholicLiqueurs=request.form['nonalcoholicLiqueur']
		tasteEnhancers=request.form['tasteEnhancers']
		others=request.form.getlist('others')
		putCocktails(fruits,vegetables,alcoholicLiqueurs,nonalcoholicLiqueurs,tasteEnhancers,others)
		retrieval()
		cocktail1 = []
		with open('output.txt', 'r') as f:
			for line in f.readlines():
				l = line.strip().split(',')
				cocktail1.append(l)
		return render_template('makeCocktail.html',matchedcocktail=cocktail1)
	else:
		return render_template('makeCocktail.html')

@app.route('/Adapt',methods=['GET','POST'])
def Adapt():
	if request.method == 'POST':
		check = request.form['AdaptName'] 
		if check == 'true':
			writeAdaptDetails(request.form['AdaptCName'],request.form['AdaptCIngredients'],request.form['AdaptCPreparation'])
			adaptXML()
			return render_template('adaptCocktail.html',Saved = "Done")
		else:
			return render_template('adaptCocktail.html',name=request.form['AdaptName'],PreparationData=listToStringWithoutBrackets(getCocktailPreparation(request.form['AdaptName'])),IngredientData=listToStringWithoutBrackets(getCocktailIngredient(request.form['AdaptName'])))
	else:
		return render_template('adaptCocktail.html')		
	
if __name__ == '__main__' :
    app.run(debug = True)