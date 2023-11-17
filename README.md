
# Title 

<p align="center">
<img src="images/ab_giphy.gif" style="width: 30%;">
</p>

## Abstract

Main characters often drive the plot and central themes of a movie. Hence, it is interesting to concentrate our analysis exclusively on the main characters and study the attributes (such as their age, gender,...) of the actors who portray them. The goal of this data analysis project is to gain insight into the casting and viewers’ preferences for main actors within a specific movie genre.

Firstly, we'll filter the dataset based on key criteria: prominent genre, relevant time period, main character, and pertinent features. Next, we'll conduct two studies on the filtered dataset:

1. **Mode Analysis:** Identifying the most frequently chosen actor’s features for main characters.
2. **Preference Analysis:** Determining the audience's top-rated attributes for each character feature to discern the most preferred actor’s features.

In the final phase of our project, we will conduct a comprehensive cross-analysis of the outcomes from the two distinct studies to identify recurring patterns in actor preferences.

## Research Questions

- Are there any predominant characteristics for actors chosen to portray main characters in a specific movie genre and does it evolve over time?

- How does the notoriety of an actor influence his likeliness to be selected for a given role? Do the viewer's preferences influence the casting? How do honors such as Oscars influence the casting? Does the number of roles prior roles? 


## Additional datasets

- **IMDb Non-Commercial Datasets**: The datasets include various aspects of movie and TV shows data like titles, crew, ratings, and episode details. In this project we use datasets title.basics (basic title information), title.principals (main participants), title.ratings (user ratings), and name.basics (personnel details).
Source: https://datasets.imdbws.com/

- **Kaggle Awards Dataset**: This dataset is a scraping of the official Academy Awards, listing winners and nominees between 1927 and 2023. A typical row indicates that a given actor was nominated in a given year for a given movie and whether an oscar was won or not.
Source: https://www.kaggle.com/datasets/unanimad/the-oscar-award

## Methods

### Data preparation

In the data preparation phase, we conducted a thorough analysis of data types, including the transformation of dd/mm/yyyy to years, for example. Unused columns were dropped, and the remaining ones were renamed for consistency. 

An inner merge was performed between IMDb and CMU movies, based on movie name and release date, augmenting the dataset with ratings and IMDb IDs.

A list of main actors was extracted from the IMDb principals dataset, and then merged with both the merged movies dataframe and Kaggle Awards dataset to add features nomination and awards.

---

### Feature extraction

From our various dataset we will retain a few selection of features. For the actors we will keep an ID (sourced from the IMDb dataset), his name, age and gender. For the movies, we keep the wikipedia ID, the IMDb ID, the movie’s title, release year, genre(s) and rating.

On top of that, we have a few additional actor features that we will engineer based on some simple statistics:
- **Awards won**: the number of academy awards won by the actor prior to this role.
- **Nominations**: similarly to the awards won but taking only nominations.
- **Previous roles**: the number of roles the actor played in prior to this role.
- **Previous roles in the same genre**: the above column filtered to keep only movies of the same genre

This will lead to the creation of our final dataset composed of two data frames.

<u>**Dataframe 1</u>: Movies**


Each movie has a unique WikiID but may share the same name or release year (not simultaneously). Therefore, there are unique combinations of "name + year."

<div align="center">

| Wiki ID | Movie name | Release year | Genres | Rating |
|---------|------------|--------------|--------|--------|
| W_ID1   | name1      | year1        | Genre1 | Rating1|
| W_ID2   | name1      | year2        | Genre2 | Rating2|
| W_ID3   | name2      | year1        | Genre3 | Rating3|

<caption>Table 1: Illustration of what final dataframe 1 would resemble" </caption>

</div>


<br>

**<u>Dataframe 2</u>: Main actors**

The Wiki ID / IMDB ID and the Actor ID uniquely identify each entry.

<div align="center">

