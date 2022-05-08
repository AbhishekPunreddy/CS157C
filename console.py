import pymongo
from pymongo import MongoClient
#1
def getMoviePlotbyTitle(db, value ):
    id="_id"
    collection = db.movies_data
    title="title"
    overview ="overview"
    query= {title: value}
    projection={id:0, overview:1}
    cursor = collection.find(query, projection)
    for record in cursor:
            print(record)
    print("****************************************************************************")
    menu(db)
#13
def getFrenchMovies(db ):
    id="_id"
    collection = db.movies_data
    title="title"
    lang ="original_language"
    query= {lang: "fr"}
    projection={id:0,title:1}
    cursor = collection.find(query, projection)
    for record in cursor:
            print(record)
    print("****************************************************************************")
    menu(db)

#5
def getMoviesReleasedbyYear(db , value):
    id="_id"
    collection = db.movies_data
    Year="Year"
    title="title"
    status="status"
    query= {Year: value, status: "Released"}
    projection={id:0, title:1}
    cursor = collection.find(query, projection)
    for record in cursor:
            print(record)
    print("****************************************************************************")
    menu(db)
#6
def getMoviesbyGenre(db, value ):
    collection = db.movies_data
    id="_id"
    title="title"
    genres = 'genres'
    query= {genres: value}
    projection={id:0,title:1}
    cursor = collection.find(query, projection).limit(10)
    for record in cursor:
            print(record)
    print("****************************************************************************")
    menu(db)
#7
def getMoviesbyTitle(db, value ):
    collection = db.movies_data
    id="_id"
    title="title"
    movieId="movieId"
    query= {title: value}
    projection={id:0,movieId:1}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#14
def getGenresbyTitle(db, value ):
    collection = db.movies_data
    id="_id"
    title="title"
    genres = "genres"
    query= {title: value}
    projection={id:0,genres:1}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#15
def updateReview(db, value ,reviewValue):
    collection = db.movies_data

    title="title"
    review = "review"
    set= "$set"
    
    upRes = collection.update_one({title:value},{set:{review:reviewValue}})
    print(upRes)
    print("****************************************************************************")
    menu(db)
#16
def deleteReview(db, value ):
    collection = db.movies_data

    title="title"
    review = "review"
    unset= "$unset"
    
    upRes = collection.update_one({title:value},{unset:{review:1}}, False, True)
    print(upRes)
    print("****************************************************************************")
    menu(db)
#4
def getPopularMoviesbyYear(db, value ):
    collection = db.movies_data
    id="_id"
    title="title"
    Year = "Year"
    query= {Year: value}
    projection={id:0, title:1}
    cursor = collection.find(query, projection, sort=[("popularity", pymongo.DESCENDING)]).limit(10)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#3
def getTopPopularMovies(db ):
    collection = db.movies_data
    id="_id"
    title="title"
    
    cursor = collection.find({},{id:0,title:1},sort=[("popularity", pymongo.DESCENDING)]).limit(10)

    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#8
def getMovieRatingbyId(db, value ):
    collection = db.ratings
    id="_id"
    match="$match"
    eq="$eq"
    group="$group"
    movie_ID = "$movieId"
    avgRating ="avgRating"
    avg="$avg"
    rating="$rating"
    movieId='movieId'

    cursor = collection.aggregate([{match: {movieId:{eq:value}}},{group:{id:movie_ID, avgRating:{avg:rating}}}])

    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#12
def getUserRatingsCount(db, value ):
    collection = db.ratings
    id="_id"
    match="$match"
    eq="$eq"
    count="$count"
    
    movieId='movieId'

    cursor = collection.aggregate([{match: {movieId:{eq:value}}},{count: "User Rating Count"}])

    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#9
def getMoviebyPixar(db ):
    collection = db.movies_data
    production='production_companies'

    id="_id"

    title="title"
    query = {production: "Pixar Animation Studios"}
    projection={id:0, title: 1}

    cursor = collection.find(query, projection).limit(10)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#2
