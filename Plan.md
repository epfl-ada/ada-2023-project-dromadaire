Problématique: Do the actors in the films preferred by viewers possess any notable characteristics? -> plus est ce que les bons films prennent un certain type d'acteur

Questions:
- Can we distingish features from "good films" and all films?
- what features are coreleated with "good films"
- do "good films" have the same kind of actors

A DECIDER:
- Drama ou pas drama (si non on doit enlever nombres de drama avant)
- 1 ou plusieurs main acteurs



# 1. Data exploration
TODO:
df acteurs:
- ajouter un feature isGoodGrade ou jsp
- standardisé les noms
- ajouter average grade
- ajouter graph connection feature machin là

# 2. General feature analysis
Graph de dimi
- voir une correlation entre awards X nominations er Movie_count X movie_count_genre X genres_b4
- intéressant de voir que avant 1970, le nombre movie_count est haut masi après ca se rejoint -> plus important
- awards et nominations

Graph Meuleh
- effectivemnt, les corrolations correspont au graph avant

Graph Kelan
- on voit que d'après ce graph les nominations et awards on la plus grand "influence"

# 3. in depth feature analysis (peut etre?)
2 graphs kelan averageRaiting X awards
- effectivement (toutes années confondues) les films avec le plus d'oscars ont en moyenne un meilleur raiting
- attention big error -> peu de données
- nominations c'est le zbeul jsp


PEUT ETRE
- regression (olm ou autre jsp)
- y'as t'il pas des confounder?
- matching
- regression
Conclusion: awards a vraiment une influence ou pas

# 4. global feature analysis
PCA -> visualise all features in 2D
UMAP -> same but diffrent

Plot kelan chelou avec hexbins
- on peut voir qu'a droite il y a plus de orange -> en moyenne il y a bien des """"" cluster""""" d'acteurs avec des atributs qui jouent dans les films bien notés

# 5 a tester peut etre
Clustering sans averageRating -> après on regarde si les clusters correspondent au rating

# conclusion

On voit que y'a bien que les films biens notés ont des acteurs avec certains features, on peut aussi voir (graph de dim) que les features varient selon les années. Mais qu'en moyenne le nombre d'awards qu'a un acteur a une grade influence sur le rating. 

On peut aussi voir que le mean feature est toujours assez proche du "bonne-note" feature, cela veut dire qu'en moyenne les acteurs qui sont choisi pour les films sont les meme qui font des films avec des bons raitings. 

There is one massive "confounder" -> how good is the actor: a good actor will play in many films, have good ratings and win many oscars











###################################################

1 separe données 30 meilleurs et 30 pires %

2 ttest general

3 Nettoyer ModeAnal (enlever movie count genre, birthyear), enlever temp

4 ajouter 

5 

--------------------------------------------

Are the actor features for high and low rated movies the same or different?


- separer data (Dim)

- ttest pour chaque feature sur toutes années confondues (6 ttest) (Armance)
    - voire influence generale

- Viz 6 plots -> high is above, low is below (Dimitri)
    Graph de dimi
    - voir une correlation entre awards X nominations er Movie_count X movie_count_genre X genres_b4
    - intéressant de voir que avant 1970, le nombre movie_count est haut masi après ca se rejoint -> plus important
    - awards et nominations

- Viz pointplot check awards X average Ratings (Kelan)

- Correlation Emeline (Emeline)
    - Correspond avec graph dimi mais en term de correlation

- Correlation avec ratings (Kelan)
    - Awards et nominations ont le plus gros impact mais ils sont corellés entre eux

- Linear model (peut etre logistic regression) (Theo)
    - voir si awards a vraiment une influence ou pas, check p value
- Matching (Theo)
    - avec awards, check if awards really has an influence on ratings

- Linear model (peut etre logistic regression) (Theo)
    - voir si awards a vraiment une influence ou pas, check pvalue, et la difference ave 1ere logreg

- PCA (Emeline)
    - lookout for clusters



































