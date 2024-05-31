import pygame
import sys
import random
import time

# Iniciar Pygame
pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculus Jenga")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Plano Cartesiano
origin = (width // 2, height // 2)
axis_color = black
grid_color = (200, 200, 200)

# Bloco
block_width, block_height = 100, 20
blocks = []

# Bloco Inicial
initial_block = pygame.Rect(origin[0] - block_width // 2, origin[1] - block_height // 2, block_width, block_height)
blocks.append(initial_block)

# Fontes
font = pygame.font.SysFont("Arial", 24)
question_font = pygame.font.SysFont("Arial", 20)
feedback_font = pygame.font.SysFont("Arial", 24)

# Sample calculus questions
questions = [
    {"question": "What is the partial derivative of f(x, y) = x^2 + y^2 with respect to x?", "answer": "2x"},
    {"question": "Find the maximum of f(x) = -x^2 + 4x.", "answer": "2"},
    {"question": "Evaluate the double integral of 1 over the region 0 <= x <= 1 and 0 <= y <= 1.", "answer": "1"}
]

# Scoreboard
correct_answers = 0
incorrect_answers = 0

# Current question and input state
current_question = random.choice(questions)
user_input = ""
show_question = False
feedback = ""
time_limit = 10  # 10 seconds to answer each question
start_time = None

# Main game loop
def main():
    global show_question, user_input, feedback, start_time
    run = True
    while run:
        win.fill(white)
        draw_cartesian_plane(win)
        draw_blocks(win, blocks)
        display_scoreboard(win)

        if show_question:
            display_question(win, current_question["question"], user_input)
            display_timer(win)

        if feedback:
            display_feedback(win, feedback)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not show_question:
                    show_question = True
                    start_time = time.time()
                elif event.key == pygame.K_RETURN:
                    check_answer()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        if show_question and time.time() - start_time > time_limit:
            feedback = "Time's up! Incorrect."
            handle_incorrect_answer()

        pygame.display.update()

    pygame.quit()
    sys.exit()

def draw_cartesian_plane(win):
    # Draw axes
    pygame.draw.line(win, axis_color, (0, origin[1]), (width, origin[1]), 2)
    pygame.draw.line(win, axis_color, (origin[0], 0), (origin[0], height), 2)

    # Draw grid lines
    for x in range(0, width, 20):
        pygame.draw.line(win, grid_color, (x, 0), (x, height))
    for y in range(0, height, 20):
        pygame.draw.line(win, grid_color, (0, y), (width, y))

def draw_blocks(win, blocks):
    for block in blocks:
        pygame.draw.rect(win, red, block)

def display_question(win, question, user_input):
    question_surface = question_font.render(question, True, black)
    input_surface = question_font.render(user_input, True, blue)
    win.blit(question_surface, (50, 50))
    win.blit(input_surface, (50, 100))

def display_feedback(win, feedback):
    feedback_surface = feedback_font.render(feedback, True, green if feedback == "Correct!" else red)
    win.blit(feedback_surface, (50, 150))

def display_timer(win):
    time_left = max(0, int(time_limit - (time.time() - start_time)))
    timer_surface = feedback_font.render(f"Time left: {time_left}s", True, black)
    win.blit(timer_surface, (50, 200))

def display_scoreboard(win):
    score_surface = font.render(f"Correct: {correct_answers}  Incorrect: {incorrect_answers}", True, black)
    win.blit(score_surface, (width - 300, 20))

def check_answer():
    global show_question, user_input, current_question, feedback, start_time, correct_answers, incorrect_answers
    print(f"User input: {user_input}")  # Debugging statement
    if user_input.strip() == current_question["answer"]:
        feedback = "Correct!"
        print("Correct! Adding a block.")  # Debugging statement
        add_block_above()
        correct_answers += 1
    else:
        feedback = "Incorrect!"
        print("Incorrect! Removing or adding a block.")  # Debugging statement
        handle_incorrect_answer()
        incorrect_answers += 1

    show_question = False
    user_input = ""
    current_question = random.choice(questions)
    start_time = None

def add_block_above():
    top_block = blocks[-1]
    new_block = pygame.Rect(top_block.left, top_block.top - block_height, block_width, block_height)
    blocks.append(new_block)
    check_win_condition()

def handle_incorrect_answer():
    global feedback
    if len(blocks) > 1:
        blocks.pop()
        feedback += " Top block removed."
    else:
        bottom_block = blocks[0]
        new_block = pygame.Rect(bottom_block.left, bottom_block.top + block_height, block_width, block_height)
        blocks.insert(0, new_block)
        feedback += " New block added below."
        check_lose_condition()

def check_win_condition():
    if blocks[-1].top <= 0:
        feedback = "You win!"
        end_game()

def check_lose_condition():
    if blocks[0].bottom >= height:
        feedback = "You lose!"
        end_game()

def end_game():
    global show_question, user_input, current_question, feedback, start_time
    show_question = False
    user_input = ""
    start_time = None
    print(feedback)  # Display the result in the console
    pygame.time.wait(2000)  # Wait for 2 seconds to show the feedback
    reset_game()

def reset_game():
    global blocks, feedback, current_question, correct_answers, incorrect_answers
    blocks = [pygame.Rect(origin[0] - block_width // 2, origin[1] - block_height // 2, block_width, block_height)]
    feedback = ""
    current_question = random.choice(questions)
    correct_answers = 0
    incorrect_answers = 0

if __name__ == "__main__":
    main()
