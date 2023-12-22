
# Exploring the World of Cinema through Data: an ADAnalysis

<p align="center">
<img src="images/ab_giphy.gif" style="width: 50%;">
</p>

Web Story : https://epfl-ada.github.io/ada-2023-project-dromadaire/

## Table of Contents

* [1. Abstract](#abstract)
* [2. Research Questions](#rq)
* [3. Additional Datasets](#ad)
* [4. Methods](#methods)
* [5. Further Analysis](#fa2)
* [6. Project Overview](#po)
* [7. Team Orgnization](#to)

## Abstract <a class="anchor" id="abstract"></a>

Main characters often drive the plot and central themes of a movie, making them crucial to the audience's experience and perception. This data analysis project focuses on these pivotal figures, aiming to unravel the intricate relationship between casting choices and audience preferences for main actors within various movie genres. Utilizing datasets like the CMU Movie Corpus and IMDb, we delve into a comprehensive analysis of actor attributes such as age, gender, and career accomplishments.

Our research is guided by key questions: Do specific actor attributes correlate with higher movie ratings? How do these attributes and their impact on film success evolve over time? By filtering our dataset based on time period and primary character features, we aim to uncover patterns and trends that influence cinematic success.

This README documents our journey through this analytical process. It begins with a description of the data sources and an overview of our methodological approach, including data preprocessing, exploratory analysis, and advanced statistical techniques. We then present our findings, discussing their implications for the film industry and potential future research directions. The structure of this document is designed to provide a clear, cohesive narrative of our analytical exploration, offering insights into the fascinating world of cinema through the lens of data.

## 2. Research Questions <a class="anchor" id="rq"></a>

- Can an actor's success in terms of awards and nominations impact the ratings of the movies in which they appear?

- Do viewers tend to rate higher movies in which prolific actors appear?

- How do the connections between actors influence the ratings of the movies they are in?

- Do physical attributes of actors, in terms of age and gender, influence the ratings of the movies they play roles in?

## 3. Additional Datasets <a class="anchor" id="ad"></a>

- **IMDb Non-Commercial Datasets**: The datasets include various aspects of movie and TV shows data like titles, crew, ratings, and episode details. In this project we use datasets title.basics (basic title information), title.principals (main participants), title.ratings (user ratings), and name.basics (personnel details).
Source: https://datasets.imdbws.com/

- **Kaggle Awards Dataset**: This dataset is a scraping of the official Academy Awards, listing winners and nominees between 1927 and 2023. A typical row indicates that a given actor was nominated in a given year for a given movie and whether an oscar was won or not.
Source: https://www.kaggle.com/datasets/unanimad/the-oscar-award


## 4. Methods <a class="anchor" id="methods"></a>

### Data Preparation

In the data preparation stage, our team meticulously analyzed and transformed various data types, converting date formats from dd/mm/yyyy to year-only format. We eliminated columns that were not needed and renamed the remaining ones for uniformity.

We enriched our dataset by performing an inner join between IMDb and CMU movies datasets, using movie titles and release dates as key identifiers. This process integrated additional details such as ratings and IMDb IDs into our data.

Furthermore, we extracted a list of lead actors from the IMDb principals dataset and merged this with our combined movies dataframe. To enhance the data further, we also incorporated information from the Kaggle Awards dataset, adding vital features like nominations and awards.

### Feature Engineering and Extraction

In our datasets, we selectively retain specific features. For actors, we include an ID (from IMDb), name, age, and gender. Movie-related features include the Wikipedia ID, IMDb ID, title, release year, genres, and rating.

Additional actor features are engineered through simple statistical methods:
- **Awards Won**: Count of Academy Awards the actor won before the role.
- **Nominations**: Count of Academy Award nominations prior to the role.
- **Previous Roles**: Total number of roles played by the actor beforehand.
- **Genre Diversity**: Variety of genres the actor has appeared in previously.
- **Age at Release**: Actor's age at the time of the movie's release.

<u>**Dataframe 1: Movies**</u>

Each movie is uniquely identified by its WikiID but might have overlapping names or release years. Unique combinations are formed by "name + year."

<div align="center" style="overflow: hidden; border-radius: 10px;">
  <table border="1" cellpadding="5" style="border-collapse: collapse; border-radius: 10px;">
    <caption><i>Table 1: Example of Movies Dataframe</i></caption>
    <thead>
      <tr>
        <th style="border-top-left-radius: 10px;">Wiki ID</th>
        <th>Movie Name</th>
        <th>Release Year</th>
        <th>Genres</th>
        <th style="border-top-right-radius: 10px;">Rating</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>W_ID1</td>
        <td>MovieName1</td>
        <td>Year1</td>
        <td>Genre1</td>
        <td>Rating1</td>
      </tr>
      <tr>
        <td>W_ID2</td>
        <td>MovieName1</td>
        <td>Year2</td>
        <td>Genre2</td>
        <td>Rating2</td>
      </tr>
      <tr>
        <td>W_ID3</td>
        <td>MovieName2</td>
        <td>Year1</td>
        <td>Genre3</td>
        <td>Rating3</td>
      </tr>
    </tbody>
  </table>
</div>

<br>

<u>**Dataframe 2: Main Actors**</u>

Entries are uniquely identified by the combination of Wiki ID / IMDb ID and Actor ID.

<div align="center" style="overflow: hidden; border-radius: 10px;">
  <table border="1" cellpadding="5" style="border-collapse: collapse; border-radius: 10px;">
    <caption><i>Table 2: Example of Main Actors Dataframe</i></caption>
    <thead>
      <tr>
        <th style="border-top-left-radius: 10px;">**Wiki ID**</th>
        <th>IMDb ID</th>
        <th>Actor ID</th>
        <th>Ordering</th>
        <th>Release Year</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Roles in Movies</th>
        <th>Awards</th>
        <th>Nominations</th>
        <th>Genre Diversity</th>
        <th style="border-top-right-radius: 10px;">Age at Release</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>W_ID1</td>
        <td>I_ID1</td>
        <td>A_ID1</td>
        <td>1</td>
        <td>Year1</td>
        <td>Age1</td>
        <td>Gender1</td>
        <td>NumRoles1</td>
        <td>Award1</td>
        <td>Nomination1</td>
        <td>4</td>
        <td>30</td>
      </tr>
      <tr>
        <td>W_ID1</td>
        <td>I_ID1</td>
        <td>A_ID2</td>
        <td>2</td>
        <td>Year1</td>
        <td>Age2</td>
        <td>Gender2</td>
        <td>NumRoles2</td>
        <td>Award2</td>
        <td>Nomination2</td>
        <td>2</td>
        <td>25</td>
      </tr>
      <tr>
        <td>W_ID2</td>
        <td>I_ID2</td>
        <td>A_ID3</td>
        <td>3</td>
        <td>Year2</td>
        <td>Age3</td>
        <td>Gender3</td>
        <td>NumRoles3</td>
        <td>Award3</td>
        <td>Nomination3</td>
        <td>1</td>
        <td>40</td>
      </tr>
    </tbody>
  </table>
</div>


---

### Feasibility Analysis

Upon reviewing the final datasets, we confirm the feasibility of our analysis. The required features are present, and the data volume is sufficient. We've also introduced flexibility by allowing the selection of a varying number of main actors, enabling us to expand our dataset as necessary.

### Exploratory Data Analysis


In the Exploratory Data Analysis section, our initial focus is on thoroughly examining essential actors and movies features for our analysis, including age, gender, awards, nominations, and genre diversity. This step is crucial for grasping the fundamental characteristics of our dataset. Following this, we engage in a time series analysis to track the evolution of these actor features over time. This approach offers valuable insights into the shifting trends within the film industry.

### Diving into the Research Questions

n this section, we track actor feature trends over time and distinguish between high-rated and low-rated films to identify key attributes linked to film success. Our analysis includes correlating actor features with movie ratings, conducting a temporal examination to observe how these correlations evolve, and comparing actor data from differently rated movies to discern patterns that signal cinematic success.

## 6. Project Overview <a class="anchor" id="po"></a>

<p align="center">
<img src="images/Project_overview.png" style="width: 80%;">
</p>

<br />
<br />

## 7. Team Orgnization <a class="anchor" id="to"></a>

- **Armance Novel**: Feature extraction, Data Visualisation, Feasibility analysis, README

- **Emeline Debalme**: Explore analysis, Cross-analysis, Machine Learning, Data-story

- **Théo Houle**: Explore analysis, Cross-analysis, Data-story, README

- **Kelan Solomon**: Feature extraction, Data Visualisation, Machine Learning, Feasibility analysis

- **Dimitri Jacquemont**: Explore analysis, Cross-analysis, Machine Learning, Data-story

