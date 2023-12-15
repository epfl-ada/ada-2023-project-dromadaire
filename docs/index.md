---
layout: page
title: ADAnalysis
---

- Toc
{:toc}

# Introduction

The main character has a key role in the realm of cinema because he drives the action. Indeed, he is the narrative focal point that holds the entire story together and serves as the audience’s guide. Main characters often become the emblem of a movie, such as Jack Sparrow for "Pirates of the Caribbean" or Harry Potter for the "Harry Potter" series. This is the reason why we hold our interest on the main character in this study. 

Furthermore, looking into the main character of a movie allows us to conduct a different analysis, perhaps closer to reality than examining all the characters. Take "James Bond," for example. While there are plenty of side characters, particularly female ones, they tend to stay in the background. Analyzing all characters might give us features that differ from the true spirit of the movie. Focusing on the main character is where the real action is. So, when things might seem a bit biased or not quite right, checking out the main character is like peeling back the layers to reveal what the movie's really all about. 

The goal of this project is to analyze the different attributes of the actors who portray them within a specific movie’s genre by studying the CMU Movie Corpus dataset. 

We have chosen to conduct a comprehensive analysis of our dataset, integrating both mode analysis and preference analysis. In our exploration, we aim to identify the most frequently chosen actor’s features for main characters by utilizing the mode of each feature. Simultaneously, we explore the audience preferences by determining the top-rated attributes for each character feature. This combined analysis aims to provide a comprehensive understanding of the nuanced relationship between casting choices and audience expectations.

# Filtering 

We first perform a meticulous filtering of the dataset. In our dataset, we conducted a meticulous analysis of missing values across various columns, ensuring the robustness and relevance of our upcoming analytical initiatives. This careful examination allows us to ascertain the completeness of our data, laying a solid foundation for accurate and insightful analyses.
=> mettre principaux résultats sur les missing values 

Additionally, we dropped unused columns and opted to focus our analysis on a pivotal genre : the drama genre, constituting xx% of our movie dataset 


# The data

this parts describes the datasets that we are going to use, what they look like, what we have to be careful about etc... We also show the data transformations that are going to fir our purpose

We are working with the CMU Movie Corpus dataset. In the data preparation phase, we decide to enrich our data set by merging two additional datasets : 

-	IMDb Non-Commercial Datasets: The datasets include various aspects of movie and TV shows data like titles, crew, ratings, and episode details. In this project we use datasets title.basics (basic title information), title.principals (main participants), title.ratings (user ratings), and name.basics (personnel details). Source: https://datasets.imdbws.com/

-	Kaggle Awards Dataset: This dataset is a scraping of the official Academy Awards, listing winners and nominees between 1927 and 2023. A typical row indicates that a given actor was nominated in a given year for a given movie and whether an oscar was won or not. Source: https://www.kaggle.com/datasets/unanimad/the-oscar-award

## DataFrames 

this is the list of the datasets we are going to use and a little bit of information about them (for more details about things such as NA count, we could link to an other page, see example below)

The list of main characters is extracted from the IMDb dataset, forming the basis of our analysis using two DataFrames: the Movie DataFrame and the Main Actor DataFrame.

### Main Actor DataFrame
this is the first dataset, it is about this and here is where you can find it and some brief information about the pitfalls and things to be careful with. See [this page](./dataset1_details.md)

- In the Main Actor DataFrame, we will include a selected set of features from various datasets:
  •	An ID
  •	Age
  •	Name
  •	Genre
  Additionally, we will incorporate additional actor features obtained through simple statistics:
  •	Awards won
  •	Nominations
  •	Previous roles
  •	Previous roles in the same genre

### Movie DataFrame

- For the Movie DataFrame, we will retain the following features:
  •	Wikipedia ID
  •	IMDb ID
  •	Movie title
  •	Release year
  •	Genre
  •	Rating


## Shaping our final datasets

here we explain the datasets we want to end up with (and why) and everything we did to get there

Finish by showing pictures of the final datasets

At the end, we obtain two DataFrames: 
- DataFrame 1 : 
- DataFrame 2 : 

# Research

Here we detail the steps we are taking to reach our final goal

We probably want to add chapters to further structure this part

# Results

Here we summarize the results that we found 

# Source

list of arcticles and whatever else we needed to get to our final result

let's see if we actually keep this


<img src="/assets/img/popcorn_bg.png" class="btm_img">