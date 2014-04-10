import pygame

def viewer(draw, width=500, height=500):
    width, height = 500, 500
    running = True

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    mouse_start = None
    mouse = None
    pygame.scrap.init()
    while running:
        try:
            screen.fill((255, 255, 255))

            elements = draw()
            for element in elements:
                element.draw(screen)

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_start = mouse
                elif event.type == pygame.MOUSEBUTTONUP:
                    size = (
                        abs(mouse[0] - mouse_start[0]),
                        abs(mouse[1] - mouse_start[1])
                    )
                    cropped = pygame.Surface(size)
                    cropped.blit(screen, (0, 0), (
                        min(mouse_start[0], mouse[0]),
                        min(mouse_start[1], mouse[1]),
                        size[0], 
                        size[1]
                    ))
                    pygame.image.save(cropped, "temp.bmp")
                    with open("temp.bmp", "rb") as fp:
                        pygame.scrap.put(pygame.SCRAP_BMP, fp.read())
                    mouse = None
                    mouse_start = None
         
            if mouse and mouse_start and mouse_start != mouse:
                pygame.draw.lines(screen, (0, 255, 0), True, [
                    mouse_start,
                    (mouse[0], mouse_start[1]),
                    mouse,
                    (mouse_start[0], mouse[1]),
                ])
            

            pygame.display.flip()
        except KeyboardInterrupt:
            running = False