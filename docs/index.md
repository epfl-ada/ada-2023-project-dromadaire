---
layout: home
title: ADAnalysis
---

- Toc
{:toc}

# Introduction & Research Questions

The quest for creating a captivating and memorable movie has captivated filmmakers and audiences alike for decades. The question of what makes a good movie remains a perpetual mystery, with numerous factors contributing to the overall cinematic experience. From the director's vision and the harmonious blend of music to the chosen genre, the elements at play are diverse and interconnected. In this analysis, however, we embark on a focused exploration, focusing on a particular aspect of the cinematic universe: the actors. Looking into the three main characters of a movie allows us to conduct a different analysis, perhaps closer to reality than examining all the characters. Take "James Bond," for example, while there are plenty of side characters they tend to stay in the background. Analyzing all characters might give us features that differ from the true spirit of the movie. Focusing on the main characters is like peeling back the layers to reveal what the movie's all about.

As we dive into the vast realm of film ratings, our inquiry takes shape around a pivotal question: Is there a pattern that distinguishes main actors in well-rated movies from those in poorly-rated ones? In simpler terms, do viewers exhibit a preference for certain types of main actors, and can we uncover a correlation between an actor's presence and the overall success of a film? 

To answer this question we will be looking at the following points:
- Can an actor's success in terms of awards and nominations impact the ratings of the movies in which they appear?
- Do viewers tend to rate higher movies in which prolific actors appear?
- How do the connections between actors influence the ratings of the movies they are in?
- Does physical atributes of actors in terms of age and gender influence the ratings of the movies they play?

# Building our Dataset

While raw data is already gathered, it's not yet ready for analysis due to potential imperfections, complexities, and missing values. The clarity and accuracy of our findings directly depend on the quality of our data - a classic case of “garbage in, garbage out”.

## Data Sources

We used the Movie Summaries dataset provided by the course alongside the extensive IMDb dataset, which offers supplementary information on movies and actors. A pivotal element of our study was the Academy Awards Database. This comprehensive record details past Academy Award winners and nominees from 1927 to 2023.

## Understanding our data

In our data preparation process, we streamlined the dataset for optimal analysis. The first step involved standardizing date formats to years only, fitting our analytical requirements. We then proceeded to remove unused features and titles from the IMDb database that were not classified as movies. Duplication was another area we addressed, ensuring the uniqueness of our dataset.

{% include plots/plot_missing_values.html %}

After looking at the completeness of our data, the rows with critical missing values to our analysis were removed. Filters based on movie runtime were also applied, restricting our focus to films with durations between 20 and 200 minutes, and release dates from 1930 to 2012. These steps collectively sharpened our dataset, making it well-suited for the analysis ahead.

## Feature Engineering

In our feature engineering phase, we focused on enhancing our dataset with actor-centric attributes based on the 3 main actors to deepen our analysis:

**TODO: table**

- Counting the number of awards and nominations each actor had accumulated up until the year of the movie’s release.
- Calculating the total number of movies each actor had appeared in up until the movie in question.
- Assessing the diversity of an actor's roles by counting the number of different genres they had worked in up until that point.
- Looking at the actor connections and their influence in the node graph
- Average IMDb movie rating in which the actor has played
- The decade in which the movie was released

We had a look at the connections between actors by constructing a network graph. To do this we created a bipartite graph between actors and movies and then projected it onto the actors. We then could calculate the eigenvector centrality to measure the influence of an actor in the network. The following graph displays this centrality after filtering out the “non-influential” actors for readability reasons.

{% include plots/network_graph.html %}

These enhancements were crucial in providing a more nuanced understanding of an actor's experience, versatility, and recognition in the industry, contributing to a more comprehensive analysis of their impact on the movies they were part of. After the filtering of our data, we can observe that we have significantly reduced the number of films in our dataset. However, the distribution of the movies filtered is similar to the all movies with IMDb scores.

{% include plots/graph_filtering_vs_all.html %}

# Exploratory Data Analysis

## Datasets Overiew

In our dataset, we've collected and combined key actor attributes. Our analysis will focus on examining the following actors features: 

- Age at release: the age of the actor at the time of the release of the movie
- Is male: binary indicator representing whether the actor is male (True) or not (False)
- Movie count: the total number of movies in which the actor has appeared
- Actor connections: the importance of the node in the actor connection graph
- Genre diversity: measure of the variety of movie genres in which the actor has participated
- Nominations: the total number of award nominations received by the actor
- Awards: the total number of awards won by the actor
- Average rating: Average IMDb movie rating in which the actor has played
- Is good: binary variable that indicates whether a film is considered high-rated or low-rated based on a predefined threshold
- Movie release year range: the decade in which the movie was released
- Primary Name: the name and surname of the actor

This dataset provides a comprehensive foundation for our analysis, offering valuable insights into the dynamics of the film industry and the impact of actors on cinematic success.

## Evolution of Features over time


Let's first have a look at the mean of our features over time, to get a general grasp of their trends.

{% include plots/graph_features_over_time_average.html %}

