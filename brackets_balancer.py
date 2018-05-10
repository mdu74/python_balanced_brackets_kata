class BracketsBalancer(object):
    def Balance(brackets):        
        if brackets.startswith("[") and brackets.endswith("]"):
            return "OK"
        elif brackets.startswith("]") and brackets.endswith("[") or brackets.startswith("[") and brackets.endswith("["):
            return "FAIL"
        else:
            return ""