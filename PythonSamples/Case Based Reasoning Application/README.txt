THIS APPLICATION IS A COCKTAIL RECOMMENDER SYSTEM

IT USES THE CORE CONCEPT OF CASE BASED REASONING.

The system tries to implement the 4 RE’s of CBR i.e., Retrieve, Reuse, Revise and Retain.

Retrieve: Here the K-NN algorithm is used to calculate the similarity function, which is then used to calculate overall similarity score of the case based on weights assigned to each attribute of the case.

Reuse: If the ingredients of the user exactly match the ingredients present in the case then we reuse the existing case and give the output pertaining to the existing case. Here, the output is the cocktail with its recipe.

Revise: If the retrieved case has attribute values different from the user input i.e, the ingredients present in the retrieved cases are different from user ingredients then adaptation or revision is performed on the retrieved case by simple substitution of the input values into the case attribute value.

Retain: Once the case is revised, its presented to the user who then has to validate and test the solution, after which he either terms the case success or failure. If success this new case is added into the case library.

FILES 

1. cocktails.xml contains the cocktail details like their ingredients and preparation method

 
