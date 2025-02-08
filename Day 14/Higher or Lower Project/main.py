import random,game_data,art

print(art.logo)

data=game_data.data

def get_random_data():
    return random.choice(data)

def object_sentence_former(compare, obj):
    print(f"{compare}: {obj["name"]}, a "
          f"{obj["description"]}, from {obj["country"]}.")

def compare_two_data(obj_a, obj_b):
    a_follower_count=obj_a["follower_count"]
    b_follower_count=obj_b["follower_count"]
    if a_follower_count>b_follower_count:
        return 'a'
    elif b_follower_count>a_follower_count:
        return 'b'
    else:
        print("Both have same Follower count, so its a bonus.")
        return 'c'

object_A=get_random_data()

choice_is_correct=True
score=0
while choice_is_correct:
    object_sentence_former("Compare A",object_A)
    object_B=get_random_data()
    while object_A==object_B:
        object_B = get_random_data()
    print(art.vs)
    object_sentence_former("Against B",object_B)
    make_a_choice=input("Who has more followers? Type 'A' or 'B':").lower()
    higher_follower=compare_two_data(object_A,object_B)
    if make_a_choice==higher_follower:
        score+=1
        print(f"You're right! Current score: {score}.")
        object_A=object_B
    elif higher_follower=='c':
        score += 1
        print(f"You got a bonus point! Current score: {score}.")
        object_A = object_B
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        choice_is_correct=False
