import random
y='yes'
while y=='yes':
    choice=input("Enter snake or water or gun")
    system_choice=random.choice(['snake','water','gun'])
    print(f"you choice :{choice}")
    print(f"computer choice : {system_choice}")
    if choice==system_choice:
        print("it's a tie")
    elif system_choice=='water' and choice=='snake' or system_choice=='snake' and choice=='gun' or system_choice=='gun' and choice=='water' :
        print("you won")
    else:
        print("you lose")
    y=input("Do you want to play more yes or no :")



