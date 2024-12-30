class Student:
    
    def __init__(self, name, age, list_of_grades):
        self.name = name
        self.age = age
        self.list_of_grades = list_of_grades

    def display_info(self):        
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grades: {self.list_of_grades}')

    def calc_avg_grades(self):
        return sum(self.list_of_grades) / len(self.list_of_grades)
    
def main():
    obj1 = Student("Bishoy", 23, [50, 60, 70])
    obj1.display_info()
    print(f"Average of Grades = {obj1.calc_avg_grades()}")
    
main()