from random import randint


class casino:
    def __init__(self, list_of_players=[]):
        self.list_of_players = list_of_players

    def show_players(self):
        for x in self.list_of_players:
            print(x.name)

    def start_match(self):
        highest_score = 0
        for gambler in self.list_of_players:
            current_player_score = self.get_dice_scores(gambler)
            if current_player_score > highest_score:
                highest_score = current_player_score
                winner = gambler.name
            elif current_player_score == highest_score:
                winner = "undeclared"
        print("GAME FINISHED\n")
        print("THE WINNER IS PLAYER: " + winner)

    def get_dice_scores(self, gambler):
        throw1 = randint(1, 6)
        throw2 = randint(1, 6)
        throw3 = randint(1, 6)
        throw4 = randint(1, 6)

        values = [throw1, throw2, throw3, throw4]

        print(gambler.name + "'s dices are: \n")
        print(values)

        for i in range(4):
            throw = 1
            outcome0 = 0
            outcome1 = 0
            outcome2 = 0
            outcome3 = 0
            pair_on_first_two = False
            pair_on_last_two = False

            if (values[0] % 2 == 0) and (values[1] % 2 == 0) and (values[2] % 2 == 0) and (values[3] % 2 == 0):
                outcome0 = throw1 + throw2 + throw3 + throw4 + 2

            if (values[0] % 2 != 0) and (values[1] % 2 != 0) and (values[2] % 2 != 0) and (values[3] % 2 != 0):
                outcome0 = throw1 + throw2 + throw3 + throw4 + 3

            # Checking first position
            if throw == 1:
                rep = 1
                for x in range(1, 4):
                    if values[0] == values[x]:
                        rep += 1

                if rep == 2:
                    outcome1 = values[0] * 2
                    pair_on_first_two = True
                if rep == 3:
                    outcome1 = values[0] * 4
                if rep == 4:
                    outcome1 = values[0] * 6
                throw += 1

            # Checking second position
            if throw == 2:
                rep = 1
                for x in range(1, 3):
                    if values[1] == values[1 + x]:
                        rep += 1
                if rep == 2:
                    outcome2 = values[1] * 2
                if rep == 3:
                    outcome2 = values[1] * 4
                throw += 1

            # Checking third position
            if throw == 3:
                rep = 1
                if values[2] == values[3]:
                    rep += 1
                if rep == 2:
                    outcome3 = values[2] * 2
                    pair_on_last_two = True
                throw += 1
            # Choosing the highest score
            if throw == 4:
                highest_score = 0
                if pair_on_first_two == True and pair_on_last_two == True:
                    outcome1 += outcome2
                    outcome2 = 0
                scores = [outcome0, outcome1, outcome2, outcome3]
                for score in scores:
                    if score > highest_score:
                        highest_score = score
                print(gambler.name + "'s score is: \n")
                print(highest_score)
                return highest_score


class player:
    def __init__(self, name):
        self.name = name

    def add_player(self, casino):
        casino.list_of_players.append(self)

    def rem_player(self, casino):
        casino.list_of_players.remove(self)


casino1 = casino()

player1 = player("Player A")
player2 = player("Player B")
player3 = player("Player C")

player1.add_player(casino1)
player2.add_player(casino1)
player3.add_player(casino1)

casino1.start_match()
