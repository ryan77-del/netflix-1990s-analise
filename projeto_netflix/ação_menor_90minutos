duration = netflix_df['duration'].mode()[0]
movies_action = netflix_df[netflix_df['genre'] == 'Action']
movies_action_90s = movies_action[np.logical_and(movies_action['release_year'] >=1990,movies_action['release_year'] < 2000)]
print(duration)

short_movie_count = 0
for rotulo,linha in movies_action_90s.iterrows():
    if linha['duration'] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count
print(short_movie_count)
