from random import choice
from itertools import product, permutations
from collections import Counter

#COLORS = ['green', 'orange', 'blue', 'brown', 'yellow', 'red']
COLORS = ['green', 'orange', 'blue', 'brown']


class MastermindAlgorithm():
    def __init__(self):
        ''' answer - random code to guess by an algorithm '''
        self.answer = [choice(COLORS), choice(COLORS), choice(COLORS), choice(COLORS)]
        self.player_guesses = []
        self.all_possible_codes = self.generate_all_possibilities()
        self.narrowed_codes = self.all_possible_codes.copy()


    def generate_all_possibilities(self):
        ''' generates all possible sets of colours (4^4 = 256 possibilities) '''
        codes = []
        for p in product(COLORS, repeat=4):
            codes.append(list(p))
        return codes

    def narrow_down_possibilities(self, feedback, last_guess):
        '''
        it remove from all possible sets the ones which can not be an answer
        for example:
            - the codes that have been already used;
            - if the move is e.g. blue, blue, green, green and feedback WW
            then the answer can not have more then two blue or two green so
            codes with more then two of these colors are removed from possibilities
        '''
        narrowed = []
        for i in range(len(self.narrowed_codes)):
            new_feedback = self.give_feedback(last_guess, self.narrowed_codes[i])
            if new_feedback == feedback:
                narrowed.append(self.narrowed_codes[i])
        return narrowed


    def give_feedback(self, answer, guess):
        white = sum((Counter(answer) & Counter(guess)).values())
        black = sum(c == g for c, g in zip(answer, guess))
        return (black, white - black)


    def most_frequent(self, feedback_list):
        '''
        it counts how many times the code from all possible sets
        gained particular feedback while iterating  through all
        possible answers and returns the most frequent one
        '''
        dict_feedback = dict(Counter(feedback_list))
        feedback_type, how_many =  max(dict_feedback.items(), key=lambda x: x[1])
        return [feedback_type, how_many]


    def minmax(self):
        feedback_types = []
        scores = []
        for code in self.all_possible_codes:
            for possible_answer in self.narrowed_codes:
                feedback = self.give_feedback(possible_answer, code)
                feedback_types.append(feedback)

            max_hit = self.most_frequent(feedback_types)
            score = len(self.narrowed_codes) - max_hit[1]
            feedback_types = []
            scores.append([code, max_hit, score])

        scores.sort(key = lambda x: x[2], reverse = True)

        best_code = scores[0][0]
        matches = [x for x in scores if x[2] == scores[0][2] and x[0] in self.narrowed_codes]
        if len(matches) > 0:
            best_code = matches[0][0]
        return best_code


    def make_move(self):
        # first move
        if len(self.player_guesses) == 0:
            color1, color2 = choice(COLORS), choice(COLORS)
            guess = [color1, color1, color2, color2]

        # any other move
        else:
            guess = self.minmax()

        self.player_guesses.append(guess)
        feedback = self.give_feedback(self.answer, guess)
        self.all_possible_codes.remove(guess)
        self.narrowed_codes = self.narrow_down_possibilities(feedback, guess)

        return guess, feedback, len(self.player_guesses)


'''mastermind = MastermindAlgorithm()
playing = True

while playing:
    guess, feedback, which_move = mastermind.make_move()
    print(which_move, '. ', guess, '||', feedback)
    if feedback[0] == 4:
        playing = False'''
