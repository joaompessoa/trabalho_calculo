import pygame
import sys
import random
import time
from criar_questoes import generate_questions

# Iniciar Pygame
pygame.init()

# Set up display
width, height = 1280, 720
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
block_width, block_height = 150, 50
blocks = []

# Bloco Inicial
initial_block = pygame.Rect(origin[0] - block_width // 2, origin[1] - block_height // 2, block_width, block_height)
blocks.append(initial_block)

# Fontes
font = pygame.font.SysFont("Arial", 28)
question_font = pygame.font.SysFont("Arial", 36)
feedback_font = pygame.font.SysFont("Arial", 32)

# Sample calculus questions
questions = []
current_question = None
# Scoreboard
correct_answers = 0
incorrect_answers = 0

# Current question and input state
user_input = ""
show_question = False
feedback = ""
time_limit = 30  # Default time limit
start_time = None
questions_asked = []

# Main game loop
def main():
    global show_question, user_input, feedback, start_time, time_limit, questions, current_question
    run = True
    show_start_menu = True
    difficulty_selected = False
    game_started = False
    end_game_menu = False

    while run:
        win.fill(white)
        
        if show_start_menu:
            display_start_menu(win)
        elif not difficulty_selected:
            display_difficulty_menu(win)
        elif not game_started:  # Question count and question generation 
            question_count = display_question_count_menu(win)
            questions = generate_questions(question_count)
            current_question = random.choice(questions) if questions else None

            # Start the game after questions are generated
            game_started = True
            show_question = True
            start_time = time.time()
        elif end_game_menu:
            end_game(questions)
            display_end_menu(win)
        else:
            draw_cartesian_plane(win)
            draw_blocks(win)
            display_scoreboard(win)
            if current_question:  # Check if there are questions
                
                display_question(win, current_question["question"], user_input)
                if show_question and start_time:  # Ensure start_time is not None
                    time_left = max(0, int(time_limit - (time.time() - start_time)))
                display_timer(win, time_left)  # Pass time_left to the function

                if feedback:
                    display_feedback(win, feedback)
            else:
                # Handle the case where no questions were generated
                feedback = "Fim do Jogo"
                # end_game(questions)  # Call end_game with questions used
                game_started = False  # Reset game after it ends
                show_question = False

            if (show_question and time_left == 0) or (not questions and current_question is None):
                feedback = "Tempo esgotado! Incorreto." if time_left == 0 else "Fim do jogo!"
                handle_incorrect_answer()

            if feedback:
                display_feedback(win, feedback)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Exit game
                    run = False
                elif show_start_menu:
                    if event.key == pygame.K_RETURN:
                        show_start_menu = False
                elif not difficulty_selected:
                    if event.key == pygame.K_1:
                        time_limit = 60  # Easy
                        difficulty_selected = True
                    elif event.key == pygame.K_2:
                        time_limit = 30  # Medium
                        difficulty_selected = True
                    elif event.key == pygame.K_3:
                        time_limit = 15  # Hard
                        difficulty_selected = True
                    else:
                        feedback = "Seleção inválida! Pressione 1, 2, ou 3."
                elif end_game_menu:
                    if event.key == pygame.K_RETURN:
                        reset_game()
                        show_start_menu = True
                        end_game_menu = False
                    elif event.key == pygame.K_ESCAPE:
                        run = False
                else:
                    if event.key == pygame.K_SPACE and not show_question:
                        show_question = True
                        start_time = time.time()
                    elif event.key == pygame.K_RETURN:
                        check_answer()
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        if feedback in ["Você venceu!", "Você perdeu!", "Fim do jogo!"]:
            # display_end_menu(win)
            end_game(questions)
            end_game_menu = True
            
           

        pygame.display.update()

    pygame.quit()
    sys.exit()

def display_start_menu(win):
    title_surface = font.render("Bem-vindo ao Calculus Jenga!", True, black)
    start_surface = font.render("Pressione Enter para começar", True, blue)
    win.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - 50))
    win.blit(start_surface, (width // 2 - start_surface.get_width() // 2, height // 2))

def display_difficulty_menu(win):
    difficulty_surface = font.render("Selecione a dificuldade:", True, black)
    easy_surface = font.render("1. Fácil (60 segundos)", True, green)
    medium_surface = font.render("2. Médio (30 segundos)", True, blue)
    hard_surface = font.render("3. Difícil (15 segundos)", True, red)
    exit_surface = font.render("Pressione ESC para sair", True, black)
    win.blit(difficulty_surface, (width // 2 - difficulty_surface.get_width() // 2, height // 2 - 100))
    win.blit(easy_surface, (width // 2 - easy_surface.get_width() // 2, height // 2 - 50))
    win.blit(medium_surface, (width // 2 - medium_surface.get_width() // 2, height // 2))
    win.blit(hard_surface, (width // 2 - hard_surface.get_width() // 2, height // 2 + 50))
    win.blit(exit_surface, (width // 2 - exit_surface.get_width() // 2, height // 2 + 100))

def draw_cartesian_plane(win):
    # Draw axes
    pygame.draw.line(win, axis_color, (0, origin[1]), (width, origin[1]), 2)
    pygame.draw.line(win, axis_color, (origin[0], 0), (origin[0], height), 2)

    # Draw grid lines
    for x in range(0, width, 20):
        pygame.draw.line(win, grid_color, (x, 0), (x, height))
    for y in range(0, height, 20):
        pygame.draw.line(win, grid_color, (0, y), (width, y))

def draw_blocks(win):
    for block in blocks:
        pygame.draw.rect(win, red, block)

def display_question(win, question, user_input):
    question_surface = question_font.render(question, True, black, white)
    input_surface = question_font.render(user_input, True, blue, white)
    win.blit(question_surface, (50, 50))
    win.blit(input_surface, (50, 100))

def display_feedback(win, feedback):
    feedback_surface = feedback_font.render(feedback, True, green if feedback == "Correto!" else red, white)
    win.blit(feedback_surface, (50, 150))

def display_timer(win, time_left):
    timer_surface = feedback_font.render(f"Faltam: {time_left}s", True, black, white)
    win.blit(timer_surface, (50, 200))

def display_scoreboard(win):
    score_surface = font.render(f"Certas: {correct_answers}  Erradas: {incorrect_answers}", True, black, white)
    win.blit(score_surface, (width - 300, 20))

def display_question_count_menu(win):
    question_count_input = ""
    max_questions = 10

    title_surface = font.render("Número de Perguntas (1-10):", True, black)
    instruction_surface = font.render("Digite o número e pressione Enter", True, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        count = int(question_count_input)
                        if 1 <= count <= max_questions:
                            return count
                        else:
                            instruction_surface = font.render("Número inválido! (1-10)", True, red)
                    except ValueError:
                        instruction_surface = font.render("Entrada inválida!", True, red)
                elif event.key == pygame.K_BACKSPACE:
                    question_count_input = question_count_input[:-1]
                else:
                    question_count_input += event.unicode

        win.fill(white)
        win.blit(title_surface, (width // 2 - title_surface.get_width() // 2, height // 2 - 100))
        count_surface = font.render(question_count_input, True, blue)
        win.blit(count_surface, (width // 2 - count_surface.get_width() // 2, height // 2 - 50))
        win.blit(instruction_surface, (width // 2 - instruction_surface.get_width() // 2, height // 2))
        pygame.display.flip()

def check_answer():
    global show_question, user_input, feedback, start_time, correct_answers, incorrect_answers, current_question, questions

    if user_input.strip() == str(current_question["answer"]):
        feedback = "Correto!"
        add_block_above()
        correct_answers += 1
    else:
        feedback = "Incorreto!"
        handle_incorrect_answer()
        incorrect_answers += 1

    show_question = False
    user_input = ""
    questions_asked.append(current_question)

    if questions:
        questions.remove(current_question)  # Remove the answered question
        if questions:  # Check if there are questions left
            current_question = random.choice(questions)
        else:
            feedback = "Fim do jogo!"
            end_game(questions_asked)
    else:
        current_question = None  # No more questions
        end_game(questions_asked)
    time_left = time_limit  # Reset the timer for the next question

def add_block_above():
    top_block = blocks[-1]
    new_block = pygame.Rect(top_block.left, top_block.top - block_height, block_width, block_height)
    blocks.append(new_block)
    check_win_condition()

def handle_incorrect_answer():
    global feedback
    if len(blocks) > 1:
        blocks.pop()
        feedback += " Bloco superior removido."
    else:
        bottom_block = blocks[0]
        new_block = pygame.Rect(bottom_block.left, bottom_block.top + block_height, block_width, block_height)
        blocks.insert(0, new_block)
        feedback += " Novo bloco adicionado abaixo."
        check_lose_condition()
    
def check_win_condition():
    global feedback
    # Check if topmost block is entirely above the screen
    if blocks[-1].top + block_height <= 0:
        feedback = "Você venceu!"
        end_game(questions)

def check_lose_condition():
    global feedback
    # Check if bottommost block is entirely below the screen
    if blocks[0].bottom - block_height >= height:
        feedback = "Você perdeu!"
        end_game(questions)


def end_game(questions_used):
    global show_question, user_input, current_question, feedback, start_time, end_game_menu
    show_question = False
    user_input = ""
    start_time = None
    end_game_menu = True

    # Result display in the main window
    result_surface = font.render(f"Corretos: {correct_answers}  Errados: {incorrect_answers}", True, blue, white)
    win.blit(result_surface, (width // 2 - result_surface.get_width() // 2, 50))  # Move to the top

    # Display used questions and their correct answers
    y_pos = 150  # Start lower down to give more space
    for question in questions_asked:
        question_surface = question_font.render(question["question"], True, black, white)
        win.blit(question_surface, (50, y_pos))

        # Display the correct answer below with more spacing
        answer_surface = question_font.render(f"Resposta: {question['answer']}", True, green, white)
        win.blit(answer_surface, (50, y_pos + 50))  # More space below the question

        y_pos += 120  # Increase the spacing between question-answer pairs

    pygame.display.flip()
    print(feedback) 


def display_end_menu(win):
    end_menu_surface = font.render("Deseja jogar novamente? Pressione Enter para continuar ou ESC para sair.", True, black)
    win.blit(end_menu_surface, (width // 2 - end_menu_surface.get_width() // 2, height - 100))

def reset_game():
    global blocks, feedback, current_question, correct_answers, incorrect_answers, questions, questions_asked, show_start_menu, end_game_menu
    blocks = [pygame.Rect(origin[0] - block_width // 2, origin[1] - block_height // 2, block_width, block_height)]
    feedback = ""
    current_question = None
    correct_answers = 0
    incorrect_answers = 0
    questions = []  # Reset the list of questions
    questions_asked = []  # Reset the list of asked questions
    show_start_menu = True
    end_game_menu = False

if __name__ == "__main__":
    main()
