scissors="""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
paper="""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
rock="""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
choice_1=int(input("what do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
if choice_1==0:
    print(rock)
elif choice_1==1:
    print (paper)
elif choice_1==2:
    print(scissors)
print("computer chose:")
import random
choice_2=random.randint(0,2)
if choice_2==0:
    print(rock)
elif choice_2==1:
    print(paper)
elif choice_2==2:
    print(scissors)
if choice_1==0:
   if choice_2==0:
       print("tie")
if choice_1==1:
    if choice_2==1:
        print("tie")
if choice_1==2:
    if choice_2==2:
        print("tie")
if choice_1==0:
    if choice_2==1:
        print("You lose")
if choice_1==0:
    if choice_2==2:
        print("You win")
if choice_1==1:
    if choice_2==0:
        print("You win")
if choice_1==1:
    if choice_2==2:
        print("You lose")
if choice_1==2:
    if choice_2==0:
        print("You lose")
if choice_1==2:
    if choice_2==1:
        print("You win")



