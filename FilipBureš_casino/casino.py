import random
import math

#Šance na výhru 18/37
#Šance na zelenou 1/37 (nelze ji vybrat = automatická prohra)

play = True
while play:
    total_guesses = 0
    total_red = 0
    total_black = 0
    total_won = 0
    total_lost = 0
    interactions = 0
    total_green = 0
    total_cash = int(input("Write your total cash: "))

    wrong_player = False

    while wrong_player == False:
        who_plays = input("Write who wants to play (bot/player): ") #Nabídka kdo bude hrát
        if who_plays == "bot" or who_plays == "player":
            wrong_player = True
        else:
            print("Wrong player. Try again.")
            continue
    if who_plays == "player": #Player
        while total_cash > 0:
            nothing_wrong = False
            wrong_color = False
            while nothing_wrong == False:
                bet = int(input("Write how much you want to bet: "))
                if total_cash < bet:
                    print("You dont have enough money.")
                    continue
                else:
                    nothing_wrong = True
                while wrong_color == False:
                    guess = input("Write which color you want to pick (red or black): ")
                    if guess == "black" or guess == "red":
                        wrong_color = True
                    else:
                        print("Wrong color. Try again.")
                        continue
                    roll = random.randint(1,37)
                    if guess == "red":
                        if roll >= 1 and roll <= 18:
                            total_cash = total_cash + bet
                            print("YOU WON - current cash:",total_cash)
                            total_won+=1
                            total_red+=1
                        elif roll >= 19 and roll <= 36:
                            total_cash = total_cash - bet
                            print("YOU LOST - current cash:",total_cash)
                            total_lost+=1
                            total_red+=1
                        else:
                            total_cash = total_cash - bet
                            print("YOU LOST - current cash:",total_cash)
                            total_lost+=1
                            total_green+=1
                    elif guess == "black":
                        if roll >= 19 and roll <= 36:
                            total_cash = total_cash + bet
                            print("YOU WON - current cash:",total_cash)
                            total_won+=1
                            total_black+=1
                        elif roll >= 1 and roll <= 18:
                            total_cash = total_cash - bet
                            print("YOU LOST - current cash:",total_cash)
                            total_lost+=1
                            total_black+=1
                        else:
                            total_cash = total_cash - bet
                            print("YOU LOST - current cash:",total_cash)
                            total_lost+=1
                            total_green+=1
                    interactions+=1
        print("---------------------------------------------------")
        playing = False
        while playing == False:
            percent_black = (total_black / interactions) * 100 #Výpis procent pro playera
            percent_red = (total_red / interactions) * 100
            percent_green = (total_green / interactions) * 100
            percent_wins = (total_won / interactions) * 100
            percent_loses = (total_lost / interactions) * 100
            print("Black color:",total_black,"(",percent_black,"%",")")
            print("Red color:",total_red,"(",percent_red,"%",")")
            print("Green color:",total_green,"(",percent_green,"%",")")
            print("Number of wins:",total_won,"(",percent_wins,"%",")")
            print("Number of loses:",total_lost,"(",percent_loses,"%",")")
            again = input("Want to play again ? (YES or NO): ")
            if again == "yes" or again == "no":
                playing = True
            else:
                print("Try again.")
                continue
            if again == "no":
                quit()
            else:
                play = True
    else: #Bot
        while total_cash > 0:
                print("Write how much you want to bet: ")
                bet = random.randint(1,total_cash) #BOT sází náhodnou částku, kterou si může dovolit
                print("BET:",bet)
                print("Write which color you want to pick (red or black): ")
                bot_guess = random.randint(1,2)
                if bot_guess == 1:
                    bot_color = "black"
                else:
                    bot_color = "red"
                roll = random.randint(1,37)
                print(roll)
                print("Bot said",bot_color)
                if bot_color == "red":
                    if roll >= 1 and roll <= 18:
                        total_cash = total_cash + bet
                        print("YOU WON - current cash:",total_cash)
                        total_won+=1
                        total_red+=1
                    elif roll >= 19 and roll <= 36:
                        total_cash = total_cash - bet
                        print("YOU LOST - current cash:",total_cash)
                        total_lost+=1
                        total_red+=1
                    else:
                        total_cash = total_cash - bet
                        print("YOU LOST - current cash:",total_cash)
                        total_lost+=1
                        total_green+=1
                elif bot_color == "black":
                    if roll >= 19 and roll <= 36:
                        total_cash = total_cash + bet
                        print("YOU WON - current cash:",total_cash)
                        total_won+=1
                        total_black+=1
                    elif roll >= 1 and roll <= 18:
                        total_cash = total_cash - bet
                        print("YOU LOST - current cash:",total_cash)
                        total_lost+=1
                        total_black+=1
                    else:
                        total_cash = total_cash - bet
                        print("YOU LOST - current cash:",total_cash)
                        total_lost+=1
                        total_green+=1
                interactions+=1
                print("---------------------------------------------------")
                total_guesses+=1
        print("")
        playing = False
        while playing == False:
            percent_black = (total_black / interactions) * 100 #Výpis procent pro bota
            percent_red = (total_red / interactions) * 100
            percent_green = (total_green / interactions) * 100
            percent_wins = (total_won / interactions) * 100
            percent_loses = (total_lost / interactions) * 100
            print("Black color:",total_black,"(",percent_black,"%",")")
            print("Red color:",total_red,"(",percent_red,"%",")")
            print("Green color:",total_green,"(",percent_green,"%",")")
            print("Number of wins:",total_won,"(",percent_wins,"%",")")
            print("Number of loses:",total_lost,"(",percent_loses,"%",")")
            again = input("Want to play again ? (YES or NO): ")
            if again == "yes" or again == "no":
                playing = True
            else:
                print("Try again.")
                continue
            if again == "no":
                quit()
            else:
                play = True
                    
                        



