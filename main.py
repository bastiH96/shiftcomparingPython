from data_access.person_data_access import PersonDataAccess
from data_access.shiftsystem_data_access import ShiftsystemDataAccess
from models.person import Person
from models.shiftsystem import Shiftsystem
from datetime import date
from services.excelCalculator import ExcelService

if __name__ == "__main__":
    
    shiftsystem = Shiftsystem("Erik's System", ["F12", "N12", "-", "F12", "N12", "-", "-", "-"])
    # person = Person("Sebastian", "Seb", date(2003, 10, 13), shiftsystem_id=1, id=2)
    person_db = PersonDataAccess("shiftcomparingDb.sqlite")
    shiftsystem_db = ShiftsystemDataAccess("shiftcomparingDb.sqlite")
    
    person_db.create_person_table()
    shiftsystem_db.create_shiftsystem_table()
    
    # person_db.update_person(person)
    
    # persons = person_db.get_all_persons()
    persons = []
    persons.append(person_db.get_one_person(1))
    excel = ExcelService(persons, 2022)
    excel.create_excel_comparison_table()
    