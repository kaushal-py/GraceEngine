from condition import Condition
from expression import Expression

class RelationalCondition(Condition):
    
    def __init__(self, relational_condition:str, card_number:int):
        
        #  "count >  3"
        self.left_expression = Expression()
        self.right_expression = Expression()

        if self.verify_condition(relational_condition):
            card_id = "relational_condition"
            super(RelationalCondition, self).__init__(card_id, relational_condition, card_number)
        else:
            return None
    
    def verify_condition(self, relational_condition):
        '''
        Check if the condition specified is a defined condition
        '''
        for condition in ['==','>', '>=', '<', '<=']:
            if condition == relational_condition:
                return True
        return False

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_logic"
        left_expression = {
            "val_type":"internal_dependant",
        }
        sticker_text = {
            "val_type": "sticker",
            "sticker_name": self.condition.sticker_type,
            "sticker_value": self.condition.sticker_value
        }
        right_expression = {
            "val_type":"internal_dependant",
        }
        self.card_dict["display"] = [left_expression, sticker_text, right_expression]
        self.card_dict["internal_dependant"] = [, self.right_expression.generate_card()]
        self.card_dict["external_dependant"] = None
        self.card_dict["children"] = []
        
        return self.card_dict

    def set_left_expression(self, expression:str, card_number:int):
        self.left_expression = Expression(expression, card_number)
        internal_dependant = {
            "val_type" : "internal_dependant",
            "dependant" : self.left_expression.generate_card()
        }
        self.card_dict["display"][0] = internal_dependant
        print(self.right_expression.expression[0].sticker_value)

    def set_right_expression(self, expression:str, card_number:int):
        self.right_expression = Expression(expression, card_number)
        internal_dependant = {
            "val_type" : "internal_dependant",
            "dependant" : self.right_expression.generate_card()
        }
        self.card_dict["display"][2] = internal_dependant

if __name__ == "__main__":
    test_card = RelationalCondition('==', 0)
    test_card.generate_card()

    test_card.set_left_expression("1", 1)
    test_card.set_right_expression("+ 2", 2)
    print(test_card.left_expression, test_card.right_expression)
    for item in test_card.left_expression.expression:
        print(item.sticker_value, end=' ')
    print(test_card.condition.sticker_value, end=' ')
    for item in test_card.right_expression.expression:
        print(item.sticker_value, end=' ')
    print()
    print(test_card.generate_card())

    #TODO: some error idk what, how