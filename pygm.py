import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

block = [[None, None, None], [None, None, None], [None, None, None]]

fonts = pygame.font.Font('OpenSans-Regular.ttf', 40)
run = True
mm = True
pp = False
jj = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if mm:
        text = fonts.render("Saroj Katwal", True, (255, 0, 0), (0, 255, 0))
        playButton = pygame.Rect(500 / 2 - 80, 500 / 2, 160, 160)
        textRect = text.get_rect()
        textRect.center = playButton.center
        win.fill((200, 200, 200))
        pygame.draw.rect(win, (0, 0, 0), playButton)
        win.blit(text, textRect)
        pygame.display.update()

    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
        if playButton.collidepoint(mouse):
            pp = True
            mm = False
    if pp:
        if jj:
            win.fill((200, 200, 200))

        size_b = 100
        ipos = (500 / 2 - 1.5 * size_b, 500 / 2 - 1.5 * size_b)
        alls = []
        for i in range(3):
            rows = []
            for j in range(3):
                rectA = pygame.Rect(ipos[0] + j * size_b, ipos[1] + i * size_b, size_b, size_b)
                pygame.draw.rect(win, (0, 0, 0), rectA, 1)
                rows.append(rectA)
            alls.append(rows)

        for i in range(3):
            for j in range(3):
                if block[i][j] is not None:
                    txt = fonts.render(block[i][j], True, (0, 255, 255))
                    txtRect = txt.get_rect()
                    txtRect.center = alls[i][j].center
                    win.blit(txt, txtRect)

        pygame.display.update()
        if click == 1:
            for i in range(3):
                for j in range(3):
                    if alls[i][j].collidepoint(mouse):
                        pygame.draw.rect(win, (255, 0, 0), alls[i][j])
                        block[i][j] = 'X'
            pygame.display.update()

pygame.quit()
