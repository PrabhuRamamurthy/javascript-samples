# coding: utf-8

from xml.dom import minidom
from lxml import etree
import os

def getCocktailIngredient(cocktailname) :
	tree = etree.parse('cocktails.xml')
	root = tree.getroot()
	titlelist = root.findall('recipe/title')
	titleValue = cocktailname
	ilist=[] 
	titleRoot = getTitleRoot(titlelist,titleValue)
	for node in titleRoot.getchildren():
			if node.tag == 'ingredients':
				ingredientsList = node.getchildren()
				for i in ingredientsList:
					ilist.append(i.text)
		
	return ilist

	
def getCocktailPreparation(cocktailname) :
	tree = etree.parse('cocktails.xml')
	root = tree.getroot()
	titlelist = root.findall('recipe/title')
	titleValue = cocktailname
	plist=[] 
	titleRoot = getTitleRoot(titlelist,titleValue)
	for node in titleRoot.getchildren():
		if node.tag == "preparation":
			ingredientsList = node.getchildren()
			for i in ingredientsList:
				plist.append(i.text)
	return plist
	
def getTitleRoot(titlelist,titleValue): 
    for title in titlelist:
        if title.text == titleValue:
            titleRoot = title.getparent()
            return titleRoot
	
	
def getCocktailList():
	xmldoc = minidom.parse('cocktails.xml')
	cocktaillist = xmldoc.getElementsByTagName('title')
	cocktaillist1 ={cocktaillist[1],cocktaillist[2],cocktaillist[3]}
	return cocktaillist1
	
	
def get_xmltext(parent, subnode_name):
    node = parent.getElementsByTagName(subnode_name)[0]
    return "".join([ch.toxml() for ch in node.childNodes])
	
def putCocktails(fruits,vegetables,alcoholicLiqueurs,nonalcoholicLiqueurs,tasteEnhancers,others):
	list = ",".join(others)
	text_file = open("input.txt", "w")
	text_file.write("fruit:%s" % fruits+'\n')
	text_file.write("vegetables:%s" % vegetables+'\n')
	text_file.write("alcoholicLiqueurs:%s" % alcoholicLiqueurs+'\n')
	text_file.write("nonalcoholicLiqueurs:%s" % nonalcoholicLiqueurs+'\n')
	text_file.write("tasteEnhancers:%s" % tasteEnhancers+'\n')
	text_file.write("others:%s" % list+'\n')
	text_file.close()
	
#define a function here to read the input text file and generate the output text file 
def xmlParse():
	a=etree.parse("cocktails.xml")
	b=a.getroot()
	d=[]

	list_alchohol=['white rum','kirsch','Cremant','cognac','champagne','vodka','martini','Noilly_Prat','Whiskey','Benedictine','pastis','rum','malibu rum','dry white wine','Porto','dark rum','White martini','Angostura bitter','pisang ambon','cava','Prosecco','Amber rum','lemon liqueur','sparkling wine','campari','vermouth','Creme de café','triple sec','white wine','red martini','plum brandy','rice wine','calvados','cachaca']

	list_fruits=['lemon','raspberry','citrus fruit','strawberry','kiwi fruit','orange','apricot','currant/black currant','lime','"lime zest(outer skin of lime)"','blood orange','pineapple apple','grapefruit','banana','litchi','berry','melon']

	list_veggies=['cucumbers','lime','wasabi','lemongrass','ginger','mint','tomato','coriander','guava']

	list_liqueur=['Lemonade','Blue curacao','syrup','passion fruit syrup','Orange juice','cointreau','grenadine','pineapple juice','coconut','lime juice','Apricot juice','Creme de cassis','apple juice','grapefruit juice','Hard cider','Cranberry juice','Banana juice','Mango juice','Passion fruit juice','rice milk','coconut milk','Tamarin juice','coffee','apple cider','apricot liqueur','worcestershire sauce','"Currant syrup(blackcurrant juice)"','orgeat syrup','grand marnier','litchi juice','berry juice','strawberry juice','coffee liqueur','coca-cola']

	list_te=['sugar','cane sugar','sour cream','tabasco sauce','light whipping cream','egg','cinnamon','nutmeg','brown sugar','anise basil','powdered sugar','granulated sugar','vanilla sugar','celery salt','pepper','milk','salt']
	
	list_others=['ice cube','sparkling water','ice cream','soda water','sparkling mineral water']
	
	#parsing the ingredients out of the xml file and storing them along with the categories
	for i in range(len(b)):
		recipe=[]
		recipe.append(b[i][0].text)
		for c in b[i][1]:
			if c.attrib["food"] is not None:
				if c.attrib["food"] in list_alchohol:
					a='alcoholicLiqueurs:'+c.attrib["food"]
					recipe.append(a)
					continue
				if c.attrib["food"] in list_fruits:
					a='fruit:'+c.attrib["food"]
					recipe.append(a)
					continue
				if c.attrib["food"] in list_veggies:
					a='vegetables:'+c.attrib["food"]
					recipe.append(a)
					continue
				if c.attrib["food"] in list_liqueur:
					a='nonalcoholicLiqueurs:'+c.attrib["food"]
					recipe.append(a)
					continue
				if c.attrib["food"] in list_te:
					a='tasteEnhancers:'+c.attrib["food"]
					recipe.append(a)
					continue
				if c.attrib["food"].lower() in list_others:
					a='others:'+c.attrib["food"]
					recipe.append(a)
					continue
		d.append(recipe)
	#Writing the parsed ingredients of the recipe into a file
	f = open("cocktail_recipe_lib","w")

	for receipes in d:
		print >> f,(',').join(receipes)

	f.close()
	
