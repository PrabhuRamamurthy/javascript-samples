import os

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
	comp_list=recipe.split(',')
	for comps in comp_list:
		try:
			ctype,cing=comps.split(':')
		except ValueError:
			continue
		for ingredients in input:
			ingredients=ingredients.strip()
			itype,ing=ingredients.split(":")
			if itype == ctype and ing !='':
				score[itype]=0
				scr=getscore(ing,cing,itype) # Getting score for similarities of each and every input ingredients against recipes (Only that are in same category)
				if scr is not None and score[itype] < scr:
					score[itype] = scr # Maximum similarity will be retained
	for k,v in score.items():
		final_score+=float(v) # Individual similarity values are added up to get the similarity score between input vs recipe
	rec=comp_list[0],final_score

	d.append(rec)

e=sorted(d,key=lambda x:float(x[1]),reverse=True) # Sort the matches in descending order to find the best set of matches

# Print top 3 matching cases
if os.path.exists("output.txt"):
	os.remove("output.txt")
f=open("output.txt","w")

for a in e[0:3]:
	f.write(a[0]+","+str(a[1]))
	f.write("\n")
f.close()