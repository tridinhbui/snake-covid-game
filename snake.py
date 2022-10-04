import pygame, random, time, sys

from pygame.font import Font

pygame.init()
def main():
    level = " "
    m = 20  # kích thước chiều cao và chiều rộng
    Imgbody = pygame.transform.scale(pygame.image.load('body.bmp'), (m, m))
    Imghead = pygame.transform.scale(pygame.image.load('head.bmp'), (m, m))
    Imgfood = pygame.transform.scale(pygame.image.load('covid.bmp'), (m, m))
    #小图片


    #平台，背景，标题
    gameSurface = pygame.display.set_mode((880, 605))
    Imguniverse=pygame.image.load('universe.bmp').convert()
    cartoon = pygame.transform.scale(pygame.image.load('cartoon.bmp'), (880, 605))
    pygame.display.set_caption('Snake Covid-19!')



    red = pygame.Color(255, 0, 0)
    blue = pygame.Color(65, 105, 255)
    black = pygame.Color(0, 0, 0)


    snakepos = [100, 60]
    snakebody = [[100, 60], [80, 60], [60, 60]]
    foodx = random.randrange(1, 71)
    foody = random.randrange(1, 45)
    foodx1 = random.randrange(1, 71)
    foody1 = random.randrange(1, 45)
    foodx2 = random.randrange(1, 71)
    foody2 = random.randrange(1, 45)
    if foodx % 2 != 0: foodx += 1
    if foody % 2 != 0: foody += 1
    if foodx1 % 2 != 0: foodx1 += 1
    if foody1 % 2 != 0: foody1 += 1
    if foodx2 % 2 != 0: foodx2 += 1
    if foody2 % 2 != 0: foody2 += 1
    foodpos = [foodx * 10, foody * 10]
    foodpos1 = [foodx1 * 10, foody1 * 10]
    foodpos2 = [foodx2 * 10, foody2 * 10]
    foodflat = True
    foodflat1=True
    foodflat2=True
    direction = 'RIGHT'
    changeto = direction
    score = 0


    def game_over():
        gfont = pygame.font.SysFont('consolas', 40)
        gsurf = gfont.render('Game over!', True, red)
        grect = gsurf.get_rect()
        grect.midtop = (360, 150)
        gameSurface.blit(gsurf, grect)
        show_score(0)
        pygame.display.flip()
        time.sleep(2)
        ans = play_again().lower()
        if ans == "yes":
            main()
        else:
            pygame.quit()

    def choose_level():
        font = pygame.font.Font(None, 25)
        input_box = pygame.Rect(150, 200, 600, 30)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:                       
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            filled = (0,0,0)
            gfont = pygame.font.SysFont('consolas',  30)
            gsurf = gfont.render('Type snake speed level (0 -> 500) ', True, red)
            grect = gsurf.get_rect()
            grect.midtop = (470, 150)
            gameSurface.blit(gsurf, grect)
            pygame.display.flip()
            gameSurface.blit(Imguniverse, (0, 0))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Blit the text.
            gameSurface.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(gameSurface, color, input_box, 5)

    
    def play_again():
        font = pygame.font.Font(None, 25)
        input_box = pygame.Rect(150, 200, 600, 30)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:                       
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            gfont = pygame.font.SysFont('consolas', bold = True, italic = False, size = 30)
            gsurf = gfont.render('type "yes" to play again!', True, blue)
            grect = gsurf.get_rect()
            grect.midtop = (440, 150)
            gameSurface.blit(gsurf, grect)
            pygame.display.flip()
            gameSurface.blit(cartoon, (0, 0))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Blit the text.
            gameSurface.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(gameSurface, color, input_box, 5)

    
    def startButton():
        gameSurface.blit(Imguniverse, (0, 0))
        color_light = (170,170,170)
        color_dark = (100,100,100)
        # blue=(176,224,230)
        width = gameSurface.get_width()
        height = gameSurface.get_height()
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render('Start' , True , black)
        while True: 
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    
                #checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    
                    #if the mouse is clicked on the
                    # button the game is terminated
                    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                        return
            
            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()
            
            # if mouse is hovered on a button it
            # changes to lighter shade 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.draw.rect(gameSurface,color_light,[width/2,height/2,140,40])
            else:
                pygame.draw.rect(gameSurface,color_dark,[width/2,height/2,140,40])
            
            # superimposing the text onto our button

            gameSurface.blit(text, (width/2+40,height/2))


            
            # updates the frames of the game
            pygame.display.update()
                    
        
    

    def show_score(choice=1):
        sfont = pygame.font.SysFont('consolas', 20)
        ssurf = sfont.render('Score: {0}'.format(score), True, black)
        srect = ssurf.get_rect()
        if choice == 1:
            srect.midtop = (70, 20)
        else:
            srect.midtop = (360, 230)
        gameSurface.blit(ssurf, srect)

    startButton()
    speedUp = int(choose_level())

    while True:
        pygame.time.delay(speedUp)  # tốc độ chơi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # xử lý phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.evet.Event(pygame.QUIT))

        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
        # cập nhật vị trí mới
        if direction == 'RIGHT':
            snakepos[0] += m
        if direction == 'LEFT':
            snakepos[0] -= m
        if direction == 'UP':
            snakepos[1] -= m
        if direction == 'DOWN':
            snakepos[1] += m

        snakebody.insert(0, list(snakepos))
        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            score += 1
            foodflat = False
        elif snakepos[0] == foodpos1[0] and snakepos[1] == foodpos1[1]:#
            score += 1
            foodflat1 = False
        elif snakepos[0] == foodpos2[0] and snakepos[1] == foodpos2[1]:#
            score += 1
            foodflat2 = False
        else:
            snakebody.pop()

        # sản sinh covid
        if foodflat == False:
            foodx = random.randrange(1, 71)
            foody = random.randrange(1, 45)
            if foodx % 2 != 0: foodx += 1
            if foody % 2 != 0: foody += 1
            foodpos = [foodx * 10, foody * 10]
        foodflat = True
        if foodflat1 == False:
            foodx1 = random.randrange(1, 71)
            foody1 = random.randrange(1, 45)
            if foodx1 % 2 != 0: foodx1 += 1
            if foody1 % 2 != 0: foody1 += 1
            foodpos1 = [foodx1 * 10, foody1 * 10]  #
        foodflat1 = True
        if foodflat2 == False:
            foodx2 = random.randrange(1, 71)
            foody2 = random.randrange(1, 45)
            if foodx2 % 2 != 0: foodx2 += 1
            if foody2 % 2 != 0: foody2 += 1
            foodpos2 = [foodx2 * 10, foody2 * 10]  #
        foodflat2 = True

        gameSurface.blit(Imguniverse, (0, 0))
        for pos in snakebody:
            gameSurface.blit(Imgbody, pygame.Rect(pos[0], pos[1], m, m))
            # pygame.draw.rect(gameSurface,blue,pygame.Rect(pos[0],pos[1],m,m))
        gameSurface.blit(Imghead, pygame.Rect(snakebody[0][0], snakebody[0][1], m, m))  # head
        gameSurface.blit(Imgfood, pygame.Rect(foodpos[0], foodpos[1], m, m))
        gameSurface.blit(Imgfood, pygame.Rect(foodpos1[0], foodpos1[1], m, m)) #踩到不影响
        gameSurface.blit(Imgfood, pygame.Rect(foodpos2[0], foodpos2[1], m, m))

        # xử lý di chuyển đụng 4 cạnh biên
        if snakepos[0] > 880 or snakepos[0] < 10:
            game_over()
        if snakepos[1] > 605 or snakepos[1] < 10:
            game_over()

        for b in snakebody[1:]:
            if snakepos[0] == b[0] and snakepos[1] == b[1]:
                game_over()

        # đường viền
        # pygame.draw.rect(gameSurface, white, (10, 10, 715, 455), 2)
        show_score()
        pygame.display.flip()
main()