def getSimilarityScore():
	def fileRead(filepath,var):
		f=open(filepath)
		globals()[var]=f.readlines()
		f.close()

	fileRead("cocktail_recipe_lib",'recipes')
	fileRead("alcoholicLiqueurs",'alcoholicLiqueurs')
	fileRead("nonalcoholicLiqueurs",'nonalcoholicLiqueurs')
	fileRead("fruit",'fruit')
	fileRead("vegetables",'vegetables')
	fileRead("tasteEnhancers",'tasteEnhancers')
	fileRead("others",'others')
	fileRead("input.txt",'input')
	d=[]

	# Snippet to generate similarity score based on similarity matrices
	def getscore(ing,cing,itype):
			reference=eval(str(itype))
			for recs in reference:
				recs=recs.strip()
				recs=recs.split(',')
				if (recs[0]==ing and recs[1]==cing) or (recs[0]==cing and recs[1]==ing):
						return recs[2]

	# User input is verified against recipes to find out similar ones
	for recipe in recipes:
		final_score=0 # Final score for the similarity match of the recipe against user input
		recipe=recipe.strip()
		score={}
		alcohol_content=0
		comp_list=recipe.split(',')
		for comps in comp_list:
			try:
				ctype,cing=comps.split(':')
			except ValueError:
				continue
			score[ctype]=0
			for ingredients in input:
				ingredients=ingredients.strip()
				itype,ing=ingredients.split(":")
				ing_cmp=ing.split(',')
				for sub_ing in ing_cmp:
					if itype == ctype and sub_ing !='':
						scr=getscore(sub_ing,cing,itype) # Getting score for similarities of each and every input ingredients against recipes (Only that are in same category)
						if ctype=="alcoholicLiqueurs":
								alcohol_content+=1
						if scr is not None and score[itype] < scr:
							score[ctype] = scr # Maximum similarity will be retained
		for k,v in score.items():
			final_score+=float(v) # Individual similarity values are added up to get the similarity score between input vs recipe
		if len(comp_list)-1>0:
			rec=comp_list[0],int(final_score/(len(comp_list)-1)*100),alcohol_content
		else:
			rec=comp_list[0],0,alcohol_content
		d.append(rec)

	e=sorted(d,key=lambda x:float(x[1]),reverse=True) # Sort the matches in descending order to find the best set of matches
		
	# Print top 3 matching cases
	if os.path.exists("output.txt"):
		os.remove("output.txt")
	f=open("output.txt","w")
	for a in e[0:3]:
		ac=""
		if a[2]==0:
			ac="Nil" 
		elif a[2] > 0 and a[2] <3:
			ac="Moderate"
		else:
			ac="High"
		f.write(a[0]+","+str(a[1])+"% ,"+ac)
		f.write("\n")
	f.close()
	
def retrieval():
	xmlParse()
	getSimilarityScore()
	
def writeAdaptDetails(cName,cIngredient,cPreparation):
	CIngredientList = cIngredient.split(",")
	CPreparationList = cPreparation.split(".")
	text_file = open("adapt.txt", "w")
	text_file.write("<recipe>"+'\n')
	text_file.write("<title>"+cName.strip()+"</title>"+'\n')
	text_file.write("<ingredients>"+'\n')
	for i in CIngredientList:
		text_file.write("<ingredient food="">"+i.strip()+"</ingredient>"+'\n')
	text_file.write("</ingredients>"+'\n')
	text_file.write("<preparation>"+'\n')
	for i in CPreparationList:
		text_file.write("<step>"+i.strip()+"</step>"+'\n')
	text_file.write("</preparation>"+'\n')
	text_file.write("</recipe>"+'\n')
	text_file.close()

def listToStringWithoutBrackets(list1):
   return str(list1).replace('[','').replace(']','')
   
def adaptXML():
	f=open("cocktails.xml","r")
	a=f.readlines()
	f.close()
	a.pop()
	
	g=open("adapt.txt","r")
	h=g.readlines()
	for i in h:
		a.append(i)

	f=open("cocktails.xml","w")
	for j in a:
		f.write(j)
	f.write("</recipes>")
	