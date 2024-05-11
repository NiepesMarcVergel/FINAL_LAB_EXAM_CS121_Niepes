import random
import os
from Utils.score import Score

class DiceGame:
    def __init__(self, user):
        self.user = user
        self.scores = []

    def menu(self):
        print("Welcome {}!".format(self.user.username))
        print("Menu:")
        print("1. Start game")
        print("2. Show top scores")
        print("3. Log out")

    def play_game(self):

        stage = 1
        self.user.points = 0
        self.user.stages_won = 0
        win = 0

        while True:
            print(f"Stage {stage}:")
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"{self.user.username} rolled: {user_roll}")
            print(f"CPU rolled: {cpu_roll}")
            if user_roll > cpu_roll:
                self.user.points += 1
                self.user.stages_won += 1
                win += 1
                print("You win this round!")
            elif user_roll < cpu_roll:
                print("CPU won this round!")
            else:
                print("It's a tie! Let's roll again.")    
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"{self.user.username} rolled: {user_roll}")
            print(f"CPU rolled: {cpu_roll}")
            if user_roll > cpu_roll:
                self.user.points += 1
                self.user.stages_won += 1
                win += 1
                print("You win this round!")
            elif user_roll < cpu_roll:
                print("CPU won this round!")
            else:
                print("It's a tie! Let's roll again.")    
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)
            print(f"{self.user.username} rolled: {user_roll}")
            print(f"CPU rolled: {cpu_roll}")
            if user_roll > cpu_roll:
                self.user.points += 1
                self.user.stages_won += 1
                win += 1
                print("You win this round!")
                if self.user.stages_won == 3:
                    self.user.points += 3
            elif user_roll < cpu_roll:
                print("CPU won this round!")
            else:
                print("It's a tie! Let's roll again.")

            if win > 2:
                    print(f"Your final score is {self.user.points} points.")
                    choice = input("Press 1 to play again, 0 to quit: ")
                    if choice == "1":
                        win = 0
                        stage += 1
                    else:
                        break

            elif win < 2:
                    print("Game over. You didn’t win this stage.")   
                    print(f"Your final score is {self.user.points} points.")
                    self.save_scores()
                    break
            
            else:
                print("Game over. You didn’t win this stage.")   
                print(f"Your final score is {self.user.points} points.")
                self.save_scores()
                break
            
    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if os.path.exists('data/rankings.txt'):
            with open('data/rankings.txt', 'r') as f:
                for line in f.readlines():
                    username, game_id, points, wins = line.strip().split(',')
                    self.scores.append(Score(username, game_id, int(points), int(wins)))

    def save_scores(self):
        with open('data/rankings.txt', 'w') as f:
            for score in self.scores:
                f.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")

    def show_top_scores(self):
        self.scores.sort(key=lambda x: x.points, reverse=True)
        print("Top 10 scores:")
        for i, score in enumerate(self.scores[:10]):
            print(f"{i+1}. {score.username} - {score.points} points")

    def log_out(self):
        print("Goodbye!")