# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("Files/netflix_data.csv")

# Movies List 
movies = netflix_df[netflix_df["type"] == "Movie"]

# Movies of 1990s List
movies_1990s = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] < 2000)]

# Histogram
plt.hist(movies_1990s["duration"])
plt.title("Distribution of Movie Durations in 1990s")
plt.xlabel("Duration in minutes")
plt.ylabel("Number of Movies")
plt.show()

duration = 100

# Filter the data again to keep only the Action movies of 1990s
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s
# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)

# A quicker way of counting values in a column is to use .sum() on the desired column
# (action_movies_1990s["duration"] < 90).sum()

# Now filter the short action movies (< 90 minutes)
short_action_movies_1990s = action_movies_1990s[action_movies_1990s["duration"] < 90]

# Plot the histogram for short action movies in the 1990s
plt.hist(short_action_movies_1990s["duration"], bins=10, edgecolor='black')
plt.title("Distribution of Short Action Movie Durations in 1990s (< 90 minutes)")
plt.xlabel("Duration in minutes")
plt.ylabel("Number of Movies")
plt.show()