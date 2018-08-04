import csv
import statistics
from collections import defaultdict, namedtuple, OrderedDict

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    with open(MOVIE_DATA, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        final_dict = defaultdict(list)
        for line in reader:
            try:
                if int(line['title_year']) >= MIN_YEAR:
                    director = line['director_name']
                    movie_title = line['movie_title']
                    title_year = line['title_year']
                    imdb_score = line['imdb_score']

                    movie = Movie(title=movie_title,
                                  year=title_year,
                                  score=imdb_score)
                    final_dict[director].append(movie)
            except ValueError:
                continue

    return final_dict


def get_average_scores(directors_movies):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    valid_directors = [a for a in directors_movies if
                       len(directors_movies[a]) >= MIN_MOVIES]

    director_averages = {}
    for director in valid_directors:
        movies_list = directors_movies[director]
        if movies_list:
            new_key = (director, _calc_mean(movies_list))
            director_averages[new_key] = movies_list

    return director_averages


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    # return round(statistics.mean(float(movie.score) for movie in movies), 1)

    ratings = [float(movie.score) for movie in movies]
    return round(sum(ratings) / max(1, len(ratings)), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.

    directors dict entry:
        ('James Cameron', 7.9):
            [Movie(title='Avatar\xa0', year='2009', score='7.9'),........]


    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    directors = OrderedDict(
        sorted(directors.items(), key=lambda x: x[0][1], reverse=True))
    for i, record in enumerate(directors, start=1):
        print(fmt_director_entry.format(counter=i, director=record[0],
                                        avg=record[1]))
        print(sep_line)
        for movie in directors[record]:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title,
                                         score=movie.score))
        print()

        if i == NUM_TOP_DIRECTORS:
            break


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
