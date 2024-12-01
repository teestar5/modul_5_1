class House:
        def __init__(self, name, number_of_floors):
            self.name = name
            self.number_of_floors = number_of_floors

        def go_to(self, new_floor):
            if new_floor < 1 or new_floor > self.number_of_floors:  #Если же new_floor больше чем self.number_of_floors или меньше 1
                print("Такого этажа не существует")                  #, то вывести строку "Такого этажа не существует".
            else:
                for i in range(1, new_floor + 1):
                    print(i)


h1 = House('ЖК Горский', 9)
h2 = House('Домик в деревне', 15)
h1.go_to(10)
h2.go_to(6)
