class BracketsBalancer(object):
    def Balance(brackets):        
        if brackets.startswith("[") and brackets.endswith("]"):
            return "OK"
        elif brackets == "][":
            return "FAIL"
        else:
            return ""