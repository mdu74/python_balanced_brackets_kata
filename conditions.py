class Condition(object):
    def BracketsAreBalanced(brackets):
        return brackets.startswith("[") and brackets.endswith("]")
    
    def BracketsAreUnbalanced(brackets):
        return brackets.startswith("]") and brackets.endswith("[") or brackets.startswith("[") and brackets.endswith("[")