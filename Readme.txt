NOTE :-
If you are planning to refer this code for your project you need to have strong knowledge about :-
    1) Python
    2) Tkinter
    3) Programming Logic.
This is a little complex project for beginner's

Please do follow me on Linkedin :- https://www.linkedin.com/in/karan-shah2001/


Tic Tac Toe Game
About the Game :-
A game in which two players alternately put Xs and Os in compartments of a figure formed by two vertical lines crossing 
two horizontal lines and each tries to get a row of three Xs or three Os before the opponent does.

Tic Tac Toe using python is a GUI based Game which I had coded just for time pass.
The difference between the other available tic tab toe using python and mine is that my code there is logic to calculate 
winner after each turn. That is if Player '0' is winning before the filling of all the nine tiles code will stop there 
and display Player '0' as the winner.In other codes available in the internet even if any of the player is winning the 
result will be shown only after all the tiles are filled that is one needs to complete the full game to check if he/she is the winner or not. 
Also another difference is 'X' and '0' cannot place bets till they get their chances. That is if the current chance to place bet is of 'X' then 
automatically the '0' button will be disabled and same goes with '0' that is if the current chance to place bet is of '0' then automatically the 'X' 
button will be disabled.

--- About the code  ---
Modules used in the given code are :-
    1) Tkinter
        Since this is a GUI based game we are using python's Tkinter module and its classes like Tkinter.font for using various fonts.
    2) Random
        Since our game is of two players where :-
            Player 1 is the User1 Which is associated with 'X'
            Player 2 is the User2 which is associated with '0'
        For taking decision of where to place X or 0, a user can select his option from the dropbox given.
        Suppose if the player1 wants to put '0' at place 9 so he can select number 9 from the dropbox and 
        then click on the '0' button given. But what if there is only one user and he wants to play this game.
        So in that case the player1 is the user and player2 is the Computer. For Computer to select any place at 
        which 'X' should be placed will be selected randomly using python's Random Module.
        That is the bets that will be placed by the user will be selected by the user.
        But, the bets that will be places by the computer will be randomly generated using Python's random Module.

---- GUI OF TIC TAC TOE GRID ----
    | 1 | 2 | 3
    | 4 | 5 | 6
    | 7 | 8 | 9 

Functions Involved in this Code :-
    1) check_if_x_is_the_winner()
        This is the function which will check after each bet (Total_bets_played >= 2)
        if Player which is associated with 'X' is the winner or not.
        If Player 1 is the winner than the game will stop there and display a message 
        'Player 1 is the winner'

    2) check_if_0_is_the_winner()
        This is the function which will check after each bet (Total bets played >= 2),
        if the Player which is associated with '0' is the winner or not.
        If player 2 is the winner than the game will stop where and display a message
        'Player 2 is the winner'
    
    3) final_round_checking()
        This is a special condition to check which player is winning.
        This function is only called after player 1 has played 4 bets and is about to 
        play one last bet in the game. That is only one place will be left for playing the best.
        This is the final condition to check.
        Here only one condition is checked that if after placing 'X' in the only tile left is 'X' 
        winning the game or not.
        If 'X' is winning the game than a message will be displayed :- 'player 1 is the winner '
        else a message will be displayed ' It's a Tie '.
    
    4) delete_from_options()
        Suppose Player1 played one bet by selecting '5th position' from the dropbox and placed 'X' at position 5. 
        Now since that position is now filled with 'X', '5th position' must not be available for any further bets.
        So this function will do the task of removing the positions from the available dropbox of positions after each 
        player bets his/her bet.

    5) put_x()
        This function will place the 'X' at the postion selected by the user from the dropbox.
        That is suppose if player 1 selects 5 as the postion from the dropbox and then clicks on the 'X' button
        this function will be called and 'X' will be appeared in the 5th Postion. 
        After that this function will call delete_from_options() to delete the 5th position.
    
    6) put_0()
        This function will place the '0' at the postion selected by the user from the dropbox.
        That is suppose if player 1 selects 5 as the postion from the dropbox and then clicks on the 'X' button
        this function will be called and '0' will be appeared in the 5th Postion. 
        After that this function will call delete_from_options() to delete the 5th position.

    

