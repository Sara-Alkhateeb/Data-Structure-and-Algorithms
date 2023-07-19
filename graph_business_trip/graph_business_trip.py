def business_trip(graph, destination):
    """
    Calculates the total cost of a business trip based on a given graph and destination.

    Args:
        graph (dict): A dictionary representing the graph of travel costs between destinations.
                      The keys represent the source destinations, and the values are dictionaries
                      where the keys represent the adjacent destinations and the values represent
                      the cost of travel between them.
        destination (list): A list of destinations in the order of the planned trip.

    Returns:
        int or None: The total cost of the trip if it is feasible and reachable based on the provided
                     graph and destination. If the trip is not feasible or any of the destinations are
                     not reachable, returns None.
    """
    total_cost = 0

    # Check if the graph contains all the destination and if it's reachable
    for i in range(len(destination) - 1):
        if destination[i] not in graph or destination[i + 1] not in graph[destination[i]]:
            return None

    # Calculate the total cost of the trip
    for i in range(len(destination) - 1):
        total_cost += graph[destination[i]][destination[i + 1]]
    return total_cost

# Example graph representation
graph = {
    'Pandora': {'Arendelle': 150, 'Metroville': 82},
    'Arendelle': {'Pandora':150 , 'Metroville': 99, 'Monstropolis': 42},
    'Metroville': {'Pandora':82 ,'Arendelle': 99 , 'Monstropolis': 105, 'Naboo':26, 'Narina' :37},
    'Monstropolis': {'Arendelle': 42 , 'Metroville': 105, 'Naboo':73},
    'Naboo' :{'Monstropolis': 73, 'Narina' :250 , 'Metroville': 26},
    'Narina':{'Monstropolis': 37, 'Nabo':250,}
}

destination = ['Metroville', 'Pandora']
cost = business_trip(graph, destination)
print(cost)  # Output: 82

destination = [ 'Pandora', 'Metroville', 'Naboo']
cost = business_trip(graph, destination)
print(cost)  # Output: 108

destination = ['Naboo', 'Pandora']
cost = business_trip(graph, destination)
print(cost)  # Output: None
