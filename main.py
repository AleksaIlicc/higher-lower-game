import random
from art import logo,vs
from game_data import data

print(logo)
print(random.choice(data))
def randomindex():
    random_index_of_list=random.randint(0, (len(data)-1))
    return random_index_of_list

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
 
indexA = randomindex()
indexB= randomindex()

nameA=data[indexA]["name"]
descriptionA=data[indexA]["description"]
countryA=data[indexA]["country"]
followersA=data[indexA]["follower_count"]

nameB=data[indexB]["name"]
descriptionB=data[indexB]["description"]
countryB=data[indexB]["country"]
followersB=data[indexB]["follower_count"]
end_of_game=False
highscore=0
while end_of_game==False:
    print(f"Compare A: {nameA}, {descriptionA}, from {countryA}")
    print(vs)
    print(f"Compare B: {nameB}, {descriptionB}, from {countryB}")
    if followersA>followersB:
        answer="A"
    else:
        answer="B"
    guess= input("Who has more followers? Type 'A' or 'B': ")
    if guess==answer:
        cls()
        print(logo)
        highscore+=1
        print(f"You're right. Your high score is: {highscore}.")
        if answer=="B":
            nameA=nameB
            descriptionA=descriptionB
            countryA=countryB
            followersA=followersB
        indexB= randomindex()
        nameB=data[indexB]["name"]
        descriptionB=data[indexB]["description"]
        countryB=data[indexB]["country"]
        followersB=data[indexB]["follower_count"]
    else:
        print(f"Sorry, that's wrong. Final score: {highscore}")
        end_of_game=True
