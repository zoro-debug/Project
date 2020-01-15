dashboard = ['-'for i in range(9)]
game_is_running = True
current_player = 'X'
winner = None


def play_game():
    
    global game_is_running
    global winner

    show_board()
    
    while game_is_running:
        
        handle_turn(current_player)
        
        check_if_gameover()
        
        flip_player()

        
    if winner == 'X' or winner == 'O':
        print(winner + "'s won")
    elif winner == None :
        print("Tie")
   
    
def show_board():
    print("\n")
    print(dashboard[0] +'|' + dashboard[1]+'|'+dashboard[2]+"\t 1|2|3")
    print(dashboard[3] +'|' + dashboard[4]+'|'+dashboard[5]+"\t 4|5|6")
    print(dashboard[6] +'|' + dashboard[7]+'|'+dashboard[8]+"\t 7|8|9")
    print("\n")
    

def handle_turn(player):
    
    print(player + "'s turn")
    position = int(input("Enter no. between 1 to 9:\n"))
       
    valid = False 
    while not valid:
        
        while position not in range(1,10):
            print("invalid input;\nplese select number between 0 to 9")
            position = int(input("Enter no. between 1 to 9:"))
        
        position -=1
        if dashboard[position] == "-":
            valid = True
        else:
            print("you cant go there,select different input")
            
    dashboard[position] = player
    show_board()
 
    
def check_if_gameover():
    check_for_winner()
    check_for_tie()
 
    
def check_for_winner():
    global winner
    row_winner = row_matched()
    col_winner = col_matched()
    dia_winner = dia_matched()
    
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    else:
        winner = None
        
   
def row_matched():
    global game_is_running
    
    row_1 =dashboard[0]==dashboard[1]==dashboard[2]!= '-'
    row_2 =dashboard[3]==dashboard[4]==dashboard[5]!= '-'
    row_3 =dashboard[6]==dashboard[7]==dashboard[8]!= '-'
    
    if row_1 or row_2 or row_3 :
        game_is_running = False
        
    if row_1:
        return dashboard[0]
    elif row_2:
        return dashboard[3]
    elif row_3:
        return dashboard[6]
    else:
        return None


def col_matched():
    global game_is_running
    
    col_1 =dashboard[0]==dashboard[3]==dashboard[6]!= '-'
    col_2 =dashboard[1]==dashboard[4]==dashboard[7]!= '-'
    col_3 =dashboard[2]==dashboard[5]==dashboard[8]!= '-'
    
    if col_1 or col_2 or col_3 :
        game_is_running = False
        
    if col_1:
        return dashboard[0]
    elif col_2:
        return dashboard[1]
    elif col_3:
        return dashboard[2]
    else:
        return None

    
def dia_matched():
    global game_is_running
    
    dia_1 =dashboard[0]==dashboard[4]==dashboard[8]!= '-'
    dia_2 =dashboard[2]==dashboard[4]==dashboard[6]!= '-'
    
    if dia_1 or dia_2 :
        game_is_running = False
        
    if dia_1:
        return dashboard[0]
    elif dia_2:
        return dashboard[2]
    else:
        return None

def check_for_tie():
    global game_is_running
    
    if '-' not in dashboard:
        game_is_running = False
#        return True
#    
#    else:
#        return False


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
 

    
play_game()