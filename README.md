
# Title 

## Abstract

Main characters often drive the plot and central themes of a movie. Hence, it is interesting to concentrate our analysis exclusively on the main character and study the attributes of the actors who portray them. The goal of this data analysis project is to gain insight into the casting and viewers’ preferences for main characters within various movie genres.

Firstly, we'll filter the dataset based on key criteria: prominent genre, relevant time period, main character, and pertinent features. Next, we'll conduct two studies on the filtered dataset:

1. **Mode Analysis:** Identifying the most frequently chosen actor’s features for main characters.
2. **Preference Analysis:** Determining the audience's top-rated attributes for each character feature to discern the most preferred actor’s features.

In the final phase of our project, we will conduct a comprehensive cross-analysis of the outcomes from the two distinct studies to identify recurring patterns in actor preferences.

## Research Questions

- Do the viewer's preferences influence the type of main actor chosen for a certain movie genre?

- Are there any predominant characteristics for actors chosen to portray main characters in a specific movie genre, and does it evolve over time?

## Additional datasets

- **IMDb Non-Commercial Datasets**: The datasets include various aspects of movie and TV show data like titles, crew, ratings, and episode details. In this project are used datasets title.basics (basic title information), title.principals (main participants), title.ratings (user ratings), and name.basics (personnel details).
Source: https://datasets.imdbws.com/

- **Kaggle Awards Dataset**: This dataset is a scraping of the official Academy Awards listing winners and nominees between 1927 and 2023. A typical row indicates that a given actor was nominated in a given year for a given movie and whether an oscar was won or not.
Source: https://www.kaggle.com/datasets/unanimad/the-oscar-award

## Methods

### Data preparation

In the data preparation phase, we conducted a thorough analysis of data types, including the transformation of dates into years, for example. Unused columns were dropped, and the remaining ones were renamed for consistency. 

An inner merge was performed between IMDb and CMU movies, based on film names and years, augmenting the dataset with ratings and IMDb IDs.

A list of main actors was extracted from the IMDb principals dataset, and then merged with both the merged movies dataframe and Kaggle Awards dataset to add features nomination and awards.

### Feature extraction


This will lead to the creation of our final dataset composed of two data frames.

**Dataframe 1: Movies**

All movies have a unique WikiID but can have the same name or the same release year (not both at the same time), hence there are unique combinations of “name + year”

<div align="center">

| Wiki ID | Movie name | Release year | Genres | Rating |
|---------|------------|--------------|--------|--------|
| W_ID1   | name1      | year1        | Genre1 | Rating1|
| W_ID2   | name1      | year2        | Genre2 | Rating2|
| W_ID3   | name2      | year1        | Genre3 | Rating3|
</div>


**Dataframe 2: Main actors**

The Wiki ID / IMDB ID can appear in several rows if there is more than one main character but the combination “Wiki ID + Actor ID” is unique.

<div align="center">

| Wiki ID | IMDB ID | Actor ID | Order | Release year | Age | Gender | Roles in movies | Roles in drama movies | Awards | Oscars Nominations |
|---------|---------|----------|-------|--------------|-----|--------|---------------|---------------------|--------|---------------------|
| W_ID1   | I_ID1   | A_ID1    | 1     | year1        | Age1| Gender1| Nomination1    | NumDramaMovies1     | Awards1| Ethnicity1          |
| W_ID1   | I_ID1   | A_ID2    | 2     | year1        | Age2| Gender2| NumMovies2    | NumDramaMovies2     | Awards2| Nomination2          |
| W_ID2   | I_ID2   | A_ID3    | 3     | year2        | Age3| Gender3| NumMovies3    | NumDramaMovies3     | Awards3| Nomination3          |


</div>








# Import data

In order to run the jupyter notebooks, you will need to download the dataset. To get it you can simply run the `import_data.py` script. If that doesn't work you can do it manually.

### Manually
1. Go to http://www.cs.cmu.edu/~ark/personas/ and in "Download" click on the the hyper link "dataset" to download the dataset
2. Unzip the files into a new folder `./data` at the same level as this README.
3. Then go to https://datasets.imdbws.com/ and download `title.basics.tsv.gz` and `title.ratings.tsv.gz` 
4. Decompress the two files in a new folder `./data/imdb/`


### Using the script

Run

```bash
pip install -r requirements.txt
python3 import_data.py
```

Your data folder should look like this:

```
data/
└── MovieSummaries/    
    ├── character.metadata.tsv 
    ├── movie.metadata.tsv
    ├── name.clusters.txt
    ├── plot_summaries.txt
    ├── README.txt
    └── tvtropes.clusters.txt
└── imdb/  
    ├── imdb_titles.tsv
    └── imdb_ratings.tsv
└── bo_mojo/  
    └── bo_mojo.csv

```

## Rendu P2
