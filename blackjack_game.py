from player import Player
from dealer import Dealer

class BlackjackGame:
    def __init__(self, player_names):
        self.dealer = Dealer() #creating object to represent dealer
        self.player_list = [] #list of players
        for player in player_names: #adding the players to the list 
           self.player_list.append(Player(player, self.dealer))


    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        toReturn = "" 
        rounds = 1
        while rounds <= num_rounds: #loop for playing num_round number of rounds
            toReturn += "Round {}\n".format(rounds)
            self.dealer.shuffle_deck() #shuffling the deck
            x = 1
            while x <= 2: #loop for dealing two cards to everyone
                for i in self.player_list:
                    self.dealer.signal_hit(i)
                self.dealer.signal_hit(self.dealer)
                x += 1

            if self.dealer.card_sum == 21: #if dealer has a natural blackjack
                for y in self.player_list:
                    if y.card_sum == 21:
                        y.record_tie()
                    else:
                        y.record_loss()

            else: #if dealer does not have a natural blackjack
                for j in self.player_list: #simulating the round for players
                    j.play_round()
                self.dealer.play_round() #simulating the round for the dealer

                for k in self.player_list:
                    if self.dealer.card_sum > 21: #recording win/losses/ties if dealer goes bust
                        if k.card_sum <= 21:
                            k.record_win()
                        else:
                            k.record_loss()
                    else: #recording wins/losses/ties if the dealer does not go bust
                        if k.card_sum > self.dealer.card_sum:
                            k.record_win()
                        elif k.card_sum == self.dealer.card_sum:
                            k.record_tie()
                        elif k.card_sum < self.dealer.card_sum:
                            k.record_loss()

            toReturn += "{}\n".format(str(self.dealer))
            self.dealer.discard_hand() #discarding the hand for the dealer for next round
            for l in self.player_list:
                toReturn+="{}\n".format(str(l))
                l.discard_hand() #discarding hands for players for the next round
            rounds += 1
        return toReturn[:-1]


    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for i in self.player_list: #reseting the stats for players
            i.discard_hand()
            i.reset_stats()
        self.dealer.discard_hand() #reseting the stats for the dealer
        self.dealer.reset_stats()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
