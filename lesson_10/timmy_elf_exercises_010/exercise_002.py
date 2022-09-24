# Menu

class Dog: # 1.
    def __init__(self):
        self.food = 0
    
    def eat(self):
        self.food += 1

    def __str__(self):
        return f"I'm your best friend and my food level is ${self.food}"

class Menu: # 2.
    MAIN_MENU_TEXT = """
    Welcome to this program!

    1. Create a new object
    2. Print your object
    3. Delete your object
    
    type q or Q to delete
    """

    def user_choice(self):
        return input("Enter your choice 1-3 or q: ")

    def wait_for_user(self):
        if self.running:
            input("Please press any key to continue.")

    def menu_commands(self, choice):
        if choice == 'q' or choice == 'Q':
            self.running = False
        elif choice == "1": # i.
            self.dog = Dog()
        elif choice == "2": # ii.
            try:
                print(self.dog)
            except AttributeError:
                print("No object available to print") # 3.
        elif choice == "3": # iii.
            try:
                del self.dog
            except AttributeError:
                print("No object to delete") # 4.
                # Alternative self.dog = None

    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()

Menu().start_loop()