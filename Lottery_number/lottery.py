import random




def lottery_app():
    while 1:
        username = input("Enter your username to play: ")
        number = input("enter your lucky number 0 - 50: ")
        numbers = random.randint(0, 50)
        if numbers == 30:
           print("congratulations!", username,"you won")
        else:
           print("sorry", username, "you lost. you didn't get the lucky number, try again")    
        
        
        

lottery_app()        