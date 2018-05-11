class BracketsAre(object):
    def Balanced(brackets):
        return brackets.startswith("[") and brackets.endswith("]")
    
    def Unbalanced(brackets):
        return brackets.startswith("]") and brackets.endswith("[") or brackets.startswith("[") and brackets.endswith("[")