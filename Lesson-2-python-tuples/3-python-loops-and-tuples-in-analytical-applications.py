class StockDataAnalyzer:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def calculate_average_closing_price(self, stock_symbol):
        total_price = 0
        count = 0
        for symbol, _, closing_price in self.stock_data:
            if symbol == stock_symbol:
                total_price += closing_price
                count += 1
        if count == 0:
            return f"No data found for stock symbol {stock_symbol}."
        else:
            return f"Average closing price for {stock_symbol}: {total_price / count:.2f}"



class EventAttendanceTracker:
    def __init__(self, attendees):
        self.attendees = attendees

    def list_attendees_of_event(self, event_name):
        attendees_list = [name for name, event in self.attendees if event == event_name]
        return f"Attendees of {event_name}: {', '.join(attendees_list)}"

    def count_attendees_per_event(self):
        event_counts = {}
        for _, event in self.attendees:
            if event in event_counts:
                event_counts[event] += 1
            else:
                event_counts[event] = 1
        return event_counts

print("\n\n Task 1")
# Sample stock data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

# Instance of StockDataAnalyzer
stock_analyzer = StockDataAnalyzer(stock_data)
print(stock_analyzer.calculate_average_closing_price("AAPL"))
print(stock_analyzer.calculate_average_closing_price("GOOG"))

print("\n\n Task 2")
# Example attendee data
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
]

# Instance of EventAttendanceTracker
attendance_tracker = EventAttendanceTracker(attendees)
print(attendance_tracker.list_attendees_of_event("Python Conference"))
print("Attendee count per event:", attendance_tracker.count_attendees_per_event())
print("\n\n")