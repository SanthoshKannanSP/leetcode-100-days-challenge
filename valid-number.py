class Solution:
    def isNumber(self, s: str) -> bool:
        transitions = {
            "Start": {"digit":"Integer","sign":"Sign","dot":"Dot"},
            "Sign": {"digit":"Integer","dot":"Dot"},
            "Integer": {"digit":"Integer","dot":"Fraction","exp":"Exponent"},
            "Dot": {"digit":"Fraction"},
            "Fraction": {"digit":"Fraction","exp":"Exponent"},
            "Exponent": {"digit":"Exp_number","sign":"Exp_sign"},
            "Exp_sign": {"digit":"Exp_number"},
            "Exp_number": {"digit":"Exp_number"}
        }
        
        final_state = {"Integer","Fraction","Exp_number"}

        curr_state = "Start"

        def get_char_type(char):
            if char.isdigit():
                return "digit"
            if char in "+-":
                return "sign"
            if char in "eE":
                return "exp"
            if char==".":
                return "dot"
            return "other"

        for i in s:
            char_type = get_char_type(i)
            if char_type not in transitions[curr_state]:
                return False
            curr_state = transitions[curr_state][char_type]
        
        if curr_state in final_state:
            return True
        return False