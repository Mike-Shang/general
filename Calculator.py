import pygame
from Class_Calculator import *

pygame.init()

pygame.display.set_caption("Calculator")
Display = pygame.display.set_mode(
    (400, 700))
Equal = ''
font = pygame.font.SysFont(
    "Arial", 50)
clock = pygame.time.Clock()

# hex color
red = (255, 255, 255)
white = (0, 0, 0)
blue_button = (255, 255, 255)
blue_button1 = (255, 255, 255)
list_xy = []
Display.fill(white)                                 # Set Color Display
list_str_cal = ['(', ')', 'c', '«', '7', '8', '9', '÷', '4', '5',
                '6', 'x', '1', '2', '3', '-', '.', '0', '=', '+']  # list button
list_btm_class = []
in_list = 0

i = 0
for y in range(200, 700, 100):
    for x in range(0, 400, 100):
        # Append Class to List
        list_btm_class.append(Draw(blue_button, x, y, 100, 100))
        # Create Button from Class
        Draw(blue_button, x, y, 100, 100).Rect()
        # White Text on Display
        Display.blit(font.render(list_str_cal[i], True, (white)), (x+30, y+30))
        i = i+1

run = True
while run:

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Even about MouseDown
            Process_btm = pygame.draw.rect(Display, white, (0, 0, 400, 200))

            # Check Position Mouse with Button (Press Button)
            if list_btm_class[3].isPosition(pos):
                Equal = Equal[:-1]
            elif list_btm_class[2].isPosition(pos):
                Equal = ''
            elif len(Equal) == 11:
                pass
            elif list_btm_class[0].isPosition(pos):
                Equal += '('
            elif list_btm_class[1].isPosition(pos):
                Equal += ')'
            elif list_btm_class[4].isPosition(pos):
                Equal += '7'
            elif list_btm_class[5].isPosition(pos):
                Equal += '8'
            elif list_btm_class[6].isPosition(pos):
                Equal += '9'
            elif list_btm_class[7].isPosition(pos):
                Equal += '/'
            elif list_btm_class[8].isPosition(pos):
                Equal += '4'
            elif list_btm_class[9].isPosition(pos):
                Equal += '5'
            elif list_btm_class[10].isPosition(pos):
                Equal += '6'
            elif list_btm_class[11].isPosition(pos):
                Equal += '*'
            elif list_btm_class[12].isPosition(pos):
                Equal += '1'
            elif list_btm_class[13].isPosition(pos):
                Equal += '2'
            elif list_btm_class[14].isPosition(pos):
                Equal += '3'
            elif list_btm_class[15].isPosition(pos):
                Equal += '-'
            elif list_btm_class[16].isPosition(pos):
                Equal += '.'
            elif list_btm_class[17].isPosition(pos):
                Equal += '0'
            elif list_btm_class[19].isPosition(pos):
                Equal += '+'

            # Clear the display area before rendering new text
            Display.fill(white, (0, 0, 400, 200))

            # Render Text ---> Equal
            text = font.render(str(Equal), True, red)
            # Show Text (x,y)
            Display.blit(text, (25, 50))

            if list_btm_class[18].isPosition(pos):
                Process_btm = pygame.draw.rect(
                    Display, white, (0, 0, 400, 200))
                pygame.display.update()
                if Equal == '13411':  # if Condition
                    Equal = "Apisit.K"
                    text = font.render(str(Equal), True, red)
                    Display.blit(text, (25, 50))
                elif len(Equal) == 0:
                    Equal = "0"
                    text = font.render(str(Equal), True, red)
                    Display.blit(text, (25, 50))
                elif '/0' in Equal or '*/' in Equal or '/*' in Equal or Equal[0] == '*' or Equal[0] == '/' or Equal[-1] == '*' or Equal[-1] == '/' or Equal[0] == '.':
                    Equal = "Error"  # for Error Case
                    text = font.render(str(Equal), True, red)
                    Display.blit(text, (25, 50))
                elif '/' in Equal or '*' in Equal or '+' in Equal or '-' in Equal:
                    answer = str("%0.2f" % (eval(Equal)))
                    if '.00' in answer:
                        answer = str(int(float(answer)))
                        text = font.render(str(answer), True, red)
                        Display.blit(text, (25, 50))
                        Equal = answer
                    else:
                        text = font.render(str(answer), True, red)
                        Display.blit(text, (25, 50))
                        Equal = answer
                else:
                    text = font.render(str(Equal), True, red)
                    Display.blit(text, (25, 50))

        # if mouse on button change color
        elif event.type == pygame.MOUSEMOTION:
            for i in list_btm_class:
                if i.isPosition(pos):
                    i.set_color(blue_button1)
                else:
                    i.set_color(blue_button)
            i = 0
            for y in range(200, 700, 100):
                for x in range(0, 400, 100):
                    # White Text on Display
                    Display.blit(font.render(
                        list_str_cal[i], True, (white)), (x+30, y+30))
                    i = i+1
        # Quit Program
        elif event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
quit()
