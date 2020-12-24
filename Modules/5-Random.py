'''
"""
1 Random -- Return 0 to 1 , Float values  |
2 Uniform -- you need partculiar range values like 1 to 20 ,it's also return float
3. Randint --  you need partculiar range values like 5 to 10 ,it's also return int  ---* important

"""



import random

# print(dir(random))


# print(random.random())


# print(random.uniform(1,20))
# Instead of uniform method we can use below format
# print(random.random()*(10-1)+1)


#print(random.randint(5,10))


# ==============( Choice )===========
"""
4. choice  -- List la irruthu oru value random ah pick painne only one  value ah print painna ,we use choice method
5. sample  -- List la irruthu oru value random ah pick painne multiple values print painna ,we use sample method ,
                here we pass 2 arg | 1st list name , 2nd how many values return or Range like (list,2) its return 2 values

6. Shuffle  -- Shiffle the list
"""



List = [ 10 ,30,20,50,40]

# print(random.choice(List))


# print(random.sample(List,2))

random.shuffle(List)
print(List)

'''

#==============x============================( Word Gussing game us random module)=========x================================x============================x======

import random

words = ["Mango", "Apple", "Banana", "Orange"]

print(f" Guess the word :  {words} ")

word = random.choice(words)
#print(word)  # Check the random pick the list

while True:
    user = input(" \nEnter your word : ").title()

    #----------X ( Logic Part ) X----------#

    if user not in words:                                                     # This logic if the user enter wrong word
        print(f"\n{user} this word not in list ,Please Enter Correct Word ")# Print the message for user , enter crt word
        continue                                                              # Coutinue is use to go back to while loop again ask enter your word

    if user == word:
        print(f"Hurry , your Guess {word} is Correct! ")

        play_again = input("\n Do you want to continue ( Say  [Yes or No] ) : ").title()
        if play_again == "Yes" or play_again=="Y":
        #    words = ["Mango", "Apple", "Banana", "Orange"]
            word = random.choice(words)
            continue
        else:
            break

    else:
        print(f"Your Guss {user} is Wrong , Try Again ")


#===============x====================x=========================x==================