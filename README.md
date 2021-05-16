# Mastermind-minimax-algorithm

The algorithm starts with generating a list with all possible four--value sets of colours: green, orange, blue, brown, yellow and red. That means at the beginning we have 1296 codes. At this stage, it also creates random secret code that has to be guessed. 

There are eight possible moves to take, although algorithm is designed in a way it should solve the puzzle in no more than five moves. First move of the codebreaker is to generate the first guess by filling two spots with one random color and the next two spots with another random color, e.x. brown, brown, orange, orange. Next, the codemaker gives a feedback. With this in mind the codebreaker removes from the list with all possible codes its move and all codes that would not give the same feedback as the move that has been just done. It is done by iterating the list with all possible codes (minus the first guess) as guesses with the first guess as an answer.

EXAMPLE
Let's say our first move is brown, brown, orange, orange and we get white, white as an answer. Now we take the list with all possible codes and try them one by one as a new guess while our first move pretends to be an answer. As an example, one of the possible codes is brown, brown, orange, brown and the feedback would be  black, black, white. As it does not get the same feedback as the first feedback we got it is removed from the list. In this situation all of the codes that have more then two brown or orange pegs would be removed as well as the codes that does not have two brown or two orange or one orange and one brown. It is because the first feedback (white, white) indicates there are at two spots filled with the colors from our move. 

After narrowing all the possible codes to the ones which still can be an answer, it is time to make another guess. Here starts the minimax algorithm. It takes the list with codes that have been left and the list with all possible codes. Now, it takes first possible code (S) from the list and mark it as an answer, it takes all possible answers and tries them one by one as a guess. All feedbacks are collected in another list and when the last code is checked it chooses the most frequent feedback from the list. Then it calculates the score which is the number of possible codes in the list minus the number that indicates how many times the most frequent feedback appeared. The score with checked code (S) is saved to another list for later. The whole procedure is repeated with the second possible code and so on as long as there are codes to check. 

After checking the list with all possible codes it chooses the code with the highest score and if it belongs to the list with narrowed codes as well, it becomes the next move. If it does not belong to the list with narrowed codes, it takes the second best move.

So the algorithm can be described simpler as follows:

1. Generate list of all possible codes from the available colors that is four value--long.
2. Generate first random move that is made from two colours.
3. Give a feedback.
4. If the feedback is four blacks, the game is won and algorithm terminates. If not, goes to step 5.
5. Narrow down all possible codes to the ones that can still be an answer.
6. Calculate the best possible move.
7. Give a feedback.
8. If feedback does not contain four black, repeat all the moves from 5 to 7.

This algorithm is not the most computationally efficient implementation as it is making operations on quite big lists of data. However, its main goal is to minimize the needed moves in order to solve the puzzle and in this case it works well as guesses the secret code in five or less moves.
