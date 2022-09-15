import pygame
from pygame import mixer
import sys
import random
import time
import pyautogui

pygame.init()
mixer.init()
Display_size = width, height = 1000,569

game_window = pygame.display.set_mode((Display_size))
pygame.display.set_caption("Snakes and Ladders")

clock = pygame.time.Clock()
fps = 30

pygame.display.update()

font = pygame.font.SysFont(None, 50)

white = (255, 255, 255)
red = (204, 0, 0)
black = (0, 0, 0)
yellow = (255, 205, 42)
# pink=(255,0,255)
pink = (180, 237, 227)
green = (157, 213, 42)
blue = (172, 84, 170)
gray = (203, 209, 208)
orange_yellow = (151, 168, 165)
orange_red = (255, 102, 0)



wlc_img = pygame.image.load("Resources/mainscreen.jpg").convert_alpha()
playmode_img = pygame.image.load("Resources/playmode.jpg").convert_alpha()
board_img = pygame.image.load("Resources/board.jpg").convert_alpha()
player1_img = pygame.image.load("Resources/player1.png").convert_alpha()
player1_goti_img = pygame.image.load("Resources/player1_goti.png").convert_alpha()
player2_img = pygame.image.load("Resources/player2.png").convert_alpha()
player2_goti_img = pygame.image.load("Resources/player2_goti.png").convert_alpha()
button_img = pygame.image.load("Resources/button.jpg").convert_alpha()
result_window = pygame.image.load("Resources/a.jpg").convert_alpha()
winner_emoji = pygame.image.load("Resources/winningemoji.png").convert_alpha()
computer_img= pygame.image.load("Resources/comp.png").convert_alpha()
computer_goti_img = pygame.image.load("Resources/comp.png").convert_alpha()
sound = pygame.image.load("Resources/soundoff.jpg").convert_alpha()
dice_1 = pygame.image.load("Resources/dice1.png").convert_alpha()
dice_2 = pygame.image.load("Resources/dice2.png").convert_alpha()
dice_3 = pygame.image.load("Resources/dice3.png").convert_alpha()
dice_4 = pygame.image.load("Resources/dice4.png").convert_alpha()
dice_5 = pygame.image.load("Resources/dice5.png").convert_alpha()
dice_6 = pygame.image.load("Resources/dice6.png").convert_alpha()

pygame.mixer.music.load("Resources/music.wav")
ladder_sound = pygame.mixer.Sound("Resources/ladder.wav")
snake_sound = pygame.mixer.Sound("Resources/snake.wav")
win_sound = pygame.mixer.Sound("Resources/win.wav")


input_rect = pygame.Rect(175, 270, 300, 60)
reset_rect = pygame.Rect(55, 400, 150, 45)
start_rect = pygame.Rect(255, 400, 150, 45)
exit_rect = pygame.Rect(455, 400, 150, 45)
quit_rect = pygame.Rect(400, 400, 150, 45)
play_again_rect = pygame.Rect(100, 400, 150, 45)

goti_1_pos_x = 10
goti_1_pos_x_prev = 10
goti_1_pos_y = 505
goti_1_pos_y_prev = 505
goti_2_pos_x = 30
goti_2_pos_x_prev = 30
goti_2_pos_y = 505
goti_2_pos_y_prev = 505
Score1 = 1
Score2 = 1
exit_game = False
first1 = False
first2 = False
turn = 1
direction1 = 0
direction2 = 0
prevScore1 = 1
prevScore2 = 1
music_on_off = True
player_comp = False


