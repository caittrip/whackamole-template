import pygame
import random
# comments
def main():
    try:
        pygame.init()

        x,y = 0,0

        mole_image = pygame.image.load("mole.png")

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        cols, rows = 20, 16
        cells = 32


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_square = pygame.Rect(x * cells, y * cells, cells, cells)

                    if mole_square.collidepoint(mouse_x, mouse_y):
                        x = random.randint(0, cols - 1)
                        y = random.randint(0, rows - 1)

            screen.fill("light green")
            for col in range(cols + 1):
                pygame.draw.line(screen, "black", (col * cells, 0), (col * cells, rows * cells))
            for row in range(rows + 1):
                pygame.draw.line(screen, "black", (0, row * cells), (cols * cells, row * cells))
            mole_position = (x * cells, y * cells)
            screen.blit(mole_image, mole_position)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
