class Ticket:
    ticket_counter = 2000
    tickets_created = 0
    tickets_resolved = 0

    def __init__(self, creator_name, staff_id, contact_email, description):
        Ticket.ticket_counter += 1
        self.ticket_number = Ticket.ticket_counter
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

        Ticket.tickets_created += 1

    def resolve_ticket(self):
        if "Password Change" in self.description:
            self.generate_password()
            self.response = f"New password generated: {self.new_password}"
        else:
            self.response = "The issue has been resolved."

        self.status = "Closed"
        Ticket.tickets_resolved += 1

    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"
            Ticket.tickets_resolved -= 1
            Ticket.tickets_created += 1

    def generate_password(self):
        self.new_password = self.staff_id[:2] + self.creator_name[:3]

    @staticmethod
    def ticket_stats():
        return {
            "Tickets Created": Ticket.tickets_created,
            "Tickets Resolved": Ticket.tickets_resolved,
            "Tickets To Solve": Ticket.tickets_created - Ticket.tickets_resolved,
        }

    def print_ticket_info(self):
        print("\nTicket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)


def main():
    # create tickets
    ticket1 = Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password change")

    # display initial statistics
    print("Displaying Ticket Statistics")
    stats = Ticket.ticket_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    # display initial tickets
    print("\nPrinting Tickets:")
    ticket1.print_ticket_info()
    ticket2.print_ticket_info()
    ticket3.print_ticket_info()

    # resolve some tickets
    ticket3.resolve_ticket()

    # display ticket information and statistics after resolving tickets
    print("\nDisplaying Ticket Statistics")
    stats = Ticket.ticket_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\nPrinting Tickets:")
    ticket1.print_ticket_info()
    ticket2.print_ticket_info()
    ticket3.print_ticket_info()

    # reopen some tickets
    ticket3.reopen_ticket()

    # display ticket information and statistics after reopening tickets
    print("\nDisplaying Ticket Statistics")
    stats = Ticket.ticket_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\nPrinting Tickets:")
    ticket1.print_ticket_info()
    ticket2.print_ticket_info()
    ticket3.print_ticket_info()


if __name__ == "__main__":
    main()
