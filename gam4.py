import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Thay Quần Áo")

# Màu nền
WHITE = (255, 255, 255)

# Load ảnh nhân vật và quần áo
character_base = pygame.image.load("game/chimbe.jpg")
shirt1 = pygame.image.load("game/h1.jpg")
shirt2 = pygame.image.load("game/h2.jpg")
pants1 = pygame.image.load("game/h1.jpg")
pants2 = pygame.image.load("game/h2.jpg")

# Kích thước và vị trí hiển thị nhân vật
character_rect = character_base.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Các tùy chọn quần áo
shirts = [shirt1, shirt2]
pants = [pants1, pants2]
current_shirt = 0
current_pants = 0

# Hàm hiển thị nhân vật với quần áo hiện tại
def draw_character():
    screen.fill(WHITE)
    screen.blit(character_base, character_rect)

    # Hiển thị áo
    if shirts[current_shirt]:
        screen.blit(shirts[current_shirt], character_rect)
    # Hiển thị quần
    if pants[current_pants]:
        screen.blit(pants[current_pants], character_rect)
    
    pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Đổi áo bằng phím trái/phải
            if event.key == pygame.K_LEFT:
                current_shirt = (current_shirt - 1) % len(shirts)
            elif event.key == pygame.K_RIGHT:
                current_shirt = (current_shirt + 1) % len(shirts)
            # Đổi quần bằng phím lên/xuống
            elif event.key == pygame.K_UP:
                current_pants = (current_pants - 1) % len(pants)
            elif event.key == pygame.K_DOWN:
                current_pants = (current_pants + 1) % len(pants)

    draw_character()

pygame.quit()
sys.exit()
