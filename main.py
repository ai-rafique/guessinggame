from data import data
from art import logo,vs
import random

def compare(ent1,ent2):
    if ent1>ent2:
        return 'a'
    else:
        return 'b'

while input('Would you like to play the guessing game ? (y or n) :') =='y':
    random.shuffle(data)
    entity_1,entity_2 = random.choice(data[1::2]),random.choice(data[0::2])
    print('Who has more followers ?\n')
    print(f"{entity_1['name']} {vs} {entity_2['name']}")
    opt = input('Enter option a or b : ')
    answer = compare(entity_1['follower_count'],entity_2['follower_count'])
    if(opt == answer):
        print('CORRECT')
    else:
        print("Sorry Wrong answer")
        print(f"{entity_1['name']} has {entity_1['follower_count']} followers")
        print(f"{entity_2['name']} has {entity_2['follower_count']} followers")    


    