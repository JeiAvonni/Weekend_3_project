class Garage:
    def __init__(self):
        self.tickets=[1,2,3,4,5]
        self.current_ticket={}
        print("parking_garage_build")
    
    
    def take_ticket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            self.current_ticket['ticket_number']=ticket_number
            self.current_ticket['paid']=False
            print(f"Your ticket number is {ticket_number}.")
        else:
            print("You have reserved parking. Please take your ticket! You have 15 minutes of parking!")
    
    def pay_for_parking(self):
        if self.current_ticket:
            amount = input("Please enter the payment amount: ")
            if amount:
                self.current_ticket['paid'] = True
                print("Successfully paid for parking!")
        else:
            print("No active ticket.")
    
    
    
    def leave(self):
        print("Have a nice day!")



garage=Garage()

is_running = True
while is_running:
    selection = input("Staying, Leaving, Paying, Quit").title()
    if selection == 'Staying':
        garage.take_ticket()
    if selection == 'Leaving':
        garage.leave()
    if selection == 'Paying':
        garage.pay_for_parking()
    if selection == 'Quit':
        is_running = False

