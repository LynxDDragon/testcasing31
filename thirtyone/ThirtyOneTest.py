import unittest
from ThirtyOne import Cards, Deck, Player, Game

class TestCards(unittest.TestCase):

    def test_Deck(self):
        Deck_test = Deck()

        Deck_test.build()
        self.assertNotIn('2 of Hearts', Deck_test.cards)
        self.assertNotEqual('2 of Hearts', Deck_test.cards)

    def test_deck(self):
        test_deckAmount = Deck()

        test_deckAmount.__init__()
        self.assertTrue(test_deckAmount.cards)

    def test_cards(self):
        test_cards = Deck()

        test_cards.__init__()
        self.assertIn('2 of Hearts', test_cards.cards)


        
if __name__ == '__main__':
    unittest.main()