| Wiki ID | IMDB ID | Actor ID | Ordering | Release year | Age | Gender | Roles in movies | Roles in drama movies | Awards | Oscars Nominations |
|---------|---------|----------|-------|--------------|-----|--------|---------------|---------------------|--------|---------------------|
| W_ID1   | I_ID1   | A_ID1    | 1     | year1        | Age1| Gender1| Nomination1    | NumDramaMovies1     | Awards1| Ethnicity1          |
| W_ID1   | I_ID1   | A_ID2    | 2     | year1        | Age2| Gender2| NumMovies2    | NumDramaMovies2     | Awards2| Nomination2          |
| W_ID2   | I_ID2   | A_ID3    | 3     | year2        | Age3| Gender3| NumMovies3    | NumDramaMovies3     | Awards3| Nomination3          |

<caption>Table 2: Illustration of what final dataframe 2 would resemble" </caption>

</div>

---

### Feasibility analysis

After checking the final datasets, we can conclude that our analysis is feasible. The features can be found within our datasets and there is enough data. We have implemented the option to change the number of main actors that will be analysed, thus growing our dataset if needed.

---
### Exploratory analysis: mode and top-rated attributes

To identify the most frequently chosen actor’s features, we will examine the mode of the data. For determining the top-rated attributes, the mean rating of movies is calculated within a specific actor attribute to identify each top-rated attribute. The distributions of these selected features will be visualized over the years to explore potential differences in value by performing t-test analysis.

### Cross-analysis: differences between the most chosen and highest rated actor’s features

1. **Data visualization**

To visualize variations and parallels between the two methods, we will illustrate our observations using the following type of plot.
This is an example of results and observations we could obtain: 

<p align="center">
<img src="images/crossAnalysis.png" style="width: 40%;">
</p>
<p align="center">
<em>Example of cross-analysis result</em>
</p>

- Years 1 to 5 show diverging trends in the most selected and highest-rated features, suggesting the film industry doesn't align actor selection with viewer preferences.

- In contrast, years 6 to 10 reveal converging trends, indicating the industry may consider viewer preferences when choosing main actors.



<br>

2. **Statistical analyses**

We could perform a t-test to verify the observations made before. By looking at the p-value we could state if there are significant differences between the two distributions across all years and for specific years. In the previous example, interesting years to look at could be year 4 (highest difference) and year 10 (smallest difference).

## Further analyses

###  Machine Learning approach:  prediction of viewers’ ratings 

Another interesting analysis could be trying to find a machine learning algorithm to predict the viewer’s ratings of a film depending on the characteristics of the main character. To do so, we will try to perform a linear regression on our data. Next, we'll proceed to train the chosen machine learning algorithm using a predefined training set and test it with the testing dataset.

###  Most profitable actor

A further analysis could involve conducting a third study to determine the most profitable type of actor by examining the box office revenue. This analysis will help us understand which actor characteristics have the greatest impact on a movie’s financial success within the selected genre. The main challenge we encounter is the high number of missing values for this feature. Hence, we aim to conduct this analysis if we possess the time and means to enrich our database. 

## Project overview

<center>
<img src="images/Project_overview.png" style="width: 80%;">
</center>

<br />
<br />

## Proposed timeline
<div align="center">

| Part   | Task                            | Deadline     |
|--------|---------------------------------|--------------|
| P2     | Data Preparation - Feasibility Analysis | done         |
| P3.1   | Feature Extraction              | 24/11        |
| P3.2   | Exploratory Analysis            | 01/12        |
| P3.3   | Cross-Analysis                  | 08/12        |
| P3.4   | Machine Learning                | 15/12        |
| P3.5   | Data Story                      | 20/12        |
| P3.6   | Most Profitable Actor           | if enough time |

</div>

## Organization within the team

- **Armance Novel**: Feature extraction, Data Visualisation, Feasibility analysis, README

- **Emeline Debalme**: Explore analysis, Cross-analysis, Machine Learning, Data-story

- **Théo Houle**: Explore analysis, Cross-analysis, Data-story, README

- **Kelan Solomon**: Feature extraction, Data Visualisation, Machine Learning, Feasibility analysis

- **Dimitri Jacquemont**: Explore analysis, Cross-analysis, Machine Learning, Data-story


