from conditions import BracketsAre

class BracketsBalancer:
    def Balance(brackets):        
        if BracketsAre.Balanced(brackets):
            return "OK"
        elif BracketsAre.Unbalanced(brackets):
            return "FAIL"
        else:
            return ""