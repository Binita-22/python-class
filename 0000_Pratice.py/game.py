import os
import random
import threading
import time
from collections import deque


class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = deque([(height // 2, width // 2)])
        self.direction = (0, 1)  # (row, col) - start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.running = True

        # Game speed (lower is faster)
        self.speed = 0.2

    def generate_food(self):
        while True:
            food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if food not in self.snake:
                return food

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_game(self):
        self.clear_screen()

        # Create game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Draw borders
        for i in range(self.height):
            board[i][0] = '█'
            board[i][self.width - 1] = '█'
        for j in range(self.width):
            board[0][j] = '█'
            board[self.height - 1][j] = '█'

        # Draw snake
        for i, (row, col) in enumerate(self.snake):
            if i == 0:  # Head
                board[row][col] = '●'
            else:  # Body
                board[row][col] = '○'

        # Draw food
        board[self.food[0]][self.food[1]] = '◆'

        # Print board
        for row in board:
            print(''.join(row))

        print(f"\nScore: {self.score}")
        print("Controls: W(up) A(left) S(down) D(right) Q(quit)")
        print("Press Enter after each move")

        if self.game_over:
            print(f"\n{'=' * 30}")
            print("GAME OVER!")
            print(f"Final Score: {self.score}")
            print(f"{'=' * 30}")

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # Check collision with walls
        if (new_head[0] <= 0 or new_head[0] >= self.height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.width - 1):
            self.game_over = True
            return

        # Check collision with self
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.appendleft(new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
            # Increase speed slightly
            self.speed = max(0.05, self.speed - 0.01)
        else:
            self.snake.pop()

    def get_input(self):
        """Get input in a separate thread"""
        while self.running and not self.game_over:
            try:
                move = input().strip().lower()
                if move == 'w' and self.direction != (1, 0):
                    self.direction = (-1, 0)
                elif move == 's' and self.direction != (-1, 0):
                    self.direction = (1, 0)
                elif move == 'a' and self.direction != (0, 1):
                    self.direction = (0, -1)
                elif move == 'd' and self.direction != (0, -1):
                    self.direction = (0, 1)
                elif move == 'q':
                    self.game_over = True
                    self.running = False
                    break
            except (EOFError, KeyboardInterrupt):
                self.game_over = True
                self.running = False
                break

    def play(self):
        print("Welcome to Snake Game!")
        print("Loading...")
        time.sleep(1)

        # Start input thread
        input_thread = threading.Thread(target=self.get_input, daemon=True)
        input_thread.start()

        while self.running and not self.game_over:
            self.draw_game()
            self.move_snake()
            time.sleep(self.speed)

        # Final display
        self.draw_game()

        print("\nThanks for playing!")
        print("Press Enter to exit...")
        try:
            input()
        except (EOFError, KeyboardInterrupt):
            pass


def main():
    try:
        game = SnakeGame()
        game.play()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()
