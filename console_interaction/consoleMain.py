from console_interaction.shiftsystem_handling import ShiftsystemHandler
from console_interaction.person_handling import PersonHandler
from console_interaction.comparison_handling import ComparisonHandler

def run_main():
    print("""
        What do you want to do?
        1 - Create a shiftsystem
        2 - Create a person
        3 - Create a comparison table
        4 - Exit
        """)
    validate_input()
    
def validate_input():
    choice = input()
    if choice == "1":
        ShiftsystemHandler().create_shiftsystem_dialog()
    if choice == "2":
        PersonHandler().create_person_dialog()
    if choice == "3":
        ComparisonHandler().create_comparison_dialog()
    
        