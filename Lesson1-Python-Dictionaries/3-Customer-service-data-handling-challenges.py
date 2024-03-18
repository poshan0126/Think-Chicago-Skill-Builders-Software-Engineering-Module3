class ServiceTicketTracker:
    def __init__(self):
        # Initial ticket data
        self.service_tickets = {
            "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
            "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
        }

    def open_ticket(self, customer_name, issue_description):
        # Generate a new ticket ID
        new_ticket_id = f"Ticket{int(list(self.service_tickets.keys())[-1][-3:]) + 1:03}"
        # Add the new ticket
        self.service_tickets[new_ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        return f"New ticket opened with ID: {new_ticket_id}"

    def update_ticket_status(self, ticket_id, new_status):
        # Check if the ticket exists
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = new_status
            return f"Ticket {ticket_id} status updated to {new_status}."
        else:
            return "Ticket ID not found."

    def display_tickets(self, status=None):
        for ticket_id, info in self.service_tickets.items():
            if status is None or info["Status"] == status:
                print(f"{ticket_id}: Customer: {info['Customer']}, Issue: {info['Issue']}, Status: {info['Status']}")

# Demo
tracker = ServiceTicketTracker()

# Open a new ticket
print(tracker.open_ticket("Charlie", "Connectivity issue"))

# Update the status of an existing ticket
print(tracker.update_ticket_status("Ticket001", "closed"))

# Display all tickets
print("\nAll Tickets:")
tracker.display_tickets()

# Display only open tickets
print("\nOpen Tickets:")
tracker.display_tickets(status="open")
