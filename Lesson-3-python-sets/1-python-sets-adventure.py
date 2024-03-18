class FlightRouteComparator:
    def __init__(self, our_routes, competitor_routes):
        self.our_routes = our_routes
        self.competitor_routes = competitor_routes

    def find_shared_destinations(self):
        return self.our_routes & self.competitor_routes

    def find_unique_to_our_airline(self):
        return self.our_routes - self.competitor_routes

    def check_no_shared_destinations(self):
        return len(self.our_routes & self.competitor_routes) == 0

    def display_results(self):
        shared_destinations = self.find_shared_destinations()
        unique_destinations = self.find_unique_to_our_airline()
        no_shared_destinations = self.check_no_shared_destinations()

        print(f"Shared Destinations: {shared_destinations}")
        print(f"Destinations unique to our airline: {unique_destinations}")
        if no_shared_destinations:
            print("There are no shared destinations between the airlines.")
        else:
            print("There are shared destinations between the airlines.")

# Example flight routes
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Create an instance of FlightRouteComparator
comparator = FlightRouteComparator(our_routes, competitor_routes)

# Display the comparison results
comparator.display_results()
