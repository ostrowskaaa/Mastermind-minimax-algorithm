import pygame
import time

from mastermind import MastermindAlgorithm

WIDTH, HEIGHT = 420, 600
BALL_SIZE = 15


colours = {
    'background' : (43, 43, 56, 0.5),
    'green' : (151, 186, 115),
    'blue' : (126, 155, 217),
    'yellow' : (242, 237, 131),
    'orange' : (217, 185, 126),
    'red' : (219, 74, 96),
    'brown' : (70, 52, 42),
    'white' : (255, 255, 255),
    'black' : (0, 0, 0)
}


class Board():
    def __init__(self, window):
        self.window = window


    def draw_ball(self, colour, pos):
        return pygame.draw.circle(self.window, colour, pos, BALL_SIZE)


    def draw_answer(self, code):
        for ball in range(4):
            self.draw_ball(colours[code[ball]], (265 - ball*(BALL_SIZE + 20), int(HEIGHT/4)))


    def draw_move(self, code, which_move):
        for ball in range(len(code)):
            self.draw_ball(colours[code[ball]], (WIDTH - 45 - (ball+5)*(BALL_SIZE*2 + 10),
                                            (HEIGHT - 25 - (which_move+1)*(BALL_SIZE*2 + 10))))


    def feedback_to_colours(self, feedback):
        feedback_colours = []
        for black_ball in range(feedback[0]): feedback_colours.append('black')
        for white_ball in range(feedback[1]): feedback_colours.append('white')
        return feedback_colours


    def draw_feedback(self, feedback, which_move):
        feedback = self.feedback_to_colours(feedback)
        for ball in range(len(feedback)):
            self.draw_ball(colours[feedback[ball]], (WIDTH - 15 - (ball+1)*(BALL_SIZE*2 + 10),
                                            (HEIGHT - 25 - (which_move+1)*(BALL_SIZE*2 + 10))))


    def start_info(self):
        self.window.fill(colours['background'])
        text = my_font.render('Press spacebar to start game', 0, colours['white'])
        self.window.blit(text, (95, 60))


def event():
    global draw_text
    pygame.event.get()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        playing = False
        exit()
    if keys_pressed[pygame.K_SPACE]:
        if draw_text == True:
            draw_text = False
            window.fill(colours['background'])

##############################################################
pygame.init()
pygame.display.set_caption('Mastermind')
window = pygame.display.set_mode((WIDTH, HEIGHT))
my_font = pygame.font.SysFont('Times New Roman', 20)

mastermind = MastermindAlgorithm()
board = Board(window)


playing = True
draw_text = True
guessing = True


while playing:
    event()

    if draw_text == True:
        board.start_info()
        pygame.display.flip()
    elif guessing:
        guess, feedback, which_move = mastermind.make_move()
        board.draw_move(guess, which_move)
        pygame.display.flip()

        time.sleep(0.4)
        board.draw_feedback(feedback, which_move)
        if feedback[0] == 4:
            board.draw_answer(guess)
            text = my_font.render('Solved :)', 0, colours['white'])
            window.blit(text, (170, 240))
            guessing = False
        pygame.display.flip()
