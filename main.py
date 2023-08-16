import random
#The game

#1. user entry
#2. authentication
#3. shuffle cards - setup game
#4. take turns
#5. get winner from each round.
#6. display winner

#prepare authentication file.


#1
def enter_username(player):
    
    return input(player + ', please enter a your user name : ')

#2
def authenticate_user(username):
    password = ''    
    #check_username exits on file.
    if not check_user_exists(username,'authenticatedusers.txt'):
        while len(password) < 8 or password == None:

            password = input('user does not exist, please enter a password of at least eight characters : ').replace(' ','').strip()
        
        create_user(username,password,'authenticatedusers.txt')
        print('password set for user : ' + username)
    
        print('')

    password = input('now please enter the password for ' + username + ':')        

    while check_password(username,password,'authenticatedusers.txt') == False:

        password = input('incorrect password attempt, please try again : ')

    print(username + ' is logged in.')


def check_password(username,password,filename):

    print(username, ' : pass input as', password)
    with open(filename) as file:

        for line in file.readlines():

            if line.split(':')[0] == username and line.split(':')[1].replace('\n','') == password:
                return True

    return False

def check_user_exists(username,filename):
    
    try:
        with open(filename) as file:

            for line in file.readlines():
                if line.split(':')[0] == username:
                    return True
    except FileNotFoundError:
        return False

    return False


def create_user(username,password,filename):

    with open(filename, 'a+') as file:
        file.write(username + ':' + password + '\n')
    print('user ' + username + ' has been created')

#main program - the game

def setup_cards():

    deck = []

    for color in ['red','yellow','black']:
        
        for number in range(1,11):
            
            card = [color,number]
            deck.append(card)
    
    random.shuffle(deck)
    return deck

def calculate_winner(card1,card2):
    
    if card1[0] == card2[0]:

        if card1[1] > card2[1]:
            
            return 1

    if card1[0] == 'red' and card2[0] == 'black':

        return 1

    if card1[0] == 'yellow' and card2[0] == 'red':

        return 1

    if card1[0] == 'black' and card2[0] == 'yellow':

        return 1

    return 2

def play_game(name1,name2,deck):
    
    player1 = {'name':name1,'cards':[]}
    player2 = {'name':name2,'cards':[]}
    
    #take turn key
    while deck != []:
        
        key = 'k'

        while(key != ''):
            key = input(name1 + ' player 1, please press enter to take your turn')
            
        p1_card = deck.pop()
        print(name1 + ' has got : ',p1_card)
        
        key = 'k'

        while(key != ''):
            key = input(name2 + ' player 2, please press enter to take your turn')
            
        p2_card = deck.pop()
        print(name2 + ' has got : ',p2_card)

        #calculate score
        winner = calculate_winner(p1_card,p2_card)
        if winner == 2: 
            print('winner of round is player 2 : '+name2)
        else:

            print('winner of round is player 1 : '+name1)

        if winner == 1:
            
            player1['cards'].append(p1_card)
            player1['cards'].append(p2_card)
        
        else:

            player2['cards'].append(p1_card)
            player2['cards'].append(p2_card)

    return player1,player2

def display_winner(player1,player2):

    if len(player1['cards']) > len(player2['cards']):
        
        print(player1['name'] + ' (player1) is the winner')

    else:

        print(player2['name'] + ' (player2) is the winner')
    
    print('scores are, p1 : score ', len(player1['cards']), ', p2 socres : ',len(player2['cards']))
    print(player1)
    print(player2)

def main():

    player1_name = enter_username('player 1 ')
#    #can play
    player1_auth = authenticate_user(player1_name)
#
    player2_name = enter_username('player 2 ')    
    player2_auth = authenticate_user(player2_name)
    
    deck = setup_cards()
    player1,player2 = play_game(player1_name,player2_name,deck)
    display_winner(player1,player2)

main()
