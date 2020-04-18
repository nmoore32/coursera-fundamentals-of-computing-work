##
# This is from an assigment for An Introduction to Interactive Programming in Python (Part 2) on Coursera
# We were provided with some constants, global variables, and most of the card class. I'll indicate which
# bits of code were from the starting template.
#

from random import choice, shuffle
import sys
import pygame as pg

# Define constants
CARD_SIZE = (72, 96)  # From template
C_GAPSIZE = 10  # Horizontal gap between cards
WIDTH = 1000  # Screen width
HEIGHT = 560  # Screen height
MARGIN = 25
B_GAPSIZE = 25  # Vertical gap between buttons
B_WIDTH = 100  # Button width
B_HEIGHT = 50  # Button height
SMALL_FONT = 28
LARGE_FONT = 42

CYAN = (0, 255, 255)
GRAY = (211, 211, 211)
BLACK = (0, 0, 0)

# Initialize global variables (These are from template)
in_play = False
outcome = ''
score = 0

# These tuples and dictionary are from template
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card():
    '''Everything in the Card class is from the template except for self.exposed, set_exposed(),
    and some modifications based on the self.exposed attribute to draw()'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.exposed = True  # Indicates whether card is face up

    def __str__(self):
        return f"{self.suit}{self.rank}"

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, screen, card_images, card_back, pos):
        # Draw the card if face up
        if self.exposed:
            card_loc = (CARD_SIZE[0] * RANKS.index(self.rank),
                        CARD_SIZE[1] * SUITS.index(self.suit))
            # Here I'm cropping a tiled image of a full set of cards (minus jokers)
            screen.blit(card_images, (pos),
                        (card_loc[0], card_loc[1], CARD_SIZE[0], CARD_SIZE[1]))
        # Otherwise draw the card back
        else:
            # Here I'm cropping a tiled image of two different card backs
            screen.blit(card_back, (pos), (0, 0, CARD_SIZE[0], CARD_SIZE[1]))

    def set_exposed(self, boolean):
        '''Set the self.exposed attribute to True or False'''
        self.exposed = boolean


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return_string = 'Hand contains'
        for card in self.cards:
            return_string += f" {str(card)}"
        return return_string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        ''' Return the value of the Hand'''
        value = 0
        has_ace = False
        # Add the value for each card (based on rank) and track if the Hand has an ace
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank == 'A':
                has_ace = True
        # If the Hand has an ace and scoring it valued at 11 won't bust, then score it as 11
        if has_ace == True and value < 12:
            # Only adding ten because ace was scored as value 1 in the above for loop
            value += 10
        return value

    def draw(self, screen, card_images, card_back, pos):
        # Create index to shift successive card positions
        i = 0
        for card in self.cards:
            card.draw(screen, card_images, card_back, [
                      pos[0] + i * (CARD_SIZE[0] + C_GAPSIZE), pos[1]])
            i += 1

    def set_exposed(self):
        self.cards[0].set_exposed(True)

    def discard(self):
        self.cards = []


class Deck:
    def __init__(self):
        self.deck = []

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return_string = 'Deck contains'
        for card in self.deck:
            return_string += f" {str(card)}"
        return return_string

    def shuffle(self):
        shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


def deal(dealer_hand, player_hand):
    '''Shuffle the deck and deal two cards to each player'''
    global in_play, score, outcome
    # Player counts as losing hand if they deal a new one before finishing current hand
    if in_play:
        score -= 1
    # Create/replenish deck, shuffle, reset hands, and reset outcome message
    deck = Deck()
    deck.shuffle()
    dealer_hand.discard()
    player_hand.discard()
    outcome = ''

    # Deal cards two cards to player and dealer
    player_hand.add_card(deck.deal_card())
    # Set the dealers first card to face down
    card1 = deck.deal_card()
    card1.set_exposed(False)
    dealer_hand.add_card(card1)
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    # Indicate that we are in play
    in_play = True

    # Return the deck since it will be used to deal additional cards until the round ends
    return deck


def hit(deck, dealer_hand, player_hand):
    global score, in_play, outcome
    # Hit button doesn't do anything if not in play (need to press deal for new round)
    if in_play:
        player_hand.add_card(deck.deal_card())
        # If player busts with the new card, display outcome, change score, end round, display dealers hand
        if player_hand.get_value() > 21:
            outcome = 'Player busted'
            score -= 1
            in_play = False
            dealer_hand.set_exposed()


def stand(deck, dealer_hand, player_hand):
    global score, in_play, outcome
    # Stand button doesn't do anything if not in play (need to press deal for new round)
    if in_play:
        # Show the dealers hand and have the dealer hit until their score is >= 17
        dealer_hand.set_exposed()
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        # Determine the outcome of the hand
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer busted'
            score += 1
        # Dealer wins ties
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = 'Dealer wins'
            score -= 1
        else:
            outcome = 'Player wins'
            score += 1
    # End round regardless of outcome
    in_play = False


def draw(screen, b_texts, player_hand, dealer_hand, card_images, card_back, large_font):
    global score
    # Draw buttons
    pg.draw.rect(screen, GRAY, (MARGIN, MARGIN, B_WIDTH, B_HEIGHT))
    pg.draw.rect(screen, GRAY, (MARGIN, MARGIN +
                                B_HEIGHT + B_GAPSIZE, B_WIDTH, B_HEIGHT))
    pg.draw.rect(screen, GRAY, (MARGIN, MARGIN + 2 *
                                (B_HEIGHT + B_GAPSIZE), B_WIDTH, B_HEIGHT))

    # Draw button text
    screen.blit(b_texts[0], (int(MARGIN + B_WIDTH / 2 -
                                 b_texts[0].get_rect().width /
                                 2), int(MARGIN + B_HEIGHT / 2
                                         - b_texts[0].get_rect().height / 2)))
    screen.blit(b_texts[1], (int(MARGIN + B_WIDTH / 2 -
                                 b_texts[1].get_rect().width /
                                 2), int(MARGIN + B_HEIGHT / 2
                                         - b_texts[1].get_rect().height / 2 + B_HEIGHT + B_GAPSIZE)))
    screen.blit(b_texts[2], (int(MARGIN + B_WIDTH / 2 -
                                 b_texts[2].get_rect().width /
                                 2), int(MARGIN + B_HEIGHT / 2
                                         - b_texts[2].get_rect().height / 2 + 2 * (B_HEIGHT + B_GAPSIZE))))

    # Draw cards
    player_hand.draw(screen, card_images, card_back, [
                     2 * (MARGIN + B_WIDTH), HEIGHT - 2 * CARD_SIZE[1]])
    dealer_hand.draw(screen, card_images, card_back, [
                     2 * (MARGIN + B_WIDTH), 2 * MARGIN])

    # Draw score
    score_text = large_font.render(f"Score: {score}", True, BLACK)
    screen.blit(
        score_text, (WIDTH - score_text.get_rect().width - MARGIN, MARGIN))

    # Draw outcome text
    outcome_text = large_font.render(outcome, True, BLACK)
    screen.blit(
        outcome_text, (WIDTH - outcome_text.get_rect().width - MARGIN, HEIGHT - 3 * CARD_SIZE[1]))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Blackjack')

    # Initialize hands, deck, and deal two cards each
    player_hand = Hand()
    dealer_hand = Hand()
    deck = deal(dealer_hand, player_hand)

    # Create deal, hit, and stand buttons (they don't need to be drawn here, but even an assignment
    # statement causes them to be drawn)
    deal_button = pg.draw.rect(
        screen, GRAY, (MARGIN, MARGIN, B_WIDTH, B_HEIGHT))
    hit_button = pg.draw.rect(screen, GRAY, (MARGIN, MARGIN +
                                             B_HEIGHT + B_GAPSIZE, B_WIDTH, B_HEIGHT))
    stand_button = pg.draw.rect(screen, GRAY, (MARGIN, MARGIN + 2 *
                                               (B_HEIGHT + B_GAPSIZE), B_WIDTH, B_HEIGHT))

    # Create text for deal, hit, and stand buttons
    font = pg.font.Font('freesansbold.ttf', SMALL_FONT)
    b_texts = []
    b_texts.append(font.render('Deal', True, BLACK))
    b_texts.append(font.render('Hit', True, BLACK))
    b_texts.append(font.render('Stand', True, BLACK))

    # Create font for scoring and outcome messages
    large_font = pg.font.Font('freesansbold.ttf', LARGE_FONT)

    # Load card images
    card_images = pg.image.load('cards.png')
    card_back = pg.image.load('card_back.png')

    while True:

        # Draw screen
        screen.fill(CYAN)
        draw(screen, b_texts, player_hand, dealer_hand,
             card_images, card_back, large_font)

        # Reset click position variables
        mouse_x = None
        mouse_y = None

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONUP:
                coords = event.pos
                if deal_button.collidepoint(coords):
                    deal(dealer_hand, player_hand)
                elif hit_button.collidepoint(coords):
                    hit(deck, dealer_hand, player_hand)
                elif stand_button.collidepoint(coords):
                    stand(deck, dealer_hand, player_hand)

        pg.display.update()


if __name__ == '__main__':
    main()
