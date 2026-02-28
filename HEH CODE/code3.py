'''import pandas as pd
import matplotlib.pyplot as plt

# Nhập dữ liệu từ bảng bạn gửi
data = {
    "TÊN VẬT TƯ": ["Butyl", "Keo bàn", "Vải bàn", "Dao in máy", "Băng dính", 
                   "Keo dán lưới", "Keo chụp khung", "Giấy Flock", 
                   "Các vật tư in khác", "Thêu"],
    "T1": [0, 14600000, 21800000, 10550000, 0, 21560000, 53550000, 0, 158545500, 12600000],
    "T2": [2825000, 14600000, 21800000, 28700000, 0, 29500000, 31500000, 0, 119825000, 12600000],
    "T3": [5650000, 5400000, 21800000, 21400000, 4984000, 35400000, 31500000, 0, 68300000, 22354000],
    "T4": [3955000, 14160000, 19620000, 11400000, 11715000, 29500000, 25200000, 190000, 11402000, 27726000],
    "T5": [5650000, 9912000, 15260000, 9750000, 2700000, 23600000, 22050000, 0, 149761000, 15990000],
    "T6": [5650000, 8904000, 6540000, 5700000, 2700000, 23600000, 9450000, 0, 10163000, 43446000],
    "T7": [6636000, 10800000, 13275000, 11937000, 3935000, 29500000, 15750000, 0, 13653000, 22810000],
    "T8": [11060000, 13632000, 6637500, 5000000, 3935000, 22050000, 22050000, 4135000, 22792400, 16350000],
    "T9": [11060000, 16900000, 13275000, 6200000, 2585000, 35400000, 28350000, 0, 8881000, 47525000]
}

df = pd.DataFrame(data)

# Chuyển dữ liệu sang dạng dọc (long format)
df_long = df.melt(id_vars="TÊN VẬT TƯ", var_name="Tháng", value_name="Chi phí")

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))
for name, group in df_long.groupby("TÊN VẬT TƯ"):
    plt.plot(group["Tháng"], group["Chi phí"], marker="o", label=name)

plt.title("Chi phí theo tháng của từng loại vật tư")
plt.xlabel("Tháng")
plt.ylabel("Chi phí (VND)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()'''

import pygame
import sys
import time
import math

pygame.init()

WIDTH, HEIGHT = 1500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hien chu tung tu + Trai tim")

font = pygame.font.SysFont("Arial", 80)

lyrics = [
    "Vi anh dau co biet trai tim ngon ngang",
    "Vi anh dau co biet dung sai ngo ngang",
    "Vi anh luon hoi tiec chiec om do dang",
    "Chim trong doi mat biec anh khong the mang",
    "Vi anh dau co biet giau di thoi gian",
    "Vi anh dau co biet nang mai dang tan",
    "Vi anh luon hoi tiec anh khong the mang",
    "Mui huong tren mai toc giu theo cau chuyen",
    "Đanh roi",
]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 20, 60)

word_delay = 0.3

'''def draw_heart(surface, x, y, size, color):
    """Vẽ trái tim đơn giản bằng 2 circle + 1 tam giác"""
    top_radius = size // 2
    pygame.draw.circle(surface, color, (x - top_radius, y), top_radius)
    pygame.draw.circle(surface, color, (x + top_radius, y), top_radius)
    points = [
        (x - size, y), 
        (x + size, y), 
        (x, y + size * 1.5)
    ]
    pygame.draw.polygon(surface, color, points)
'''
for line in lyrics:
    words = line.split()
    displayed = ""

    for word in words:
        displayed += word + " "
        start_time = time.time()
        showing = True
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(BLACK)
            text_surface = font.render(displayed.strip(), True,(255,255,255))
            rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text_surface, rect)
            blink = int(time.time() * 2) % 2 
            '''if blink:
                draw_heart(screen, WIDTH//2, HEIGHT - 100, 40, RED)'''

            pygame.display.flip()

            if time.time() - start_time > word_delay:
                showing = False

    time.sleep(0.6)

pygame.quit()
sys.exit()