from condition import Condition

class LogicalCondition():

    def __init__(self, left_condition, right_condition, logical_condition):
        
        self.left_condition = left_condition
        self.right_condition = right_condition

        if self.verify_condition(logical_condition):
            card_id = "logical_condition"
            card_type=[True,True,True,False,0,False] #TODO: DO THIS
            super(LogicalCondition, self).__init__(card_id, card_type, logical_condition)
        else:
            return None
    
    def verify_condition(self, logical_condition):
        for condition in ['AND','OR']:
            if condition == logical_condition:
                return True
        return False
