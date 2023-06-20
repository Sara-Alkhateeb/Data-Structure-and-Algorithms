import pytest
from sorting.sort_objects.sort_objects import sort_by_most_recent, sort_alphabetical

movies = [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"]
        },
        {
            "title": "The Godfather",
            "year": 1972,
            "genres": ["Crime", "Drama"]
        },
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genres": ["Action", "Crime", "Drama", "Thriller"]
        },
        {
            "title": "Pulp Fiction",
            "year": 1994,
            "genres": ["Crime", "Drama"]
        },
        {
            "title": "Inception",
            "year": 2010,
            "genres": ["Action", "Crime", "Drama", "Mystery", "Sci-Fi", "Thriller"]
        },
        {
            "title": "Schindler's List",
            "year": 1993,
            "genres": ["Biography", "Drama", "History"]
        },
        {
            "title": "Interstellar",
            "year": 2014,
            "genres": ["Adventure", "Drama", "Sci-Fi"]
        },
    ]


def test_sort_by_most_recent():
    # Test sorting by year in descending order
    sorted_movies = sort_by_most_recent(movies)
    assert sorted_movies[0]["title"] == "Interstellar"
    assert sorted_movies[0]["year"] == 2014
    assert sorted_movies[-1]["title"] == "The Godfather"
    assert sorted_movies[-1]["year"] == 1972


def test_single_movie():
    # Test sorting by year for a single movie
    single_movie = [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"],
        }
    ]
    sorted_single_movie = sort_by_most_recent(single_movie)
    assert sorted_single_movie[0]["title"] == "The Shawshank Redemption"
    assert sorted_single_movie[0]["year"] == 1994


def test_empty_list():
    # Test sorting an empty list
    empty_list = []
    sorted_empty_list = sort_by_most_recent(empty_list)
    assert sorted_empty_list == []


def test_sort_movies_by_title():
    expected = [
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genres": ["Action", "Crime", "Drama", "Thriller"],
        },
        {   "title": "The Godfather", 
            "year": 1972, 
            "genres": ["Crime", "Drama"]},
        {
            "title": "Inception",
            "year": 2010,
            "genres": ["Action", "Crime", "Drama", "Mystery", "Sci-Fi", "Thriller"],
        },
        {
            "title": "Interstellar",
            "year": 2014,
            "genres": ["Adventure", "Drama", "Sci-Fi"],
        },
        {   "title": "Pulp Fiction", 
            "year": 1994, 
            "genres": ["Crime", "Drama"]},
        {
            "title": "Schindler's List",
            "year": 1993,
            "genres": ["Biography", "Drama", "History"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"],
        },
    ]
    actual = sort_alphabetical(movies)
    assert actual == expected
