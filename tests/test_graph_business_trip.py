from graph_business_trip.graph_business_trip import business_trip


def test_business_trip_direct():
    graph = {
    'Pandora': {'Arendelle': 150, 'Metroville': 82},
    'Arendelle': {'Pandora':150 , 'Metroville': 99, 'Monstropolis': 42},
    'Metroville': {'Pandora':82 ,'Arendelle': 99 , 'Monstropolis': 105, 'Naboo':26, 'Narina' :37},
    'Monstropolis': {'Arendelle': 42 , 'Metroville': 105, 'Naboo':73},
    'Naboo' :{'Monstropolis': 73, 'Narina' :250 , 'Metroville': 26},
    'Narina':{'Monstropolis': 37, 'Nabo':250,}
    }

    destination = ['Pandora', 'Arendelle']
    cost = business_trip(graph, destination)
    assert cost == 150


def test_business_trip_possible():
    graph = {
    'Pandora': {'Arendelle': 150, 'Metroville': 82},
    'Arendelle': {'Pandora':150 , 'Metroville': 99, 'Monstropolis': 42},
    'Metroville': {'Pandora':82 ,'Arendelle': 99 , 'Monstropolis': 105, 'Naboo':26, 'Narina' :37},
    'Monstropolis': {'Arendelle': 42 , 'Metroville': 105, 'Naboo':73},
    'Naboo' :{'Monstropolis': 73, 'Narina' :250 , 'Metroville': 26},
    'Narina':{'Monstropolis': 37, 'Nabo':250,}
    }

    destination = ['Pandora', 'Metroville', 'Naboo']
    cost = business_trip(graph, destination)
    assert cost == 108

def test_business_trip_not_possible():
    graph = {
    'Pandora': {'Arendelle': 150, 'Metroville': 82},
    'Arendelle': {'Pandora':150 , 'Metroville': 99, 'Monstropolis': 42},
    'Metroville': {'Pandora':82 ,'Arendelle': 99 , 'Monstropolis': 105, 'Naboo':26, 'Narina' :37},
    'Monstropolis': {'Arendelle': 42 , 'Metroville': 105, 'Naboo':73},
    'Naboo' :{'Monstropolis': 73, 'Narina' :250 , 'Metroville': 26},
    'Narina':{'Monstropolis': 37, 'Nabo':250,}
    }

    destination = ['Pandora', 'Naboo', 'Arendelle']
    cost = business_trip(graph, destination)
    assert cost is None

def test_business_trip_not_included():
    graph = {
    'Pandora': {'Arendelle': 150, 'Metroville': 82},
    'Arendelle': {'Pandora':150 , 'Metroville': 99, 'Monstropolis': 42},
    'Metroville': {'Pandora':82 ,'Arendelle': 99 , 'Monstropolis': 105, 'Naboo':26, 'Narina' :37},
    'Monstropolis': {'Arendelle': 42 , 'Metroville': 105, 'Naboo':73},
    'Naboo' :{'Monstropolis': 73, 'Narina' :250 , 'Metroville': 26},
    'Narina':{'Monstropolis': 37, 'Nabo':250,}
    }

    destination = ['Pandora', 'Amman']
    cost = business_trip(graph, destination)
    assert cost is None

def test_empty_graph():
    graph = {}
    destination = ['A', 'B', 'C']
    cost = business_trip(graph, destination)
    assert cost is None

