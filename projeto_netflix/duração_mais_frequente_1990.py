
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv("netflix_data.csv")

# 1ºPasso: Selecionando somente os tipos de filmes 
movies = netflix_df[netflix_df['type'] == 'Movie']
# 2ºPasso: Filtro para filmes na decada de 1990
movies_90s = movies[np.logical_and(movies['release_year'] >= 1990,movies['release_year'] < 2000)]
# 3ºPasso: Plotar o Gráfico em formato de histograma
plt.hist(movies_90s['duration'],color='Blue',rwidth=0.9)
plt.title('Duração mais frequente de filmes em 1990')
plt.xlabel('Duração em minutos')
plt.ylabel('Quantidade de filmes')
plt.xticks([25,50,75,100,125,150,175,200],['25Min','50Min','75Min','100Min','125Min','150Min','175Min','200Min'])
plt.show()
