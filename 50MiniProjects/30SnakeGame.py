import curses
import random
import time

class Snake:
    def __init__(self, window):
        self.window = window
        self.snake_body = [(4, 10), (4, 9), (4, 8)]
        self.direction = curses.KEY_RIGHT
        self.score = 0

    def move(self):
        head_y, head_x = self.snake_body[0]
        if self.direction == curses.KEY_RIGHT:
            new_head = (head_y, head_x + 1)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head_y, head_x - 1)
        elif self.direction == curses.KEY_UP:
            new_head = (head_y - 1, head_x)
        elif self.direction == curses.KEY_DOWN:
            new_head = (head_y + 1, head_x)
        self.snake_body.insert(0, new_head)
        self.snake_body.pop()

    def grow(self):
        tail_y, tail_x = self.snake_body[-1]
        self.snake_body.append((tail_y, tail_x))

    def draw(self):
        for y, x in self.snake_body:
            self.window.addch(y, x, curses.ACS_CKBOARD)

    def check_collision(self):
        head_y, head_x = self.snake_body[0]
        if head_y in [0, curses.LINES - 1] or head_x in [0, curses.COLS - 1]:
            return True
        if (head_y, head_x) in self.snake_body[1:]:
            return True
        return False

    def change_direction(self, key):
        if key == curses.KEY_RIGHT and self.direction != curses.KEY_LEFT:
            self.direction = curses.KEY_RIGHT
        elif key == curses.KEY_LEFT and self.direction != curses.KEY_RIGHT:
            self.direction = curses.KEY_LEFT
        elif key == curses.KEY_UP and self.direction != curses.KEY_DOWN:
            self.direction = curses.KEY_UP
        elif key == curses.KEY_DOWN and self.direction != curses.KEY_UP:
            self.direction = curses.KEY_DOWN

    def get_head(self):
        return self.snake_body[0]

    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

class Food:
    def __init__(self, window, snake_body):
        self.window = window
        self.snake_body = snake_body
        self.food = None
        self.generate_food()

    def generate_food(self):
        while True:
            food_y = random.randint(1, curses.LINES - 2)
            food_x = random.randint(1, curses.COLS - 2)
            if (food_y, food_x) not in self.snake_body:
                self.food = (food_y, food_x)
                break

    def draw(self):
        food_y, food_x = self.food
        self.window.addch(food_y, food_x, curses.ACS_PI)

    def get_position(self):
        return self.food

def game_loop(window):
    curses.curs_set(0)
    window.timeout(100)
    snake = Snake(window)
    food = Food(window, snake.snake_body)
    score_window = curses.newwin(1, curses.COLS, 0, 0)
    score_window.addstr(0, 0, f"Score: {snake.get_score()}")
    food.draw()
    snake.draw()

    while True:
        key = window.getch()
        if key == 27:  # ESC key to exit
            break
        snake.change_direction(key)
        snake.move()
        if snake.get_head() == food.get_position():
            snake.grow()
            snake.increase_score()
            food.generate_food()
            score_window.clear()
            score_window.addstr(0, 0, f"Score: {snake.get_score()}")
        if snake.check_collision():
            break
        window.clear()
        food.draw()
        snake.draw()

    window.clear()
    window.addstr(curses.LINES // 2, curses.COLS // 2 - 5, "Game Over")
    window.refresh()
    time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(game_loop)
