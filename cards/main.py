import random


#1
def enter_username(player):
    '''The player is asked for their username
    
    Parameters
    ----------
    str : player
        player1 or player2 to be displayed in when asking for input from a player.

    Returns
    -------
    str
        The player's username
    '''
    
    return input(player + ', please enter a your user name : ')

#2
def authenticate_user(username):

    '''checks the user using password authentication. If the user does not exist, then the user must set a password. For both cases, the password will be asked. If not correct, then they must enter their password until it is correct.
    
    Parameters
    ----------
    str : username
        The username to check if exists and match their password against.

    '''
    password = ''    
    #check_username exists.
    if not check_user_exists(username,'authenticatedusers.txt'):
        #make sure the password entered is sufficiently strong, length 8, excluding empty spaces.
        while len(password) < 8 or password == None:

            password = input('user does not exist, please enter a password of at least eight characters : ').replace(' ','').strip()
        
        #as user does not exist, make a new user.
        create_user(username,password,'authenticatedusers.txt')
        print('password set for user : ' + username)
    
        print('')
    
    #NOw user exists, ask for their password.
    password = input('now please enter the password for ' + username + ':')        
    #keep asking if the password is wrong, until it is correct.
    while check_password(username,password,'authenticatedusers.txt') == False:

        password = input('incorrect password attempt, please try again : ')

    print(username + ' is logged in.')


def check_password(username,password,filename):

    '''Checks the player's account username with their password to see if it is correcty matched with the textfile DB.
    
    Parameters
    ----------
    str : username
        The player's account username
    str : password
        The player's account password to match with username.
    str : filename
        location of textfile containing account usernames and password

    Returns
    -------
    bool
        True of False result of matching each line on textfile database.
    '''
    #Finds the file and opens it.
    with open(filename) as file:
        #reads each line on the file.
        for line in file.readlines():
            #splits the line, that uses a ':' delimiter. Checkst username on left of delimiter and password, on right of delimiter matches those entered.
            if line.split(':')[0] == username and line.split(':')[1].replace('\n','') == password:
                return True

    return False

def check_user_exists(username,filename):
    
    '''checks the user exists inside the textfile DB
    
    Parameters
    ----------
    str : username
        the username to check in textfile DB.
    str : filename
        the file location.

    Returns
    -------
    boolean
        the result of whether the username exists as an account on the textfile database.
    '''
    #Try to open the file, if it exists.
    try:
        with open(filename) as file:
            #read each line in the file 
            for line in file.readlines():
                # for each line in the textfile, read the username, to the left of the ':' delimiter.
                if line.split(':')[0] == username:
                    #if the username matches, they exist in the the textfile db.
                    return True
    except FileNotFoundError:
    #If the file does not exist, the username does not exist.
        return False
    #If user is not in the DB textfile, return False.
    return False


def create_user(username,password,filename):
    
    '''adds a new user inside the textfile DB
    
    Parameters
    ----------
    str : username
        the username to check in textfile DB.
    str : password
        the user password to add to the textfile DB.
    str : filename
        the file location.
    '''
    #If the file exists, add the name and password to the end of the file. If not, make a new file and then add the username and password to the file. Both adds have a ':' delimiter added in between and a newline escape character add to the end.
    with open(filename, 'a+') as file:
        file.write(username + ':' + password + '\n')
    print('user ' + username + ' has been created')

def setup_cards():

    '''Prepares the game by creating a stack of cards, called a deck.

    Returns
    -------
    list : deck
        the sequential deck of cards for the game, randomised(shuffled).
    '''
    deck = []
    
    # go through each color
    for color in ['red','yellow','black']:
        # go through  each value from 1 to 10
        for number in range(1,11):
            #for each color and value make a unique card
            card = [color,number]
            #then add that card to the deck.
            deck.append(card)
    #after creating a deck of thirty cards, make sure they are random.
    random.shuffle(deck)
    #return the shuffled deck to the game.
    return deck

def calculate_winner(card1,card2):

    '''Compares p1s and p2s cards to see who wins.
    Parameters
    ----------
    list : card1
        Player1's card for comparison
    list : card2
        Player2's card for comparison

    Returns
    -------
    int
        a number represent whether player 1 or player 2 won.
    '''

    #if card colors are the same,
    if card1[0] == card2[0]:
        #compare their values.
        if card1[1] > card2[1]:
            
            return 1
    #IF card colors are not the same, compare their colors to see if player 1 wins.
    if card1[0] == 'red' and card2[0] == 'black':

        return 1

    if card1[0] == 'yellow' and card2[0] == 'red':

        return 1

    if card1[0] == 'black' and card2[0] == 'yellow':

        return 1
    #If player 1 did not win, assume player 2 wins.
    return 2

def play_game(name1,name2,deck):
    
    '''runs the game round by round until the deck of cards are empty.

    Parameters
    ----------
    str : name1
        The player's account username
    str : name2
        The player 2's account username
    list : deck
        The stack of cards to take the top cards from.
    

    Returns
    -------
    object : player1
        contains p1's name and the cards they acquired throughout playing the game.
    object : player2
        contains p2's name and the cards they acquired throughout playing the game.
    '''
    #make the two players
    player1 = {'name':name1,'cards':[]}
    player2 = {'name':name2,'cards':[]}
    
    #play until the deck is empty
    while deck != []:
        
        key = 'k'
        #ask player 1 to press enter, if they do not, ask again, until they do.
        while(key != ''):
            key = input(name1 + ' player 1, please press enter to take your turn')
        #give player one the top card from the deck.
        p1_card = deck.pop()
        print(name1 + ' has got : ',p1_card)
        
        key = 'k'

        #ask player 2 to press enter, if they do not, ask again, until they do.
        while(key != ''):
            key = input(name2 + ' player 2, please press enter to take your turn')
            
        #give player two the top card from the deck.
        p2_card = deck.pop()
        print(name2 + ' has got : ',p2_card)

        #compare the player's cards to see who wins.
        winner = calculate_winner(p1_card,p2_card)
        if winner == 2:
            print('winner of round is player 2 : '+name2)
        else:
            print('winner of round is player 1 : '+name1)
i       #GIve both of the cards to the winner.
        if winner == 1:
            
            player1['cards'].append(p1_card)
            player1['cards'].append(p2_card)
        
        else:

            player2['cards'].append(p1_card)
            player2['cards'].append(p2_card)
    #return the players with their cards at the end of the game.
    return player1,player2

def display_winner(player1,player2):

    '''show who won, with both players results.
    
    Parameters
    ----------
    object : player1
        player1 with their cards and name
    object : player2
        player2 with their cards and name

    '''
    if len(player1['cards']) > len(player2['cards']):
        
        print(player1['name'] + ' (player1) is the winner')

    else:

        print(player2['name'] + ' (player2) is the winner')
    print('') 
    print('scores are, p1 : score ', len(player1['cards']), ', p2 socres : ',len(player2['cards']))
    print('')
    print('total results are')
    print(player1)
    print(player2)

def main():

    ''' Runs the main game. '''

    #gets player one's username
    player1_name = enter_username('player 1 ')
    #Checks  player one is authorised to play the game.
    player1_auth = authenticate_user(player1_name)

    #gets player one's username
    player2_name = enter_username('player 2 ')    

    #Checks  player two is authorised to play the game.
    player2_auth = authenticate_user(player2_name)
    
    #Gets a shuffled deck for the game.
    deck = setup_cards()
    #plays the game and gets both players results after playing the game
    player1,player2 = play_game(player1_name,player2_name,deck)
    #displays the winner out of both of the players.
    display_winner(player1,player2)


if __name__== "__main__":
    
    main()
