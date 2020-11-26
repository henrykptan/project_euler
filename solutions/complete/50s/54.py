"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example,
a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a
pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the
next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
import time
from collections import Counter

start = time.time()

# we obtain the hands from another file, noting that they come in a list of both hands (10 cards)
hands = (line.split() for line in open('../../resources/poker.txt'))

values = {r: i for i, r in
          enumerate('23456789TJQKA', 2)}  # then the values for each card, starting from 2, Ace high, in a dictionary

# we will rank straight as 4, flush 5, straight flush 8, royal flush 9
ranks = {(1, 1, 1, 1, 1): 0, (2, 1, 1, 1): 1, (2, 2, 1): 2, (3, 1, 1): 3, (3, 2): 6, (4, 1): 7}

# we create the set of straights, in ranked order
straights = [(14, 5, 4, 3, 2)] + [tuple([j for j in range(i, i + 5)][::-1]) for i in range(2, 11)]


def is_a_straight(nums):
    if nums in straights:
        return True
    else:
        return False


def is_a_flush(hand):
    if len(set(card[1] for card in hand)) == 1:
        return True
    else:
        return False


# for all hands but straights and flushes we only need to keep track of multiples of card numbers
# we will score all of the hands from 1 (high card) to 10 (royal flush)


def p1_wins(h1, h2):  # deal with ties in a sec
    h = [h1, h2]
    scores = [0, 0]
    card_values = [0, 0]
    pairs = [[], []]
    # we run through the hand score function for each hand, recording the scores in a list
    for j in range(2):
        # just the values of the cards (no suits), in desc order
        card_values[j] = tuple(sorted([values[i[0]] for i in h[j]], reverse=True))
        # produces the pairs structure in two tuples
        pair = zip(*sorted(((v, values[k]) for k, v in Counter(x[0] for x in h[j]).items()), reverse=True))
        for p in pair:
            pairs[j].append(p)
        scores[j] = ranks[pairs[j][0]]  # will override if flush or straight

        # then straights
        if is_a_straight(card_values[j]):
            scores[j] = 4
        if is_a_flush(h[j]):
            scores[j] = 5
            if is_a_straight(card_values[j]):
                scores[j] = 8
                if card_values[j][4] == 14:
                    scores[j] = 9
        scores[j] = scores[j]
    # then we take a count on the number of P1 wins
    if scores[0] > scores[1]:
        return True
    if scores[1] > scores[0]:
        return False
    elif scores[0] == scores[1]:  # now we deal with ties (note a true tie means no P1 win)
        if card_values[0] == card_values[1]:
            return False
        elif scores[0] == 4 or scores[0] == 8:  # straight/straight flush
            # we look at the second highest card (as low card ace straight will mess up stuff)
            if (card_values[1][1]) >= (card_values[0][1]):
                return False
            else:
                return True

        elif scores[0] == 5:  # flush
            # only need to look at highest card (can only have a flush in one suit)
            if (card_values[1][0]) >= (card_values[0][0]):
                return False
            i = 0
            while i <= 4:
                if (card_values[1][i]) >= (card_values[0][i]):
                    return False
                elif pairs[1][1][i] < pairs[0][1][i]:
                    return True
                i += 1

        else:  # multiples
            if pairs[1][1] == pairs[0][1]:  # if the hands are exactly the same
                return False
            else:
                i = 0
                while i <= 4:
                    if pairs[1][1][i] > pairs[0][1][i]:
                        return False
                        break
                    elif pairs[1][1][i] < pairs[0][1][i]:
                        return True
                        break
                    i += 1


if __name__ == '__main__':
    print("P1 wins", sum(p1_wins(hand[:5], hand[5:]) for hand in hands))