def text_screen(text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    text_scr = font.render(text, True, color)
    game_window.blit(text_scr, (x, y))



def RollDice():
    # dice_number = {dice_1:"dice_1", dice_2:"dice_2", dice_3:"dice_3", dice_4:"dice_4", dice_5:"dice_5", dice_6:"dice_6"}
    dice_number = [[dice_1,"dice_1"], [dice_2,"dice_2"], [dice_3,"dice_3"], [dice_4,"dice_4"], [dice_5,"dice_5"], [dice_6,"dice_6"]]
    dice_result = random.choice(dice_number)

    return dice_result

def Welcome_Screen():
    global music_on_off
    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

            else:
                game_window.blit(wlc_img, (0, 0))
                if music_on_off == False:
                    pygame.draw.line(game_window, white, (945, 23), (977, 55), 5)

                x, y = pygame.mouse.get_pos()
                print(x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                        if (463 < x < 548 ) and (410 < y < 500):

                            print("player select")
                            PlayMode()
                            break

                        if (945 < x < 980 ) and (23 < y < 54):
                            if music_on_off == True:
                                pygame.mixer.music.pause()
                                music_on_off = False


                            else:
                                pygame.mixer.music.unpause()
                                music_on_off = True
                            print("sound on/off")
                        if (28 < x < 59 ) and (23 < y < 55):
                            print("info")


                pygame.display.update()
                clock.tick(fps)

def PlayMode():
    global music_on_off, player_comp
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

            else:

                game_window.blit(playmode_img, (0, 0))
                game_window.blit(sound, (939, 18))
                if music_on_off == False:
                    pygame.draw.line(game_window, white, (945, 23), (977, 55), 5)
                x, y = pygame.mouse.get_pos()
                print(x,y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (945 < x < 980 ) and (23 < y < 54):
                            if music_on_off == True:
                                pygame.mixer.music.pause()
                                music_on_off = False


                            else:
                                pygame.mixer.music.unpause()
                                music_on_off = True
                        if (88 < x < 222) and (310 < y < 342):
                            print("player vs comp")
                            player_comp = True
                            Main_Game()
                        if (306 < x < 442) and (319 < y < 351):
                            print("player vs player")
                            Main_Game()
                        if (287 < x < 425) and (448 < y < 478):
                            print("back")
                            Welcome_Screen()
                            break


                pygame.display.update()
                clock.tick(fps)

def PlayerVSComp():

    pass

def PlayerVSPlayer():
    pass



def Game_Over(s):
    global goti_1_pos_x, goti_1_pos_y, goti_2_pos_y, goti_2_pos_x, Score1, Score2, turn, exit_game, first1, first2, goti_1_pos_x_prev, \
        goti_1_pos_y_prev, goti_2_pos_x_prev, goti_2_pos_y_prev, prevScore1, prevScore2, direction1, direction2, music_on_off

    pygame.mixer.Sound.play(win_sound)
    if s == Score1:
        if player_comp == True:
            text = "You Win!"
        else:
            text = "Player1 Win!"

    else:
        if player_comp == True:
            text = "Computer Win!"
        else:
            text = "Player1 Win!"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
            else:
                if music_on_off == False:
                    pygame.draw.line(game_window, white, (945, 23), (977, 55), 5)
                game_window.blit(result_window, (0, 0))
                text_screen(text, white, 355, 290,60)

                game_window.blit(winner_emoji, (412, 50))
                game_window.blit(sound, (939, 18))
                game_window.blit(button_img, (267, 420))
                game_window.blit(button_img, (592, 420))
                text_screen("New Game", white, 289, 429, 30)
                text_screen("Exit", white, 645, 429, 30)
                if music_on_off == False:
                    pygame.draw.line(game_window, white, (945, 23), (977, 55), 5)
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (945 < x < 980 ) and (23 < y < 54):
                            if music_on_off == True:
                                pygame.mixer.music.pause()
                                music_on_off = False


                            else:
                                pygame.mixer.music.unpause()
                                music_on_off = True
                        if (274 < x < 408) and (422 < y < 448):
                            print("new game")

                            goti_1_pos_x = 10
                            goti_1_pos_x_prev = 10
                            goti_1_pos_y = 505
                            goti_1_pos_y_prev = 505
                            goti_2_pos_x = 30
                            goti_2_pos_x_prev = 30
                            goti_2_pos_y = 505
                            goti_2_pos_y_prev = 505
                            Score1 = 1
                            Score2 = 1
                            exit_game = False
                            first1 = False
                            first2 = False
                            turn = 1
                            direction1 = 0
                            direction2 = 0
                            prevScore1 = 1
                            prevScore2 = 1
                            music_on_off = True
                            Welcome_Screen()
                            break
                        if (595 < x < 732) and (421 < y < 451):
                            print("exit")
                            sys.exit()
                            break


        pygame.display.update()
        clock.tick(fps)


def Snake(S, n):
    global Score1, Score2, prevScore1, prevScore2
    if S == 43:
        if n == 1:
            prevScore1 = 43
            Score1 = 17
            return 17, 'y'
        else:
            prevScore2 = 43
            Score2 = 17
            return 17, 'y'
    if S == 50:
        if n == 1:
            prevScore1 = 50
            Score1 = 5
            return 5, 'y'
        else:
            prevScore2 = 50
            Score2 = 5
            return 5, 'y'
    if S == 56:
        if n == 1:
            prevScore1 = 56
            Score1 = 8
            return 8, 'y'
        else:
            prevScore2 = 56
            Score2 = 8
            return 8, 'y'
    if S == 73:
        if n == 1:
            prevScore1 = 73
            Score1 = 15
            return 15, 'y'
        else:
            prevScore2 = 73
            Score2 = 15
            return 15, 'y'
    if S == 84:
        if n == 1:
            prevScore1 = 84
            Score1 = 58
            return 58, 'y'
        else:
            prevScore2 = 84
            Score2 = 58
            return 58, 'y'
    if S == 98:
        if n == 1:
            prevScore1 = 98
            Score1 = 40
            return 40, 'y'
        else:
            prevScore2 = 98
            Score2 = 40
            return 40, 'y'
    if S == 87:
        if n == 1:
            prevScore1 = 87
            Score1 = 49
            return 49, 'y'
        else:
            prevScore2 = 87
            Score2 = 49
            return 49, 'y'

    return S, 'n'


def travel(pS, nS, prev_x, prev_y, n):
    global direction1, direction2
    print(prev_x)
    print(prev_y)
    head = []
    player_lst = []
    while pS != nS:
        l1 = [0,1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29,30,41,42,43,44,45,46,47,48,49,50,61,62,63,64,65,66,67,68,69,70,81,82,83,84,85,86,87,88,89,90]
        l2 = [11,12,13,14,15,16,17,18,19,20,31,32,33,34,35,36,37,38,39,40,51,52,53,54,55,56,57,58,59,60,71,72,73,74,75,76,77,78,79,80,91,92,93,94,95,96,97,98,99]
        head = []
        if pS <= nS:
            if pS in l1:
                if n == 1:
                    direction1 = 0
                else:
                    direction2 = 0


                if direction1 == 0 and n == 1:
                    if pS in [10, 30, 50, 70, 90]:
                        prev_y -= 53
                    else:
                        prev_x += 53

                elif direction2 == 0 and n == 2:
                    if pS in [10, 30, 50, 70, 90]:
                        prev_y -= 53
                    else:
                        prev_x += 53
                print(prev_x,prev_y, pS)
                # head = []
                head.append(prev_x)
                head.append(prev_y)
                player_lst.append(head)
                pS += 1
                # if n == 1:
                #     game_window.blit(player1_goti_img, (prev_x, prev_y))
                #     pygame.display.update()
                # if n == 2:
                #     game_window.blit(player2_goti_img, (prev_x, prev_y))
                #     pygame.display.update()


            elif pS in l2:
                if n == 1:
                    direction1 = 1
                else:
                    direction2 = 1

                if direction1 == 1 and n == 1:
                    if pS in [20, 40, 60, 80]:
                        prev_y -= 53
                    else:
                        prev_x -= 53

                elif direction2 == 1 and n == 2:
                    if pS in [20, 40, 60, 80]:
                        prev_y -= 53
                    else:
                        prev_x -= 53
                print(prev_x,prev_y, pS)
                # head = []
                head.append(prev_x)
                head.append(prev_y)
                player_lst.append(head)
                pS += 1
                # if n == 1:
                #     game_window.blit(player1_goti_img, (prev_x, prev_y))
                #     pygame.display.update()
                # if n == 2:
                #     game_window.blit(player2_goti_img, (prev_x, prev_y))
                #     pygame.display.update()

        else:
            if pS in l1:
                if n == 1:
                    direction1 = 1
                else:
                    direction2 = 1



                if direction1 == 1 and n == 1:
                    if pS in [21, 41, 61, 81]:
                        prev_y += 53
                    else:
                        prev_x -= 53

                elif direction2 == 1 and n == 2:
                    if pS in [21, 41, 61, 81]:
                        prev_y += 53
                    else:
                        prev_x -= 53
                print(prev_x,prev_y, pS)
                # head = []
                head.append(prev_x)
                head.append(prev_y)
                player_lst.append(head)
                pS -= 1

                # if n == 1:
                #     game_window.blit(player1_goti_img, (prev_x, prev_y))
                #     pygame.display.update()
                # if n == 2:
                #     game_window.blit(player2_goti_img, (prev_x, prev_y))
                #     pygame.display.update()



            elif pS in l2:
                if n == 1:
                    direction1 = 0
                else:
                    direction2 = 0


                if direction1 == 0 and n == 1:
                    if pS in [11, 31, 51, 71, 91]:
                        prev_y += 53
                    else:
                        prev_x += 53

                elif direction2 == 0 and n == 2:
                    if pS in [11, 31, 51, 71, 91]:
                        prev_y += 53
                    else:
                        prev_x += 53
                print(prev_x,prev_y, pS)
                # head = []
                head.append(prev_x)
                head.append(prev_y)
                player_lst.append(head)
                pS -= 1
        if n == 1:
            # prev_x, prev_y = player_lst[-1]
            # for x, y in player_lst[0]:
            game_window.blit(player1_goti_img, (prev_x, prev_y))
            pygame.display.update()
        if n == 2:
            if player_comp == True:
                # prev_x, prev_y = player_lst[-1]
                # for x, y in player_lst[0]:
                game_window.blit(computer_goti_img, (prev_x, prev_y))
                pygame.display.update()
            else:
                # prev_x, prev_y = player_lst[-1]
                # for x, y in player_lst[0]:
                game_window.blit(player2_goti_img, (prev_x, prev_y))
                pygame.display.update()


        clock.tick(fps)


def Ladder(S, n):
    global Score1, Score2, prevScore1, prevScore2
    if S == 30:
        if n == 1:
            Score1 = 95
            prevScore1 = 30
            return 95, 'y'
        else:
            Score2 = 95
            prevScore2 = 30
            return 95, 'y'
    if S == 4:
        if n == 1:
            Score1 = 68
            prevScore1 = 4
            return 68, 'y'
        else:
            Score2 = 68
            prevScore2 = 4
            return 68, 'y'
    if S == 2:
        if n == 1:
            Score1 = 23
            prevScore1 = 2
            return 23, 'y'
        else:
            Score2 = 23
            prevScore2 = 2
            return 23, 'y'
    if S == 20:
        if n == 1:
            Score1 = 59
            prevScore1 = 20
            return 59, 'y'
        else:
            Score2 = 59
            prevScore2 = 20
            return 59, 'y'
    if S == 6:
        if n == 1:
            Score1 = 45
            prevScore1 = 6
            return 45, 'y'
        else:
            Score2 = 45
            prevScore2 = 6
            return 45, 'y'
    if S == 52:
        if n == 1:
            Score1 = 72
            prevScore1 = 52
            return 72, 'y'
        else:
            Score2 = 72
            prevScore2 = 52
            return 72, 'y'
    if S == 71:
        if n == 1:
            Score1 = 92
            prevScore1 = 71
            return 92, 'y'
        else:
            Score2 = 92
            prevScore2 = 71
            return 92, 'y'
    if S == 57:
        if n == 1:
            Score1 = 96
            prevScore1 = 57
            return 96, 'y'
        else:
            Score2 = 96
            prevScore2 = 57
            return 96, 'y'
    return S , 'n'


def MovePlayer(Score, n, d):
    game_window.blit(d[0], (720, 200))
    print(str(n) +" " + str(Score))
    global goti_1_pos_x, goti_1_pos_y, goti_2_pos_x, goti_2_pos_y,  goti_1_pos_x_prev, goti_1_pos_y_prev, goti_2_pos_x_prev, goti_2_pos_y_prev, exit_game
    l1 = [ [0, 0],[20, 505],[73,505],[126,505],[179,505],[232,505],[285,505],[338,505],[391,505],[444,505],[497,505],
          [497, 452], [444, 452], [391, 452], [338, 452], [285, 452], [232, 452], [179, 452], [126, 452], [73, 452], [20, 452],
          [20, 399], [73, 399], [126, 399], [179, 399], [232, 399], [285, 399], [338, 399], [391, 399], [444, 399], [497, 399],
          [497, 346], [444, 346], [391, 346], [338, 346], [285, 346], [232, 346], [179, 346], [126, 346], [73, 346], [20, 346],
          [20, 293], [73, 293], [126, 293], [179, 293], [232, 293], [285, 293], [338, 293], [391, 293], [444, 293], [497, 293],
          [497, 240], [444, 240], [391, 240], [338, 240], [285, 240], [232, 240], [179, 240], [126, 240], [73, 240], [20, 240],
          [20, 187], [73, 187], [126, 187], [179, 187], [232, 187], [175, 187], [338, 187], [391, 187], [444, 187], [497, 187],
          [497, 134], [444, 134], [391, 134], [338, 134], [285, 134], [232, 134], [179, 134], [126, 134], [73, 134], [20, 134],
          [20, 81], [73, 81], [126, 81], [179, 81], [232, 81], [285, 81], [338, 81], [391, 81], [444, 81], [497, 81],
          [497, 28], [444, 28], [391, 28], [338, 28], [285, 28], [232, 28], [179, 28], [126, 28], [73, 28], [20, 28] ]


    if n == 1:

        l2 = l1[Score]
        goti_1_pos_x_prev = goti_1_pos_x
        goti_1_pos_y_prev = goti_1_pos_y

        goti_1_pos_x = l2[0]
        goti_1_pos_y = l2[1]

        travel(prevScore1, Score, goti_1_pos_x_prev, goti_1_pos_y_prev, n)
        Score, res1 = Snake(Score, n)
        Score, res2 = Ladder(Score, n)

        if res1 == 'y' or res2 == 'y':
            game_window.blit(d[0], (720, 200))
            if res1 == 'y':
                pygame.mixer.Sound.play(snake_sound)
            else:
                pygame.mixer.Sound.play(ladder_sound)
            l2 = l1[Score]

            goti_1_pos_x_prev = goti_1_pos_x
            goti_1_pos_y_prev = goti_1_pos_y
            goti_1_pos_x = l2[0]
            goti_1_pos_y = l2[1]
            time.sleep(1)
            travel(prevScore1, Score, goti_1_pos_x_prev, goti_1_pos_y_prev, n)


    else:
        l2 = l1[Score]
        goti_2_pos_x_prev = goti_2_pos_x
        goti_2_pos_y_prev = goti_2_pos_y

        goti_2_pos_x = l2[0]
        goti_2_pos_y = l2[1]

        travel(prevScore2, Score, goti_2_pos_x_prev, goti_2_pos_y_prev, n)
        Score, res1 = Snake(Score, n)
        Score, res2 = Ladder(Score, n)

        if res1 == 'y' or res2 == 'y':
            game_window.blit(d[0], (720, 200))
            if res1 == 'y':
                pygame.mixer.Sound.play(snake_sound)
            else:
                pygame.mixer.Sound.play(ladder_sound)
            l2 = l1[Score]


            goti_2_pos_x_prev = goti_2_pos_x
            goti_2_pos_y_prev = goti_2_pos_y

            goti_2_pos_x = l2[0]
            goti_2_pos_y = l2[1]
            time.sleep(1)
            travel(prevScore2, Score, goti_2_pos_x_prev, goti_2_pos_y_prev, n)

    pygame.display.update()
    clock.tick(fps)


def Main_Game():
    global goti_1_pos_x, goti_1_pos_y, goti_2_pos_y, goti_2_pos_x,Score1, Score2, turn, exit_game, first1, first2, goti_1_pos_x_prev,\
        goti_1_pos_y_prev,goti_2_pos_x_prev,goti_2_pos_y_prev, prevScore1, prevScore2, direction1, direction2, music_on_off
    dice_num = RollDice()
    game_window.fill(black)
    myRectangle1 = pygame.Rect(630, 20, 110, 90)
    myRectangle2 = pygame.Rect(820, 20, 110, 90)
    pygame.draw.rect(game_window, white, myRectangle1, 2)

    while exit_game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

            else:


                game_window.blit(board_img, (0, 0))

                game_window.blit(player1_img, (656, 25))
                game_window.blit(sound, (939, 18))
                if player_comp == True:
                    game_window.blit(computer_img, (851, 25))
                    text_screen("Comp", yellow, 842, 80, 35)
                    text_screen("You", green, 660, 80, 35)
                else:
                    text_screen("Player 1", green, 640, 80, 35)
                    text_screen("Player 2", yellow, 832, 80, 35)

                    game_window.blit(player2_img, (851, 25))
                game_window.blit(button_img, (617, 493))
                game_window.blit(button_img, (810, 493))
                game_window.blit(dice_num[0], (720, 200))
                text_screen("Vs", red, 758,45, 40)

                text_screen("New Game", white, 639, 502, 30)
                text_screen("Exit", white, 861, 502, 30)
                if music_on_off == False:
                    pygame.draw.line(game_window, white, (945, 23), (977, 55), 5)
                if first1 == True:

                    game_window.blit(player1_goti_img, (goti_1_pos_x, goti_1_pos_y))
                if first2 == True:
                    if player_comp == True:
                        game_window.blit(computer_goti_img, (goti_2_pos_x, goti_2_pos_y))
                    else:
                        game_window.blit(player2_goti_img, (goti_2_pos_x, goti_2_pos_y))
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (945 < x < 980 ) and (23 < y < 54):
                            if music_on_off == True:
                                pygame.mixer.music.pause()
                                music_on_off = False


                            else:
                                pygame.mixer.music.unpause()
                                music_on_off = True
                        if (619 < x < 756) and (493 < y < 523):
                            print("new game")

                            goti_1_pos_x = 10
                            goti_1_pos_x_prev = 10
                            goti_1_pos_y = 505
                            goti_1_pos_y_prev = 505
                            goti_2_pos_x = 30
                            goti_2_pos_x_prev = 30
                            goti_2_pos_y = 505
                            goti_2_pos_y_prev = 505
                            Score1 = 1
                            Score2 = 1
                            exit_game = False
                            first1 = False
                            first2 = False
                            turn = 1
                            direction1 = 0
                            direction2 = 0
                            prevScore1 = 1
                            prevScore2 = 1
                            music_on_off = True
                            Welcome_Screen()
                            break
                        if (812 < x < 951) and (493 < y < 523):
                            print("exit")
                            sys.exit()
                            break
                        if (287 < x < 425) and (448 < y < 478):
                            print("back")
                            Welcome_Screen()
                            break

                        if (736 < x < 829) and (200 < y < 319):

                            if (turn == 2):


                                dice_num = RollDice()

                                print(dice_num[1])

                                if first2 == False:
                                    if dice_num[1] == "dice_6":
                                        first2 = True
                                else:
                                    prevScore2 = Score2
                                    print(str(prevScore2))
                                    if dice_num[1] == "dice_1":
                                        Score2 += 1
                                        # MovePlayer(Score2, 2)


                                    elif dice_num[1] == "dice_2":
                                        Score2 += 2
                                        # MovePlayer(Score2, 2)

                                    elif dice_num[1] == "dice_3":
                                        Score2 += 3
                                        # MovePlayer(Score2, 2)


                                    elif dice_num[1] == "dice_4":
                                        Score2 += 4
                                        # MovePlayer(Score2, 2)


                                    elif dice_num[1] == "dice_5":
                                        Score2 += 5
                                        # MovePlayer(Score2, 2)


                                    elif dice_num[1] == "dice_6":
                                        Score2  += 6
                                        # MovePlayer(Score2, 2)
                                    if Score2 > 100:
                                        Score2 = prevScore2

                                        # MovePlayer(Score2, turn,dice_num)
                                    elif Score2 == 100:
                                        MovePlayer(Score2, turn, dice_num)
                                        time.sleep(2)
                                        Game_Over(Score2)
                                        exit_game = True
                                        break
                                    else:
                                        MovePlayer(Score2, turn, dice_num)
                                    print(Score2)

                                if dice_num[1] == "dice_6":
                                    turn = 2
                                    pygame.draw.rect(game_window, black, myRectangle1, 2)
                                    pygame.draw.rect(game_window, white, myRectangle2, 2)
                                else:
                                    turn = 1
                                    pygame.draw.rect(game_window, white, myRectangle1, 2)
                                    pygame.draw.rect(game_window, black, myRectangle2, 2)



                            else:
                                dice_num = RollDice()
                                print(dice_num[1])

                                if first1 == False:
                                    if dice_num[1] == "dice_6":
                                        first1 = True
                                else:
                                    prevScore1 = Score1
                                    # print(str(prevScore1))
                                    if dice_num[1] == "dice_1":
                                        Score1 += 1
                                        # MovePlayer(Score1, 1)
                                    elif dice_num[1] == "dice_2":
                                        Score1 += 2
                                        # MovePlayer(Score1, 1)
                                    elif dice_num[1] == "dice_3":
                                        Score1 += 3
                                        # MovePlayer(Score1, 1)
                                    elif dice_num[1] == "dice_4":
                                        Score1 += 4
                                        # MovePlayer(Score1, 1)
                                    elif dice_num[1] == "dice_5":
                                        Score1 += 5
                                        # MovePlayer(Score1, 1)
                                    elif dice_num[1] == "dice_6":
                                        Score1 += 6

                                        # MovePlayer(Score1, 1)
                                    print(Score1)

                                    if Score1>100:
                                        Score1 = prevScore1
                                        MovePlayer(Score1, turn, dice_num)
                                    elif Score1 == 100:
                                        MovePlayer(Score1, turn, dice_num)
                                        time.sleep(2)
                                        Game_Over(Score1)
                                        exit_game = True
                                        break
                                    else:
                                        MovePlayer(Score1, turn, dice_num)
                                if dice_num[1] == "dice_6":
                                    turn = 1
                                    pygame.draw.rect(game_window, white, myRectangle1, 2)
                                    pygame.draw.rect(game_window, black, myRectangle2, 2)
                                else:
                                    turn = 2
                                    pygame.draw.rect(game_window, black, myRectangle1, 2)
                                    pygame.draw.rect(game_window, white, myRectangle2, 2)
                pygame.display.update()
                clock.tick(fps)


while True:
    Welcome_Screen()
    # Main_Game()
    # Game_Over("Score1")


