from conditions import Condition

class BracketsBalancer(object):
    def Balance(brackets):        
        if Condition.BracketsAreBalanced(brackets):
            return "OK"
        elif Condition.BracketsAreUnbalanced(brackets):
            return "FAIL"
        else:
            return ""