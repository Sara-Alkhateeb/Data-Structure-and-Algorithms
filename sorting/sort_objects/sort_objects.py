import re
array = [
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

def sort_by_most_recent(array):
    sorted_list = sorted(array, key=lambda x: x['year'], reverse=True)
    return sorted_list

def sort_alphabetical(array):
    sorted_list = sorted(array, key=lambda x: re.sub(r'^(A *|An *|The *)\s', '', x['title'], flags=re.IGNORECASE))
    return sorted_list


if __name__ == '__main__':
        sorted_by_year = sort_by_most_recent(array)
        print('Sorted by year:')
        for movie in sorted_by_year:
            print(movie['title'], movie['year'])

        sorted_by_title = sort_alphabetical(array)
        print('\nSorted by title:')
        for movie in sorted_by_title:
            print(movie['title'], movie['year'])

        print(sort_alphabetical(array))




    