def getMoviesLT120(db ):
    collection = db.movies_data
    runtime='runtime'
    lte='$lte'
    id="_id"
    title="title"
    
    query= {runtime:{lte:120}}
    projection={title:1,id:0}
    
    cursor = collection.find(query, projection).limit(10)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#10
def getTopMoviesbyTom(db ):
    collection = db.movies_data
    id="_id"
    title="title"
    cast = "cast"
    elem ="$elemMatch"
    eq ="$eq"

    projection={id:0, title:1}
    cursor = collection.find({cast:{elem:{eq:"Tom Hanks"}}}, projection, sort=[("popularity", pymongo.DESCENDING)]).limit(10)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)
#11
def getMovieCast(db, value ):
    collection = db.movies_data
    cast='cast'
    id="_id"

    title="title"
    query = {title: value}
    projection={id:0, cast: 1}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
    print("****************************************************************************")
    menu(db)

def print_menu():
    menu_option={
        1: 'Find Movie Plot by title', 
        2: 'Find movies with duration less than 2 hours',
        3: 'Find Top 10 most popular movies of all time', 
        4: 'Find most popular movies in a year', 
        5: 'Find all movies released in a year', 
        6: 'Get all movie recommendations by genre', 
        7: 'Find Movie Id by title', 
        8: 'Fing average movie rating using Id',
        9: 'Find all movies by Pixar Studios',
        10: 'Find top 10 most popular movies by Tom Hanks',
        11: 'Find the cast of a movie',
        12: 'Find number of user ratings by movie id',
        13: 'Get All French Movies',
        14: 'Find all genres of a movie by title',
        15: 'Update movie review by title',
        16: 'Delete a movie review',
        17: 'Exit'
        }
    for key, value in menu_option.items():
        print(key,".", value)


def menu(db):
    print_menu()
    option = int(input('Enter your choice: '))
    print("Entered Option: ", option)
    if option==1:
        value = str(input('Enter movie title: '))
        print("****************************************************************************")
        getMoviePlotbyTitle(db, value)
    if option==2:
        getMoviesLT120(db)
    if option==3:
        getTopPopularMovies(db)
    if option==4:
        value = int(input('Enter year: '))
        print("****************************************************************************")
        getPopularMoviesbyYear(db, value)
    if option==5:
        value = int(input('Enter year: '))
        print("****************************************************************************")
        getMoviesReleasedbyYear(db, value)
    if option==6:
        value = str(input('Enter Movie Genre: '))
        print("****************************************************************************")
        getMoviesbyGenre(db, value)
    if option==7:
        value = str(input('Enter movie title: '))
        print("****************************************************************************")
        getMoviesbyTitle(db, value)
    if option==8:
        value = int(input('Enter movie id: '))
        print("****************************************************************************")
        getMovieRatingbyId(db, value)
    if option==9:
        print("****************************************************************************")
        getMoviebyPixar(db)
    if option==10:
        print("****************************************************************************")
        getTopMoviesbyTom(db)
    if option==11:
        value = str(input('Enter movie title: '))
        print("****************************************************************************")
        getMovieCast(db, value)
    if option==12:
        value = int(input('Enter movie id: '))
        print("****************************************************************************")
        getUserRatingsCount(db, value)
    if option==13:
        print("****************************************************************************")
        getFrenchMovies(db)
    if option==14:
        value = str(input('Enter movie title: '))
        print("****************************************************************************")
        getGenresbyTitle(db, value)
    if option==15:
        value = str(input('Enter movie title: '))
        reviewValue = str(input('Enter review: '))
        print("****************************************************************************")
        updateReview(db, value, reviewValue)
    if option==16:
        value = str(input('Enter movie title: '))
        print("****************************************************************************")
        deleteReview(db, value)


def main():
    try:
            conn = MongoClient("mongodb://127.0.0.1:27017")
            print("Mongo db Connected successfully!!!")
    except:
            print("Could not connect to MongoDB")
    
    db = conn.movies
    menu(db)

if __name__ == "__main__":
    main()