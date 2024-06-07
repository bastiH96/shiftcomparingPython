from data_access.person_data_access import PersonDataAccess
from services.excelCalculator import ExcelService
from datetime import date

class ComparisonHandler:
    
    def create_comparison_dialog(self):
        try:
            print("Which persons do you want to compare?")
            persons = self.get_persons_for_comparison()
            print("Which calendar year do you want?")
            year = self.get_year_for_comparison()
            ExcelService(persons, year).create_excel_comparison_table()
            print("Calendar was created!")
        except Exception as e:
            print(e)


    def get_persons_for_comparison(self):
        persons = PersonDataAccess().get_all_persons()
        selected_persons = []
        add_more_persons = True
        
        while add_more_persons:
            possible_persons = []
            persons_str = ""
            for person in persons:
                if person.shiftsystem_id != None:
                    possible_persons.append(person)
                    persons_str += f"{persons.index(person) + 1} - {person.name}\n"
            print(persons_str)
            choice = int(input())
            selected_persons.append(possible_persons[choice - 1])
            possible_persons.pop(choice - 1)
            persons = possible_persons
            if len(persons) != 0:
                print("Do you want to add another person? (y/n)")
                choice = input()
                if choice == "y":
                    print("Add another person!")
                else:
                    add_more_persons = False
            else:
                add_more_persons = False
        return selected_persons


    def get_year_for_comparison(self):
        year = int(input())
        if 1900 <= year <= 2090:
            return year
        