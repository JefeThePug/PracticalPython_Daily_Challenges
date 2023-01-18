#Challenge 46: Create a DataFrame
import pandas as pd

def build_dataframe(movies):
    movie_list = [movie.split() for movie in movies]
    d = dict(zip(["Year", "Title", "Genre"], zip(*movie_list)))
    return pd.DataFrame(d)


raw_data = """2009 Brothers Drama
2002 Spider-Man Sci-fi
2009 WatchMen Drama
2010 Inception Sci-fi
2009 Avatar Fantasy"""
print(build_dataframe(raw_data.split("\n")))


#Extra Challenge: Website Data with Pandas
def get_web_table(link):
    type_table = pd.read_html(link)[1]
    return type_table[['Type', 'Mutability']]
 

link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
print(get_web_table(link))
