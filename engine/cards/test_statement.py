from card import Card

class TestStatement(Card):
    def __init__(self, card_number:int):
        card_id = "test_statement"
        card_type = [True, True, False, False, False, True, 0]
        super(TestStatement,self).__init__(card_id,card_type,card_number)