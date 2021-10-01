import random
# winnig_no=10
# print("Enter the number between 1 to 100 : ")
# user_guss=int(int(input("Enter the number : ")))
# count=1
# game_over=False
# while not game_over:
#     if winnig_no==user_guss:
#         print("Congratulation !!!! You have guess correct.")
#         count+=1
#         game_over=True
#     else:
#         if winnig_no<user_guss:
#             print("Guess too low !!")
#             user_guss=int(input("Enter the number : "))
        
#         elif(user_guss>winnig_no):
#             print("Guess too High !!")
#             user_guss=int(input("Enter the number : "))


num=random.randint(1,100)
guess=None
while guess!=num:
    guess=int(input("Enter the number : "))
    if guess==num:
        print("congratulation!!! You win")
    else:
        if (num<guess):
            print("You guess high, please try again..." )
        else:
            print('you guess low, please try again...')