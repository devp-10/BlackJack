import random


class Player:

    def __init__(self, name, dealer):
        self.name = name
        self.dealer = dealer
        self.win_counter = 0
        self.loss_counter = 0
        self.tie_counter = 0
        self.hand = []


    def decide_hit(self):
        return random.choice([True, True, False])

    def deal_to(self, card_value):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.hand
        [11]
        >>> player.deal_to(10)
        >>> player.hand
        [11, 10]
        """
        self.hand.append(card_value) #adding card_value to the list
        

    @property
    def card_sum(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(2)
        >>> player.card_sum
        2
        >>> player.deal_to(10)
        >>> player.card_sum
        12
        """
        return sum(self.hand) #adding all the elements in the list
        

    def play_round(self):
        """
        >>> from dealer import Dealer
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, dealer)

        We see that after the first call the play_round, we have only hit once as dictated by decide_hit
        >>> player.play_round()
        >>> player.hand
        [10]

        After calling play_round again, decide_hit has decided to stand
        >>> player.play_round()
        >>> player.hand
        [10]

        After a third call to play_round, we've decided to hit, but busted!
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]

        After a final call to play_round, our hand shouldn't change since we've already busted
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        """
        while self.card_sum<21 and self.decide_hit()==True: #simmulating a round of blackjack of the player
            self.dealer.signal_hit(self) #to decide whether to stand or hit (randomly)
        

    def discard_hand(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.deal_to(5)
        >>> player.discard_hand()
        >>> player.hand
        []
        """
        self.hand = [] #removes all cards from the players hand
        

    @property
    def wins(self):
        return self.win_counter
        

    @property
    def ties(self):
        return self.tie_counter
        

    @property
    def losses(self):
        return self.loss_counter
        

    def record_win(self):
        """
        >>> player = Player(None, None)
        >>> player.record_win()
        >>> player.wins
        1
        """
        self.win_counter += 1
        

    def record_loss(self):
        """
        >>> player = Player(None, None)
        >>> player.record_loss()
        >>> player.losses
        1
        """
        self.loss_counter += 1
        

    def record_tie(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.ties
        1
        """
        self.tie_counter += 1
        

    def reset_stats(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.reset_stats()
        >>> player.ties
        0
        >>> player.wins
        0
        >>> player.losses
        0
        """
        self.win_counter = 0
        self.loss_counter = 0
        self.tie_counter = 0
        

    def __repr__(self):
        """
        Output should include the player name, their current hand, and their wins/ties/losses in that order
        >>> player = Player("Eric", None)
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.record_win()
        >>> player
        Eric: [] 2/0/1
        """
        return "{}: {} {}/{}/{}".format(self.name, self.hand, self.win_counter, self.tie_counter, self.loss_counter)
        return ""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
