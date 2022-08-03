import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        clear()
        black_jack()           

def black_jack():
    print(logo)
    
    player_cards = random.choices(cards, k=2)
    current_score = sum(player_cards)
    hit = random.choices(cards)[0]
    player_no_ace = []
    
    computer_cards = random.choices(cards, k=2)
    computer_score = sum(computer_cards)
    computer_hit = random.choices(cards)[0]
    no_ace = []

    while computer_score <= 16:
        computer_cards.append(computer_hit)
        if 11 in computer_cards and computer_score + computer_hit > 21:
            for card in computer_cards:
                if card == 11:
                    card = 1
                no_ace.append(card)
            computer_score = sum(no_ace)
            computer_cards = no_ace
        else:
            computer_score += computer_hit

    print(f"  Your cards: {player_cards}, Current score: {current_score}")
    #print(f"  ** Computer cards: {computer_cards}, Computer score: {computer_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    go = True

    while go:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            player_cards.append(hit)
            #current_score = sum(player_cards)

            if 11 in player_cards and current_score + hit > 21:
                for card in player_cards:
                    if card == 11:
                        card = 1
                    player_no_ace.append(card)
                current_score = sum(player_no_ace)
                player_cards = player_no_ace
            else:
                current_score += hit
            
            
            print(f"  Your cards: {player_cards}, Current score: {current_score}")
            print(f"  Computer's first card: {computer_cards[0]}")
            if current_score > 21 and computer_score > 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You both Bust! 😑")
                go = False
                play()
            elif computer_score > 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Computer bust. You win! 🥳")
                go = False
                play()
            elif current_score > 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Bust! 😫")
                go = False
                play()
            elif current_score == 21 and computer_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("It's a Blackjack Tie! 🙃")
                go = False
                play()
            elif current_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Win! 🥳")
                go = False
                play()
            elif computer_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Computer has Blackjack. You Lose. 😭")
                go = False
                play() 
                
        else:
            if current_score == 21 and computer_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("It's a Blackjack Tie! 🙃")
                go = False
                play()
            elif computer_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Computer has Blackjack. You Lose. 😭")
                go = False
                play() 
            elif current_score == 21:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Win! 🥳")
                go = False
                play() 
            elif current_score > computer_score:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Win! 🥳")
                go = False
                play()
            elif current_score == computer_score:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("It's a Tie! 🙃")
                go = False
                play()
            else:
                print(f"  Your final hand: {player_cards}, final score: {current_score}")
                print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("You Lose. 😭")
                go = False
                play()  
    
play()    
