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
        final_dict = {}
        for line in reader:
            final_dict.setdefault(line['director_name'], []).append(
                Movie(line['movie_title'],
                      line['title_year'],
                      line['imdb_score']))
    return final_dict


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    valid_directors = [a for a in directors if len(directors[a]) >= MIN_MOVIES]

    director_averages = {}
    for director in valid_directors:
        if directors[director]:
            director_averages[director] = _calc_mean(directors[director])
            # director_averages[director] = statistics.mean(
            #     float(movie.score) for movie in directors[director])

    return director_averages


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(statistics.mean(float(movie.score) for movie in movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    movies = get_movies_by_director()

    directors = OrderedDict(
        sorted(directors.items(), key=lambda x: x[1], reverse=True))
    for i, record in enumerate(directors, start=1):
        print(fmt_director_entry.format(counter=i, director=record,
                                        avg=directors[record]))
        print(sep_line)
        for movie in movies[record]:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title,
                                         score=movie.score))
        print()

        if i == 20:
            break


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
