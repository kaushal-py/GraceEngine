from condition import Condition
from card import Card

class LogicalCondition():

    def __init__(self, left_condition:Condition, right_condition:Condition, logical_condition:str, card_number:int):
        
        self.left_condition = left_condition
        self.right_condition = right_condition

        if self.verify_condition(logical_condition):
            card_id = "logical_condition"
            super(LogicalCondition, self).__init__(card_id, logical_condition, card_number)
        else:
            return None
    
    def verify_condition(self, logical_condition):
        for condition in ['AND','OR']:
            if condition == logical_condition:
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
        self.card_dict["internal_dependants"] = []
        self.card_dict["external_dependants"] = None
        self.card_dict["children"] = []

    def set_left_condition(self, card_number:int):
        # TODO: Having problem, condition or expression, if condition the logical or relational condition
        pass

    def set_right_condition(self, condition:Condition, card_number:int):
        # TODO: Having problem, condition or expression, if condition the logical or relational condition
        pass

if __name__ == "__main__":
    pass