from condition import Condition
from expression import Expression

class RelationalCondition(Condition):
    
    def __init__(self, left_expression:Expression, right_expression:Expression, relational_condition):

        self.left_expression = left_expression
        self.right_expression = right_expression

        if self.verify_condition(relational_condition):
            card_id = "relational_condition"
            card_type=[True,True,True,False,0,False] #TODO: DO THIS
            super(RelationalCondition, self).__init__(card_id, card_type, relational_condition)
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