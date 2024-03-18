class ItineraryFormatter:
    def __init__(self, itineraries):
        self.itineraries = itineraries

    def format_itineraries(self):
        """
        Formats and returns a string that lists each flight itinerary.
        """
        formatted_str = ""
        for index, (traveler_name, origin, destination) in enumerate(self.itineraries, start=1):
            formatted_str += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
        return formatted_str.strip()

# Sample input of flight itineraries
itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

# Create an instance of the class with the sample itineraries
formatter = ItineraryFormatter(itineraries)

# Call the method to format and print the itineraries
formatted_itineraries = formatter.format_itineraries()
print(formatted_itineraries)
