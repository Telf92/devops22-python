# A

X = 1 
Y = 4 
addresses = {"Adam": "Ormvägen 5", 
            "Bella": "Klockgatan 1", 
            "Cornelia": "Vikingagatan 3"} 
cars = ["Volvo", "Opel", "BMW"] 
numbers1 = {1, 2, 3, X, 6} 
numbers2 = {Y, 2, 3, 4, 7} 

def q1():
    print(type(X)) # int
    print(type(Y)) # int

def q2():
    print(type(addresses)) # dict

def q3():
    print(addresses["Bella"])

def q4():
    # Vi lägger till ett nytt key:value par i addresses 
    addresses["Daniel"] = "Prinsgränd 2"
    print(addresses["Daniel"])

def q5():
    l = len(addresses)
    print(l)
    # 5.1
    name = sorted(addresses)[-1]
    print(addresses[name])
    # 5.2
    addresses_reversed = { v: k for k, v in addresses.items() }
    address = sorted(addresses_reversed)[0]
    print(addresses_reversed[address])

def q6():
    print(type(cars)) # list

def q7():
    print(cars[X])

def q8():
    print(cars[Y])

def q9():
    cars.sort()
    print(cars[0]) # BMW

def q10():
    cars_2 = cars
    cars_3 = []
    cars_3.extend(cars)
    cars.append("Saab")
    
    print(cars)
    print(cars_2)
    print(cars_3)
    cars.extend(cars)
    cars.sort(reverse=True)
    print(cars)
    unique_cars = list(set(cars))
    print(unique_cars)

def q11():
    print(type(numbers1)) # set
    print(type(numbers2)) # set

def q12():
    print((numbers1)) # set
    print((numbers2)) # set

def q13():
    print(numbers1.intersection(numbers2))

def q14():
    print(numbers1.union(numbers2))

def q15():
    print(numbers1.symmetric_difference(numbers2))

if __name__ == "__main__":
    print("Q1")
    q1()
    print("Q2")
    q2()
    print("Q3")
    q3()
    print("Q4")
    q4()
    print("Q5")
    q5()
    print("Q6")
    q6()
    print("Q7")
    q7()
    #print("Q8")
    #q8()
    print("Q9")
    q9()
    print("Q10")
    q10()
    print("Q11")
    q11()
    print("Q12")
    q12()
    print("Q13")
    q13()
    print("Q14")
    q14()
    print("Q15")
    q15()

# B
from operator import itemgetter
persons = []

name_person_one = input("Please enter name for person 1:").lower()
age_person_one = int(input("Please enter age for person 1:"))
size_person_one = float(input("Please enter shoe size of person 1:"))
person_one = (name_person_one, age_person_one, size_person_one)
persons.append(person_one)

name_person_two = input("Please enter name for person 2:").lower()
age_person_two = int(input("Please enter age for person 2:"))
size_person_two = float(input("Please enter shoe size of person 2:"))
person_two = (name_person_two, age_person_two, size_person_two)
persons.append(person_two)

name_person_three = input("Please enter name for person 3:").lower()
age_person_three = int(input("Please enter age for person 3:"))
size_person_three = float(input("Please enter shoe size of person 3:"))
person_three = (name_person_three, age_person_three, size_person_three)
persons.append(person_three)

sorted_shoe_size = sorted(persons, key = itemgetter(1))
sorted_age = sorted(persons, key = itemgetter(2))

oldest = sorted_age[2]
median_size = sorted_shoe_size[1]

print(f"Name: {oldest[0].capitalize()}, Shoe size: {oldest[2]}")
print(f"Name: {median_size[0].capitalize()}, Age: {median_size[1]}")

searches = {
    "age":  {
        str(age_person_one): person_one,
        str(age_person_two): person_two,
        str(age_person_three): person_three
    },
    "shoe": {},
    "name": {}
}

prop, value = input("Enter prop value: ").split(" ")
print(searches[prop][value])