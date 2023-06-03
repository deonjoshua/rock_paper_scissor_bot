import random
from colorama import Fore

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            decision = input(Fore.RED + "\nWhat's your move? rock, paper or"
                             " scissors?\n")
            choice = decision.lower()
            if choice == "rock":
                return choice
            elif choice == "paper":
                return choice
            elif choice == "scissors":
                return choice
            else:
                print("Invalid Input")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move
        if self.my_move == "rock":
            self.my_move = "paper"
        elif self.my_move == "paper":
            self.my_move = "scissors"
        else:
            self.my_move = "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(Fore.RED + f"\nPlayer 1: {move1}\n\nPlayer 2: {move2}\n")
        if beats(move1, move2) is True:
            self.count1 += 1
            print(Fore.RED + f"Player 1 Wins!\n\nScore: Player1: {self.count1}"
                  f" Player2: {self.count2}")
        elif beats(move2, move1) is True:
            self.count2 += 1
            print(Fore.RED + f"Player 2 Wins!\n\nScore: Player1: {self.count1}"
                  f" Player2: {self.count2}")
        else:
            print(Fore.RED + f"It's a Tie!\n\nScore: Player1: {self.count1}"
                  f" Player2: {self.count2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(Fore.RED + "Game start!")
        for round in range(1, 4):
            print(Fore.RED + f"\nRound {round}:")
            self.play_round()
        if self.count1 == self.count2:
            print(Fore.RED + f"\nGame over! It's a Tie!\n\nFinal score: "
                  f"Player1: {self.count1} Player2: {self.count2}")
        elif self.count1 > self.count2:
            print(Fore.RED + f"\nGame over! Player 1 Wins!\n\nFinal score: "
                  f"Player1: {self.count1} Player2: {self.count2}")
        else:
            print(Fore.RED + f"\nGame over! Player 2 Wins!\n\nFinal score: "
                  f"Player1: {self.count1} Player2: {self.count2}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
