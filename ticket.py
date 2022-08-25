#conditional statement in puython
'''
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
'''

#ask two integer numbers with user and function should return their addition:
'''
first_number=int(input("please enter a number="))
second_number=int(input("please enter another number="))

def hello(first_number,second_number):
    addition=(first_number)+(second_number) 
    return addition

print("addition is=",hello(first_number,second_number))
'''

brand_name=input("enter brand name:")
model_name=input("enter model name:")
price=input("enter price:")
def laptop_specs(brand,model,price):
    print(f"The laptop is {brand},{model} @Rs. {price}")
    my_laptop=laptop_spes(brand,model,price)
    print(my_laptop)
