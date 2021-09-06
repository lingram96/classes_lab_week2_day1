class Team:
    # attributes
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    # methods
    def add_player (self, new_player):
        self.players.append(new_player)

    def has_player (self, check_player):
        for player in self.players:
            if player == check_player:
                return True
            # else:
            #     pass
        return False

        # if check_player in self.players:
        #     return True
        # else:
        #     return False

        # return check_player in self.players

    def play_game (self, team_won):
        if team_won == True:
            self.points += 3

    