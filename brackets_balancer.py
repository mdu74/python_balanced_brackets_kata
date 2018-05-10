class BracketsBalancer(object):
    def Balance(brackets):        
        if brackets.startswith("[") and brackets.endswith("]"):
            return "OK"
        else:
            return ""