import pygame

game = None


class Player:
    x = 0
    y = 0
    move_speed = 4
    focus_speed = 2
    focused = False

    def update(self):
        input_state = pygame.key.get_pressed()
        self.focused = input_state[pygame.K_LSHIFT]
        spd = self.focus_speed if self.focused else self.move_speed
        self.x += spd * (input_state[pygame.K_RIGHT] - input_state[pygame.K_LEFT])
        self.y += spd * (input_state[pygame.K_DOWN] - input_state[pygame.K_UP])

    def draw(self, screen):
        screen.blit(game.marisa_image, (self.x, self.y))


class Bullet:
    x = 0
    y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (0, 0), 10)


class Game:
    player = Player()
    screen = None
    marisa_image = None
    bullet = Bullet()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Grungich")

        self.marisa_image = pygame.image.load("marisa.png")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()
            pygame.time.delay(10)

    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        self.bullet.draw(self.screen)
        pygame.display.update()


game = Game()
game.run()

