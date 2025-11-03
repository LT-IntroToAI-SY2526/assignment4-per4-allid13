# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
The most difficult part of tic-tac-toe was understanding how to implement game_over function and understand how to make the self.has_won function onto it and figure out when the player wins. Although I knew how to get the has_won function for both x and o and call whichever of the two has won, it was hard for me to be able to create a function that works with it and find all the possible cominations that were possible and which combinations weren't possible. 

2. Explain how you would add a computer player to the game.
I would add a computer player to the game by assigning a parameter based on whether the computer is x or o. And evertime the modified function of play_tic_tac_toe where it  will check whether it is the humans turn or the computers.Then I would create a function called compuer_turn which would make the computer input a correct move onto the board. Then if it is the humans turn, it would just wait for the human to input a move.
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
I would create a way for the computer to be able to think ahead like a human in a way where the computer would questiontheir move and the results that that move would lead to. For example if the computer is thinking of placing a move in a certain position, then it would think twice and try to guess what the opponent would do in order to be able to win. 