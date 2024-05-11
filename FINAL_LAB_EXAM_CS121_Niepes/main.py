from Utils.user_manager import UserManager
from Utils.dice_game import DiceGame

def main():
    user_manager = UserManager()
    user_manager.load_users()

    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if user_manager.register(username, password):
                print("Registration successful!")
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = user_manager.login(username, password)
            if user:
                game = DiceGame(user)
                while True:
                    game.menu()
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        game.play_game()
                    elif choice == "2":
                        game.load_scores()
                        game.show_top_scores()
                    elif choice == "3":
                        game.save_scores()
                        game.log_out()
                        break
                user_manager.save_users()
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()