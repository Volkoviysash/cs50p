class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")        #if there is not name, return an error!                    
        self.name = name        
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    #Getter
    @property
    def house(self):
        return self.house

    #Setter
    @house.setter
    def house(self, house):
        if house in ["Gryffindor", "Revenclaw", "Lolaland"]:
            self.house = house


def main():
    student = get_student()        
    print(student)


def get_student():        
    name = input("Name: ")
    house = input("House: ")     
    return Student(name, house)

        
if __name__ == "__main__":
    main()