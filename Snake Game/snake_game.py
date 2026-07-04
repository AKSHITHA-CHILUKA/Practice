import random
import sys
import pygame

# Config
CELL_SIZE = 20
GRID_WIDTH = 32  # 32 * 20 = 640
GRID_HEIGHT = 24  # 24 * 20 = 480
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 30, 30)
GREEN = (40, 180, 40)


class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.reset()

    def reset(self):
        self.direction = (1, 0)
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.generate_food()
        self.score = 0
        self.game_over = False

    def generate_food(self):
        while True:
            pos = (random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT))
            if pos not in self.snake:
                self.food = pos
                return

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP) and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif event.key in (pygame.K_s, pygame.K_DOWN) and self.direction != (0, -1):
                    self.direction = (0, 1)
                elif event.key in (pygame.K_a, pygame.K_LEFT) and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif event.key in (pygame.K_d, pygame.K_RIGHT) and self.direction != (-1, 0):
                    self.direction = (1, 0)
                elif event.key == pygame.K_r and self.game_over:
                    self.reset()

    def update(self):
        if self.game_over:
            return
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Check wall collision
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            return

        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.generate_food()
        else:
            self.snake.pop()

    def draw_cell(self, pos, color):
        x, y = pos
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, color, rect)

    def draw(self):
        self.screen.fill(BLACK)
        # Draw food
        self.draw_cell(self.food, RED)
        # Draw snake
        for seg in self.snake:
            self.draw_cell(seg, GREEN)

        # Score
        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surf, (8, 8))

        if self.game_over:
            over_surf = self.font.render("Game Over - Press R to restart", True, WHITE)
            rect = over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(over_surf, rect)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)


def main():
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()
