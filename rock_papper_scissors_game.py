import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
c = int(input())
a = [rock,paper,scissors]
print(a[c])
b = random.randint(0,2)
print("computer choice\n" + a[b])
# print(f"computer choice\n {b}" )
if c == 0 and b == 2:
    print("You win")
elif c == 1 and b == 0:
    print("You win")
elif c == 2 and b == 1:
    print("You win")
elif c == b:
    print("its a draw")
else:
    print("You lose")