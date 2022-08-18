#conditional statement in puython

name= input("what is your name?")
age= int(input("what is your age?"))

if age < 0:
    print(f"invalid age")
elif age==10:
    print(f"dear {name}, Your ticket price is: 100")
elif age>10:
    print(f"dear {name}, Your ticket price is: 150")
else:
    print(f"dear {name},Your ticket price is: 50")  

