# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections 
# and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Example ticket structure:

# service_tickets = {
#    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }


serviceTickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "Open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "Closed"}
}

def openTicket(customer, issue):
    print('''
     ---Welcome to the Customer Service Form---
          ''')
    customer = input("Whats your name?")
    issue = input("Whats your issue?")
    ticketId = f"Ticket{len(serviceTickets) + 1:03d}"
    serviceTickets[ticketId] = {"Customer": customer, "Issue": issue, "Status": "Open"}
    print(f"New ticket opened: {ticketId}")

def updateTicket(ticketId, status):
    if ticketId in serviceTickets:
        serviceTickets[ticketId]["Status"] = status
        print(f'''
Ticket {ticketId} status updated to: {status}
''')
    else:
        print(f"Ticket {ticketId} not found.")

def displayTickets(status=None):
    if status:
        ticketStatus = {ticketId: ticketInfo for ticketId, ticketInfo in serviceTickets.items() if ticketInfo["Status"] == status}
        if ticketStatus:
            print(f'''
Tickets with status '{status}': 
                  ''')
            for ticketId, ticketInfo in ticketStatus.items():
                print(f"Ticket ID: {ticketId}, Customer: {ticketInfo['Customer']}, Issue: {ticketInfo['Issue']}, Status: {ticketInfo['Status']}")
        else:
            print(f"No tickets found with status '{status}'.")
    else:
        print("All tickets:")
        for ticketId, ticketInfo in serviceTickets.items():
            print(f"Ticket ID: {ticketId}, Customer: {ticketInfo['Customer']}, Issue: {ticketInfo['Issue']}, Status: {ticketInfo['Status']}")


openTicket("customer", "issue")
updateTicket("Ticket001", "Closed")
displayTickets("Open")
displayTickets("Closed")
