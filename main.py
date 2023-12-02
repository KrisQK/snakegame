import pygame
import random

# 初始化Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 设置屏幕尺寸和方块大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 定义贪吃蛇类
class Snake:
    def __init__(self):
        self.length = 1  # 蛇的初始长度
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]  # 蛇的初始位置
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 蛇的初始移动方向
        self.color = GREEN  # 蛇的颜色

    def get_head_position(self):
        return self.positions[0]  # 返回蛇头位置

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        # 计算蛇头的新位置
        new = (((cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()  # 如果蛇碰到自己，则重置游戏
        else:
            self.positions.insert(0, new)  # 将新位置添加到蛇头
            if len(self.positions) > self.length:
                self.positions.pop()  # 删除蛇尾

    def reset(self):
        self.length = 1  # 重置蛇的长度
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]  # 重置蛇的位置
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # 随机选择蛇的初始移动方向

    def draw(self, surface):
        for p in self.positions:
            # 绘制蛇的每一节身体
            pygame.draw.rect(surface, self.color, pygame.Rect(p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

    def handle_keys(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = UP  # 向上移动
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = DOWN  # 向下移动
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = LEFT  # 向左移动
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = RIGHT  # 向右移动

# 定义食物类
class Food:
    def __init__(self):
        self.position = (0, 0)  # 食物的初始位置
        self.color = RED  # 食物的颜色
        self.randomize_position()  # 随机设置食物位置

    def randomize_position(self):
        # 在随机位置设置食物，确保食物在网格中
        self.position = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self, surface):
        # 绘制食物
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# 定义方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    running = True
    clock = pygame.time.Clock()
    snake = Snake()  # 初始化蛇对象
    food = Food()  # 初始化食物对象

    while running:
        screen.fill(BLACK)  # 清屏

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        snake.handle_keys(keys)  # 处理按键事件

        snake.update()  # 更新蛇的位置
        snake.draw(screen)  # 绘制蛇
        food.draw(screen)  # 绘制食物

        # 检查蛇是否吃到食物
        if snake.get_head_position() == food.position:
            snake.length += 1  # 蛇长度加一
            food.randomize_position()  # 随机设置新的食物位置

        pygame.display.update()
        clock.tick(FPS)  # 控制游戏帧率

    pygame.quit()

if __name__ == "__main__":
    main()
