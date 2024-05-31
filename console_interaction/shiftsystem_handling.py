import re
from data_access.shiftsystem_data_access import ShiftsystemDataAccess
from models.shiftsystem import Shiftsystem
from console_interaction.exceptions import WrongTermException

class ShiftsystemHandler:
    
    def create_shiftsystem_dialog(self):
        print("Enter a shiftpattern. Type 'done' when you finished the pattern.\nValid terms: 'F12', 'N12', 'F', 'S', 'N', '-'")
        pattern = self.get_pattern()
        print("The following pattern have been collected")
        pattern_str = ""
        for term in pattern:
            pattern_str += term + " "
        print("What's the name of the pattern?")       
        self.create_shiftsystem(input(), pattern)
            
    def get_pattern(self):
        pattern = []
        term = self.validate_term(input())
        while term != "done":
            pattern.append(term)
            term = self.validate_term(input())
        return pattern
    
    def create_shiftsystem(self, name: str, pattern: list):
        shiftsystem = Shiftsystem(name, pattern)
        ShiftsystemDataAccess().insert_shiftsystem(shiftsystem)
        
            
    def validate_term(self, term: str):
        regex_pattern = re.compile(r"^(F12|N12|F|S|N|-|done)$")
        try:
            if re.match(regex_pattern, term) != None:
                return term
            else:
                raise WrongTermException()
        except WrongTermException:
            print("Abort! You entered a wrong term.")
            