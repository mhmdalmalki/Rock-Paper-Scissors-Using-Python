import random

moves = ["rock", "paper", "scissors"]


class player():
    win = 0
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class AllRockPlayer(player):
    def move(self):
        return "rock"


class RandomPlay(player):
    def move(self):
        return random.choice(moves)


class humanclass(player):
    def move(self):
        while True:
            move = input("  rock   paper  scissors  ? ").lower()
            if move in moves:
                return move
            print(f"please Enter valid move {move} :)")


def beats(one, two):
    return ((one == "rock" and two == "scissors") or
            (one == "scissors" and two == "paper") or
            (one == "paper" and two == "rock"))


class re_play(player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class secoundchoice(player):
    def move(self):
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move2, move1):
            self.p2.win += 1
            print("          player 2 win")
            print("          score")
            print(f"          {self.p1.win} -- {self.p2.win}")
        elif beats(move1, move2):
            self.p1.win += 1
            print("          player 1 win")
            print("          score")
            print(f"          {self.p1.win} -- {self.p2.win}")
        else:
            print("          It is a Tie!")
            print("          score")
            print(f"          {self.p1.win} -- {self.p2.win}")

    def play_game(self):
        print("Game start")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.p1.win < self.p2.win:
            print("     The Winnar is player 2")
            print("     with score")
            print(f"     {self.p1.win} -- {self.p2.win}")
        elif self.p2.win < self.p1.win:
            print("     The Winnar is player 1")
            print("     with score")
            print(f"     {self.p1.win} -- {self.p2.win}")
        else:
            print("     IT IS A TIE!!")
            print("     The score")
            print(f"     {self.p1.win} -- {self.p2.win}")


if __name__ == '__main__':
    game = Game(humanclass(), re_play())
    game.play_game()
