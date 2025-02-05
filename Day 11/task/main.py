#     #### My Practiced code for black jack

# import art
# import random
#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#
# choose_to_play=input("Do you want to play a game of Blackjack?"
#                      " Type 'y' or 'n': ").lower()
#
# def card_allot_handler(array_of_cards, no_of_card):
#     for i in range(no_of_card):
#         random_card=random.choice(cards)
#         sum_of_cards=random_card
#         for card in array_of_cards:
#             sum_of_cards+=card
#         if random_card==11 and sum_of_cards>=21:
#             random_card=1
#         array_of_cards.append(random_card)
#     return array_of_cards
#
# def get_card_list_sum(card_list):
#     card_sum=0
#     for card in card_list:
#         card_sum+=card
#     return card_sum
#
#
# if choose_to_play=='y':
#     print(art.logo)
#     user_cards = card_allot_handler([], 2)
#     computer_cards = card_allot_handler([], 2)
#     user_card_sum=get_card_list_sum(user_cards)
#     computer_card_sum=get_card_list_sum(computer_cards)
#
#     while computer_card_sum<=17:
#         computer_cards=card_allot_handler(computer_cards, 1)
#         computer_card_sum = get_card_list_sum(computer_cards)
#     another_card='y'
#     while another_card=='y':
#         print(f"Your cards: {user_cards}, current score: {user_card_sum}")
#         print(f"Computer's first card: {computer_cards[0]}")
#         if user_card_sum<21:
#             another_card=input("Type 'y' to get another card, type 'n' "
#                                "to pass:").lower()
#             if another_card=='y':
#                 user_cards = card_allot_handler(user_cards, 1)
#                 user_card_sum = get_card_list_sum(user_cards)
#             else:
#                 break
#         else:
#             break
#
#     print(f"Your final hand: {user_cards}, final score: {user_card_sum}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_card_sum}")
#
#     if computer_card_sum == user_card_sum:
#         print("Draw 🙃")
#     elif computer_card_sum > user_card_sum:
#         if computer_card_sum <= 21:
#             print("You lose 😤")
#         else:
#             print("Opponent went over. You win 😁")
#     elif computer_card_sum < user_card_sum:
#         if user_card_sum <= 21:
#             print("You win 😁")
#         else:
#             print("You went over. You lose 😭")
#
# else:
#     exit()



# ### code by course instructor

import random

import art

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    """Take a list of cards and return sum of according to the
    rules of blackjack game"""
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_scores, c_scores):
    if u_scores==c_scores:
        return "Draw 🙃"
    elif c_scores==0:
        return "Lose, Opponent has a Blackjack 😱"
    elif u_scores==0:
        return "Win with a Blackjack 😎"
    elif u_scores>21:
        return "You went over. You lose 😭"
    elif c_scores>21:
        return "Opponent went over. You win 😁"
    elif u_scores>c_scores:
        return "You win 😁"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)

    user_cards=[]
    computer_cards=[]
    computer_scores=-1
    user_scores=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_scores=calculate_scores(user_cards)
        computer_scores=calculate_scores(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_scores}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_scores==0 or computer_scores==0 or user_scores>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' "
                                       "to pass:").lower()
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_scores!=0 and computer_scores<17:
        computer_cards.append(deal_card())
        computer_scores=calculate_scores(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_scores}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_scores}")

    print(compare(user_scores,computer_scores))

while input("Do you want to play a game of Blackjack?"
                     " Type 'y' or 'n': ").lower()=='y':
    print("\n"*20)
    play_game()






