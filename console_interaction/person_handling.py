from console_interaction.exceptions import InvalidAliasLengthException, InvalidDateException
from data_access.shiftsystem_data_access import ShiftsystemDataAccess
import re
from datetime import date
from models.person import Person
from data_access.person_data_access import PersonDataAccess

class PersonHandler:
    def create_person_dialog(self):
        try:
            print("Enter the name of the person:")
            name = self.get_person_name()
            print("Enter the alias of the person (max. 3 letters):")
            alias = self.get_person_alias()
            print("In which shiftsystem is the person working?")
            shiftsystem_id = self.get_person_shiftsystem().id
            print("Enter the startdate of the shiftpattern for this person\nExcepted pattern:\n'01.01.2024'\n'1.1.2024'")
            shiftpattern_start_date = self.get_person_shiftsystem_start_date()
            PersonDataAccess().insert_person(Person(name, alias, shiftpattern_start_date, shiftsystem_id=shiftsystem_id))
            print("Person successfully created!")
            
        except Exception as e:
            print(e)
        
        
    def get_person_name(self):
        name = input()
        return name
    
    def get_person_alias(self):
        alias = input()
        if len(alias) <= 3:
            return alias
        else:
            raise InvalidAliasLengthException("Abort! Due invalid length of the alias")
        
    def get_person_shiftsystem(self):
        shiftsystems = ShiftsystemDataAccess().get_all_shiftsystems()
        shiftsystem_str = ""
        for x in range(0, len(shiftsystems)):
            shiftsystem_str += f"{x + 1} - {shiftsystems[x].name}\n"
        print(shiftsystem_str)
        choice = int(input())
        return shiftsystems[choice-1]
    
    def get_person_shiftsystem_start_date(self):
        regex_pattern = r"^\d{1,2}\.\d{1,2}\.\d{4}$"
        start_date = input()
        if re.match(regex_pattern, start_date) != None:
            date_parts = start_date.split(".")
            return date(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
        else:
            raise InvalidDateException("Abort! Due invalid date or date pattern.")