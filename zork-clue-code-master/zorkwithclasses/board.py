from player import Player
import random
class Board():

    def __init__(self):
        self.players = []
         
    
    
    board= [["a1","|","a2", " ","a3","|","a4", " ","a5", " ","a6","|","a7","|","a8", " ","a9", " ","a10"],
        [" ", "|", " ", " ", " ","|", " ", " ", " ", " ", " ","|", " ","|", " ", " ", " ", " ", " "],
        ["b1","|","b2", " ","b3","d","b4", " ","b5", " ","b6","|","b7"," ","b8", " ","b9", " ","b10"],
        ["d" ,"-", " ", " ", " " ,"-" ,"-" ,"-" ,"-" ,"-","d" ,"-", " " ,"-" ,"d" ,"-" ,"-" ,"-" ,"-"],
        ["c1", " ","c2", " ","c3", " ","c4", " ","c5", " ","c6", " ","c7", " ","c8","|","c9", " ","c10"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","|", " ", " ", " "],
        ["d1", " ","d2", " ","d3", " ","d4", " ","d5", " ","d6", " ","d7", " ","d8","d","d9", " ","d10"], 
        ["-" ,"-" ,"-" ,"-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","|" ,"-", " " ,"-"],
        ["e1", " ","e2","|","e3", " ","e4", " ","e5", " ","e6", " ","e7", " ","e8","|","e9", " ","e10"],
        [" ", " ", " ","|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","|", " ", " " ,"-"],
        ["f1", " ","f2","|","f3", " ","f4", " ","f5", " ","f6", " ","f7", " ","f8","d","f9", " ","f10"],
        ["-" ,"-","d","|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","|" ,"-" ,"-" ,"-"],
        ["g1", " ","g2", " ","g3", " ","g4", " ","g5", " ","g6", " ","g7", " ","g8","|","g9", " ","g10"],
        ["-" ,"-" ,"-" ,"-", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","|" ,"", " " ,"-"],
        ["h1", " ","h2","d","h3", " ","h4", " ","h5", " ","h6", " ","h7", " ","h8","d","h9", " ","h10"],
        [" ", " ", " ","|", " " ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-", " ","|", " ", " ", " "],
        ["i1", " ","i2","|","i3","|","i4", " ","i5", " ","i6", " ","i7","|","i8","|","i9", " ","i10"],
        [" ", " ", " ","|", " ","|", " ", " ", " ", " ", " ", " ", " ","|", " ","|", " ", " ", " "],
        ["j1", " ","j2","|","j3","d","j4", " ","j5", " ","j6", " ","j7","d","j8","d","j9", " ","j10"] ]




    doors=["b1","b6","b4","b8","f2","d9","f9","h2"]
    storage=["a1","b1"] 
    study=["a4","a5","a6","b4","b5","b6"]
    lib=["a8","a9","a10","b8","b9","b10"]
    kitchen=["e1","e2","f1","f2"]
    teleport=["e5","f6"]
    bathroom=["c9","c10","d9","d10"]
    gallery=["e9","e10","f9","f10","g9","g10"]
    bed1=["h9","h10","i9","i10","j9","j10"]
    bed2=["h1","h2","i1","i2","j1","j2"]
    foyer=["i4","i5","i6","i7","j4","j5","j6","j7"]
    rooms=[storage,study,lib,kitchen,bathroom,gallery,bed1,bed2,foyer]

    board_for_random = [["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10"],
                    ["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"],
                    ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"],   
                    ["d1","d2","d3","d4","d5","d6","d7","d8","d9","d10"],   
                    ["e1","e2","e3","e4","e5","e6","e7","e8","e9","e10"],
                    ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"],
                    ["g1","g2","g3","g4","g5","g6","g7","g8","g9","g10"],
                    ["h1","h2","h3","h4","h5","h6","h7","h8","h9","h10"],
                    ["i1","i2","i3","i4","i5","i6","i7","i8","i9","i10"],
                    ["j1","j2","j3","j4","j5","j6","j7","j8","j9","j10"]] 
    
  
  #  def printAllPlayers(self):
   #     print('There are ', len( self.players), 'players')
    #    for player in self.players:
     #       print(player.name, ' and his position is ', player.x, player.y)
  
    
    def addPlayer(self, joined_player):
        self.players.append(joined_player)
        #print("New player", joined_player.name, "added to the game with position", joined_player.x,',', joined_player.y )
    
    
    def moveright(self,player):
        
        if player.y>=0 and player.y<len(Board.board)-1:
           if Board.board[player.x][player.y+1]==" ":
                player.y = player.y+2
                pos=Board.board[player.x][player.y]
                print(player.name,"is standing in ", pos,".")
                
          
           elif  Board.board[player.x][player.y+1]=="d":
                choice=input("Hey , do you choose to open the door?y or n :-")    
                if choice=="y":
                     player.y=player.y+2
                     pos= Board.board[player.x][player.y]
                     print(player.name,"is standing in ", pos,".")
                elif choice=="n":
                     pos= Board.board[player.x][player.y]
                     print(player.name,"is standing in the same place ", pos,".")
                else:
                     print("Invalid input.")
     
           else:
                print("There is a wall")
        else:
           print(player.name,"is standing at boundary.") 
        
    def moveleft(self,player):
        
        if  player.y<=len(Board.board)-1 and player.y>0:
            if Board.board[player.x][player.y-1]==" ":
                player.y=player.y-2
                pos=Board.board[player.x][player.y]
                print(player.name,"is standing in ", pos,".")
                
        
            elif Board.board[player.x][player.y-1]=="d":
                 choice=input("Do you choose to open the door?y or n :-")
                 if choice=="y":
                         player.y=player.y-2
                         pos= Board.board[player.x][player.y]
                         print(player.name,"standing in ", pos,".")
                 elif choice=="n":
                         pos= Board.board[player.x][player.y]
                         print(player.name,"is standing in the same place ", pos,".")
                 else:
                         print("Invalid input.")
        
            else:
                 print("There is a wall.")
        else:
             print(player.name,"is standing at boundary.")

        
    def moveup(self, player):
        
        if  player.x<=len(Board.board)-1 and player.x>0:    
            if Board.board[player.x-1][player.y]==" ":
                player.x=player.x-2
                pos=Board.board[player.x][player.y]
                print(player.name,"is standing in ", pos,".")
                
            
            elif Board.board[player.x-1][player.y]=="d":
                choice=input("Do you choose to open the door?y or n :-")
                if choice=="y":
                         player.x=player.x-2
                         pos= Board.board[player.x][player.y]
                         print(player.name,"is standing in ", pos,".")
                elif choice=="n":
                         pos= Board.board[player.x][player.y]
                         print(player.name,"is standing in the same place ", pos,".")
                else:
                         print("Invalid input.")
            
            else:
                 print("There is a wall.")
        
        else:
             print(player.name,"is standing at boundary.") 
        

    def movedown(self,player):
       
        if player.x>=0 and player.x<len(Board.board)-1:    
            if Board.board[player.x+1][player.y]==" ":
                player.x=player.x+2
                pos=Board.board[player.x][player.y]
                print(player.name,"is standing in ", pos,".")
                
    
    
            elif Board.board[player.x+1][player.y]=="d":
                choice=input("Do you chose to open the door?y or n :-")
                if choice=="y":
                    player.x=player.x+2
                    pos= Board.board[player.x][player.y]
                    print(player.name,"is standing in ", pos,".")
            
                elif choice=="n":
                     pos= Board.board[player.x][player.y]
                     print(player.name,"is standing in the same place ", pos,".")
            
                else:
                     print("Invalid input.")
            
            else:
                print("There is a wall.")
            
        else:
             print(player.name,"is standing at boundary.")  

    
    def current_room(self,player):
        
        if Board.board[player.x][player.y] in Board.storage:
            print("Player is in storage.")
            present_room="storage"
            
        elif Board.board[player.x][player.y] in Board.study:
            print("Player is in study.")
            present_room="study"
        
        elif Board.board[player.x][player.y] in Board.bathroom:
            print("Player is in bathroom.")
            present_room="bathroom"

        elif Board.board[player.x][player.y] in Board.lib:
            print("Player is in library.")
            present_room="lib"
        
        elif Board.board[player.x][player.y] in Board.gallery:
            print("Player is in gallery.")
            present_room="gallery"
        
        elif Board.board[player.x][player.y] in Board.bed1:
            print("Player is in bedroom 1.")
            present_room="bed1"
        
        elif Board.board[player.x][player.y] in Board.foyer:
            print("Player is in foyer.")
            present_room="foyer"
        
        elif Board.board[player.x][player.y] in Board.bed2:
            print("Player is in bedroom 2.")
            present_room="bed2"
        elif Board.board[player.x][player.y] in Board.kitchen:
            print("Player is in kitchen.")
            present_room="kitchen"
        else:
            print("Player is in hallway")
            present_room="hallway"

    def clues():
        print("The police didn't get many clues from interrogating the lunatic but here's what you have to go on, ")
        if weapon_position in Board.storage:
            print("")
            print("Boxes, boxes , boxes.")
            print("\nYou lose things forever, but once in a while you find belongings that trigger nostalgia.")            
            print("\nThe least accessed rom int he house.")
            print("")
        elif weapon_position in Board.study:
            print("")
            print("Sometimes it's used as an office.")
            print("\nIt's mostly only used on the weekends.")
            print("\nMost people forget I exist until they have to concentrate and get work done.")
            print("")
        elif weapon_position in Board.bathroom:
            print("")
            print("It's used a minimum of two times a day by the occupants.")
            print("Sometimes I'm stinky.")
            print("Unspeakable things are done in the room.")
            print("")
        elif weapon_position in Board.lib:
            print("")
            print("Most people spend a lot on the room, but end up rarely using it.")    
            print("Mark Cuban says the contents of this room are what made him a billionaire.")
            print("I'm an authors misery.")
            print("")
        elif weapon_position in Board.gallery:
            print("")
            print("The room only exists in the homes of the rich.")
            print("It has a couple of Rothko's, and a couple of other unheard names.")
            print("It's a display of wealth.")        
            print("")
        elif weapon_position in Board.bed1:
            print("")
            print("5 little monkeys didn't make it in the room.")
            print("The snooze button is the enemy.")
            print("It could have a king, queen or twin.")
            print("")
        elif weapon_position in Board.foyer:
           print("")
           print("We go in and out, in and out.")
           print("To leave you have to pass through me.")
           print("To enter you have to pass through me.")
           print("")
        elif weapon_position in Board.bed2:
            print("")
            print("5 little monkeys didn't make it in the room.")
            print("The snooze button is the enemy.")
            print("It could have a king, queen or twin.")
            print("")
        elif weapon_position in Board.kitchen:
            print("")
            print("The biggest scam is cooking for two hours to eat for 10 minutes.")
            print("It attract the rats if the plates aren't clean.")
            print("Order in!?")        
            print("")
        else:
           print("")
           print("It's been used a lot.")
           print("Nobody really gives it any credit for existing.")
           print("You have to pass through it to get anywhere")
           print("") 

weapon_x=random.randrange(0,len(Board.board_for_random))
weapon_y=random.randrange(0,len(Board.board_for_random))

weapon_position=Board.board_for_random[weapon_x][weapon_y]


