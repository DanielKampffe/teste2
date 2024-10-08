import pygame
import sys
import time

class ImageButton:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, win):
        win.blit(self.image, self.rect.topleft)

    def isOver(self, pos):
        return self.rect.collidepoint(pos)

def redrawWindow(screen, buttons, background):
    screen.blit(background, (0, 0))  # Desenha o background
    for button in buttons:
        button.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 600))  # Tamanho da tela
    fullscreen = False  # Adicionado para controlar o modo de tela cheia

    # Carrega as imagens de background
    welcome_background = pygame.image.load('/home/danielk/Imagens/telas/welcome.jpg')
    initial_background = pygame.image.load('/home/danielk/Imagens/telas/initial.jpg')
    lecture_backgrounds = [
        pygame.image.load('/home/danielk/Imagens/telas/lecture1.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/lecture2.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/lecture3.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/lecture4.jpg')
    ]
    room_backgrounds = [
        pygame.image.load('/home/danielk/Imagens/telas/room1.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/room2.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/room3.jpg'),
        pygame.image.load('/home/danielk/Imagens/telas/room4.jpg')
    ]
    help_background = pygame.image.load('/home/danielk/Imagens/telas/help.jpg')
    end_background = pygame.image.load('/home/danielk/Imagens/telas/end.jpg')

    # Botões da tela inicial
    initial_buttons = [
        ImageButton(425, 144, '/home/danielk/Imagens/botoes/Blecture1.png'),
        ImageButton(243, 244, '/home/danielk/Imagens/botoes/Blecture2.png'),
        ImageButton(200, 344, '/home/danielk/Imagens/botoes/Blecture3.png'),
        ImageButton(330, 444, '/home/danielk/Imagens/botoes/Blecture4.png')
    ]

    lecture_buttons = [
        ImageButton(20, 276, '/home/danielk/Imagens/botoes/back.png'),
        ImageButton(956, 276, '/home/danielk/Imagens/botoes/next.png'),
        ImageButton(20, 20, '/home/danielk/Imagens/botoes/menu.png')
    ]

    room_buttons = [
        ImageButton(20, 276, '/home/danielk/Imagens/botoes/back.png'),
        ImageButton(956, 276, '/home/danielk/Imagens/botoes/next.png'),
        ImageButton(20, 20, '/home/danielk/Imagens/botoes/menu.png')
    ]

    help_buttons = [
        ImageButton(725, 477, '/home/danielk/Imagens/botoes/no.png'),
        ImageButton(170, 477, '/home/danielk/Imagens/botoes/yes.png')
    ]

    welcome_buttons = [
        ImageButton(424, 488, '/home/danielk/Imagens/botoes/start.png')
    ]

    end_buttons = [
        ImageButton(424, 488, '/home/danielk/Imagens/botoes/end.png')
    ]

    current_screen = 'welcome'
    buttons = welcome_buttons
    lecture_info = None
    screen_history = ['welcome']
    lecture_index = None

    # Timers
    timer_40s = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_40s, 40000)  # 40 segundos
    timer_70s = pygame.USEREVENT + 2
    pygame.time.set_timer(timer_70s, 70000)  # 70 segundos

    while True:
        redrawWindow(screen, buttons, welcome_background if current_screen == 'welcome' else end_background if current_screen == 'end' else initial_background if current_screen == 'initial' else help_background if current_screen == 'help' else lecture_backgrounds[lecture_index] if current_screen == 'lecture' else room_backgrounds[lecture_index])
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # Adicionado para detectar a tecla F11
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((1024, 600), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1024, 600))

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isOver(pos):
                        # Ação correspondente ao botão clicado
                        if button == initial_buttons[0]:
                            lecture_info = 'Informações da palestra 1'
                            lecture_index = 0
                            current_screen = 'lecture'
                            buttons = lecture_buttons
                            screen_history.append('lecture')
                        elif button == initial_buttons[1]:
                            lecture_info = 'Informações da palestra 2'
                            lecture_index = 1
                            current_screen = 'lecture'
                            buttons = lecture_buttons
                            screen_history.append('lecture')
                        elif button == initial_buttons[2]:
                            lecture_info = 'Informações da palestra 3'
                            lecture_index = 2
                            current_screen = 'lecture'
                            buttons = lecture_buttons
                            screen_history.append('lecture')
                        elif button == initial_buttons[3]:
                            lecture_info = 'Informações da palestra 4'
                            lecture_index = 3
                            current_screen = 'lecture'
                            buttons = lecture_buttons
                            screen_history.append('lecture')
                        elif button in lecture_buttons:
                            if button == lecture_buttons[0]:  # Voltar
                                screen_history.pop()
                                current_screen = screen_history[-1]
                                if current_screen == 'initial':
                                    buttons = initial_buttons
                                elif current_screen == 'lecture':
                                    buttons = lecture_buttons
                                elif current_screen == 'room':
                                    buttons = room_buttons
                                elif current_screen == 'help':
                                    buttons = help_buttons
                            elif button == lecture_buttons[1]:  # Próximo
                                if current_screen == 'lecture':
                                    current_screen = 'room'
                                    buttons = room_buttons
                                    screen_history.append('room')
                                elif current_screen == 'room':
                                    current_screen = 'end'
                                    buttons = end_buttons
                                    screen_history.append('end')
                            elif button == lecture_buttons[2]:  # Menu
                                current_screen = 'initial'
                                buttons = initial_buttons
                                screen_history.append('initial')
                        elif button in room_buttons:
                            if button == room_buttons[0]:  # Voltar
                                screen_history.pop()
                                current_screen = screen_history[-1]
                                if current_screen == 'initial':
                                    buttons = initial_buttons
                                elif current_screen == 'lecture':
                                    buttons = lecture_buttons
                                elif current_screen == 'room':
                                    buttons = room_buttons
                                elif current_screen == 'help':
                                    buttons = help_buttons
                            elif button == room_buttons[1]:  # Próximo
                                current_screen = 'end'
                                buttons = end_buttons
                                screen_history.append('end')
                            elif button == room_buttons[2]:  # Menu
                                current_screen = 'initial'
                                buttons = initial_buttons
                                screen_history.append('initial')
                        elif button in help_buttons:
                            if button == help_buttons[0]:  # Não
                                pygame.quit()
                                sys.exit()
                            elif button == help_buttons[1]:  # Sim
                                current_screen = 'initial'
                                buttons = initial_buttons
                                screen_history.append('initial')
                        elif button in welcome_buttons:
                            current_screen = 'initial'
                            buttons = initial_buttons
                            screen_history.append('initial')
                        elif button in end_buttons:
                            pygame.quit()
                            sys.exit()

            if event.type == timer_40s:
                if current_screen not in ['welcome', 'end']:
                    current_screen = 'welcome'
                    buttons = welcome_buttons
                    screen_history = ['welcome']  # Limpa o histórico

            if event.type == timer_70s:
                if current_screen == 'end':
                    current_screen = 'welcome'
                    buttons = welcome_buttons
                    screen_history = ['welcome']  # Limpa o histórico

if __name__ == "__main__":
    main()
