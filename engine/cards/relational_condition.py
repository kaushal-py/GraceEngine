from condition import Condition
from expression import Expression
from sticker import Sticker

class RelationalCondition(Condition):
    
    def __init__(self, left_expression:list, relatinoal_condition:tuple, right_expression:list, card_number:int, card_number_l:int, card_number_r:int):
        
        self.left_expression = Expression(left_expression,card_number_l)
        self.right_expression = Expression(right_expression,card_number_r)
        (sticker_type, sticker_value) = relatinoal_condition
        condition = Sticker(sticker_type, sticker_value)

        card_id = "relational_condition"
        super(RelationalCondition, self).__init__(card_id, condition, card_number)
        self.code = ""

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_logic"
        left_expression = {
            "val_type":"internal_dependant",
            "dependant" : self.left_expression.generate_card()
        }
        sticker_text = {
            "val_type": "sticker",
            "sticker_name": self.condition.sticker_type,
            "sticker_value": self.condition.sticker_value
        }
        right_expression = {
            "val_type":"internal_dependant",
            "dependant" : self.right_expression.generate_card()
        }
        self.card_dict["display"] = [left_expression, sticker_text, right_expression]
        self.card_dict["external_dependant"] = None
        self.card_dict["children"] = []
        
        return self.card_dict

    def generate_code(self):
        self.code = ""
        if self.left_expression.generate_code():
            left_expression_string = self.left_expression.generate_code()
        else:
            left_expression_string = " None"
        if self.right_expression.generate_code():
            right_expression_string = self.right_expression.generate_code()
        else:
            right_expression_string = " None"
        self.code = left_expression_string + " " + self.condition.sticker_value + right_expression_string
        return self.code

if __name__ == "__main__":
    test_card = RelationalCondition([("number", "3"),("operator", "+"),("number", "3")],("condition",">"), [("number", "5"),("operator", "-"),("number", "2")], 0, 1, 2)
    print(test_card.generate_card())
    print(test_card.generate_code())