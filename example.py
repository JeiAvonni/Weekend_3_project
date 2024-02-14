class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = [i for i in range(1, total_tickets + 1)]
        self.parking_spaces = [i for i in range(1, total_parking_spaces + 1)]
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            parking_space = self.parking_spaces.pop(0)
            self.current_ticket = {'ticket_number': ticket_number, 'parking_space': parking_space, 'paid': False}
            print(f"Your ticket number is {ticket_number}. Parking space {parking_space} is reserved for you.")
        else:
            print("Sorry, the garage is full.")

    def pay_for_parking(self):
        if self.current_ticket:
            amount = input("Please enter the payment amount: ")
            if amount:
                self.current_ticket['paid'] = True
                print("Your ticket has been paid. You have 15 minutes to leave.")
            else:
                print("No payment entered.")
        else:
            print("No active ticket.")

    def leave_garage(self):
        if self.current_ticket:
            if self.current_ticket['paid']:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket['parking_space'])
                self.tickets.append(self.current_ticket['ticket_number'])
                self.current_ticket = {}
            else:
                payment = input("Please pay for your parking before leaving: ")
                if payment:
                    print("Thank you, have a nice day!")
                    self.current_ticket['paid'] = True
                    self.parking_spaces.append(self.current_ticket['parking_space'])
                    self.tickets.append(self.current_ticket['ticket_number'])
                    self.current_ticket = {}
                else:
                    print("No payment entered.")
        else:
            print("No active ticket.")


# Example usage:
parking_garage = ParkingGarage(10, 10)  # Initialize with 10 tickets and 10 parking spaces

parking_garage.take_ticket()
parking_garage.pay_for_parking()
parking_garage.leave_garage()
