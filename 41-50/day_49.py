#Challenge 49: Create a Database
import sqlite3
from contextlib import closing
from itertools import pairwise, islice

def create_table():
    movies = [(2009, "Brothers", "Drama"), (2002, "Spider Man", "Sci-fi"),
              (2009, "WatchMen", "Drama"), (2010, "Inception", "Sci-fi"),
              (2009, "Avatar", "Fantasy")]
    
    cursor.execute("""CREATE TABLE movies(
                       year INTEGER NOT NULL,
                       title VARCHAR(20) PRIMARY KEY,
                       genre VARCHAR(20) NOT NULL
                      );""")
    
    cursor.executemany("INSERT INTO movies VALUES(?, ?, ?);", movies)
    return cursor.execute("SELECT * FROM movies;").fetchall()
    
def get_movies_with(category, item):
    txt = f"SELECT * FROM movies WHERE {category} = ?;"
    item = (item,)
    return cursor.execute(txt, item).fetchall()

def get_movies_withs(*args):
    commands = list(islice(pairwise(args),None, None, 2))
    txt = f"SELECT * FROM movies WHERE {commands[0][0]} = ? "
    bindings = [commands[0][1]]
    
    for category, item in commands[1:]:
        txt += f"OR {category} = ?"
        bindings.append(item)
    txt += ";"    
    return cursor.execute(txt, tuple(bindings)).fetchall()

def delete_table():
    cursor.execute("DROP TABLE movies;")
    return "Table deleted."


with closing(sqlite3.connect('movies.db')) as connection:
    with closing(connection.cursor()) as cursor:
        #a) Once you create a table, run a SQL query to see all the movies in your table.
        print(*create_table(), sep="\n")
        print() 
        #b) Run another SQL query to select only the movie Brothers from the list.
        print(*get_movies_with("title", "Brothers"), sep="\n")
        print()
        #c) Run another SQL query to select all movies that were released in 2009 from your table.
        print(*get_movies_with("year", 2009), sep="\n")
        print()
        #d) Run another query to select movies in the fantasy and drama genre.
        print(*get_movies_withs("genre", "Fantasy", "genre", "Drama"), sep="\n")
        print()
        #e) Run a query to delete all the contents of your table.
        print(delete_table())
        
        connection.commit()
