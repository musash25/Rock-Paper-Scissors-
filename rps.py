from random import randint

t = ["Rock", "Paper", "Scissors", "Gun"]


computer = t[randint(0,2)]
player = False
             
while player == False:
            
            player = input ("Rock, Paper, Scissors?")
            if player.capitalize() == computer.capitalize():
                print("Tie")
            elif player.capitalize() == "Rock":
                if computer == "Paper":
                     print("You lose!", computer, "covers", player)
                else:
                  print("You win!", player, "smashes", computer)
            elif player.capitalize() == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", computer, "cut", player)
            elif player.capitalize() == "Scissors":
                if computer == "Rock":
                  print("You lose!", computer, "crushes", player)
                else:
                  print("You win!", computer, "crushes", player)
                  player = False
            elif player.capitalize() == "Gun":
              if computer =="Rock":
                print("You win! Gun beats everything :)")
              else:
                print("You win! Gun beats everything :)")
              
            else:
              print("Error 1 - Type not recognized.")
              