- **Awards**: We can observe a maximum average number of awards per actor in the 1950’s, followed by a long-term decrease over the decades. This observation could be due to an increased number of actors over time, which makes it more difficult to obtain an award. Note that the average awards are so low (between 0.02 and 0.07) as very few actors have awards
- **Nominations**: The same observation can be made about the average number of nominations as this plot follows the same trend as the awards.
- **Movie count**: We can observe a maximum peak in the 1940s followed by a sharp decrease until the 1980’s. Actors in earlier decades may have participated in more movies, which has since stabilised.
- **Diversity of genres**: The same observation can be made about the diversity of actors' participation in movie genres, as this plot follows the same trend as the movie count.
- **Gender (Is Male)**: The film industry appears to have been and continues to be male-dominated, although the data suggests a small shift towards more gender diversity.
- **Age at release**: The average age of actors has a peak in the 1970s, but the plot doesn’t show a clear trend of becoming younger or older over the decades. 
- **Actor Connections**: There is a steep decline in the average value of actor connections from the 1930s onward. Earlier actors may have had more connections within the industry, which could suggest a tighter-knit community or a smaller industry at the time.

## Correlation between features

We saw previously that some of our features seem to follow similar trends throughout time. Let’s have a look to see if there are any significant correlations.

{% include plots/correlation_matrix_btw_features_plot.html %}

First, this matrix indicates that movie count and genre diversity exhibit a very high positive correlation (0.87), suggesting that prolific actors have a significant presence in a wide range of genres. Another high correlation can be observed between awards and nominations (0.71). 

The connections an actor makes tend to be higher when the actor is prolific, as suggested by the moderate correlations actor_connections has with movie_count (0.53) and genres_diversity (0.50). We can notice that except for a weak correlation with age at release, the gender of an actor is not correlated to the features, meaning the success and experience of an actor doesn’t depend on their gender. All the other correlations are weak or null.
These correlations explain the matching trends observed between awards and nominations, as well as movie_count and genre_diversity in [previous section](#evolution-of-features-over-time).


# Deep Dive into Analysis

To eliminate the influence of “medium” films,  we have chosen to take the 30th upper and lower percentiles of movies to define well rated and poorly rated movies. This reduces our dataset but allows us to better distinguish a good IMDb rating from a bad one. We have also binned our data into decades, allowing us to analyse a general trend rather than spikes in individual years.

## Correlation of Features with Ratings

Firstly, we should confirm whether or not the actor features we've identified do indeed correlate with the IMDb film rating.

{% include plots/graph_correlation_with_average_rating.html %}

The feature with the highest correlation is actor connections, followed by nominations and genre diversity. It is however important to note that the correlations are not very large, topping out at 0.15.

## Well-rated and poorly-rated movies over time by feature

{% include plots/graph_features_over_time_is_good.html %}

These plots suggest there are observable differences in the features of actors between high and low-rated movies. Specifically, actors in higher-rated movies have a history of more awards and nominations, have appeared in more movies, and have had experience across a wider range of genres before the current movie. These findings indicate that actors' experience and recognition (in terms of awards and variety of roles) may correlate with the ratings of the movies they are in. Let’s investigate the features' evolutions in more detail.

**Awards, nominations, movie count and genre diversity**

The first thing to note is that these four features are always statistically significant no matter the year. They all have substantial differences between well-rated and poorly-rated movies before the 1980s. After this, there is a slight converging trend that could be due to the large number of actors and diversity of movies, that there are today.

**Is male and age at release**

Not much can be concluded from these graphs due to the lack of statistical significance.

**Actor connections**

The first thing that stands out from this graph is the extremely low confidence interval. This feature has statistical significance into the late 1970s and after this both lines become indistinguishable.

## Correlation of Features with ratings over the years

Now that we have had a look at the temporal graphs, we know that the correlations between actor features and average ratings shown previously are probably not accurate over all years. Let’s have a look at the correlations throughout the decades.

{% include plots/graph_correlation_with_rating_by_years.html %}

The same features stand out, actor connections has a high correlation, especially at the start of the 20th century. Nominations also has a high correlation over the years and so does genre diversity. Now that we have found the influential features, we will continue this analysis by looking at each feature individually. One important thing to take from this graph is the reduction in general correlation over the years, this means that the features that we have collected have a smaller influence today than they did 8 decades ago. 

## Features Analysis

We will now analyse more specifically the most influential actor’s features impacting the ratings. As awards and nominations are highly correlated, we will focus more closely on nominations as it has a higher correlation with ratings. Finally,  between genre_diversity and movie_count, which are also highly correlated,  we will be concentrating on  genre_diversity due to its higher general correlation. 

### Top 15 actors in connections, nominations, and genre diversity

In the following word clouds, we can observe the top 15 actors for the three features mentioned above. This can be considered a sanity check to be sure that our 3 most influential features are not tied to the same actors which would influence our analyses.

### ???









# Results

Here we summarize the results that we found 

# Source

list of arcticles and whatever else we needed to get to our final result

let's see if we actually keep this