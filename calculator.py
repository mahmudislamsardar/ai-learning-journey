#project calculator


x=float(input("enter any number : "))
operator=input("enter an operator (+,-,*,/) : ")
y=float(input("enter any  number :"))
if operator == "+":
    print(f"the addition is :{x + y} ")
elif operator=="-":
    print(f"the subtraction is :{x - y}")
elif operator=="*":
    print(f"the multiplication is :{x *y}")
elif operator=="/":
    print(f"the fraction is : {x/y}")
elif operator =="**":
    print(f"{x ** y}")
elif operator=="%":
    print(f"{x%y}")
