'''from PIL import Image, ImageSequence
import time
import os

def get_ascii_char(brightness, ascii_chars):
    """
    chuyển độ sáng pixel thành kí tự ascii.
    """
    brightness = max(0.0, min(1.0, brightness))
    return ascii_chars[int(brightness * (len(ascii_chars) - 1))]

def gif_to_ascii_loop(gif_path, output_width = 70, frame_delay=0.04):
    """
    chuyển đổi ảnh gif thành hoạt hình ascii đen trắng và lặp lại liên tục.
    tối ưu cho tốc độ nhanh và background là màu đen của terminal
    """
    ascii_chars = ".'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    if not os.path.exists(gif_path):
        print(f"")
        print("vui lòng kiểm tra lại đường dẫn và tên file. ")
        print("đảm bảo file gif nằm trong cùng thư mục với script python này, ")
        print("hoặc cung cấp đường dây dẫn đầy đủ và chính xác. ")
        return
    
    try:
        img = Image.open(gif_path)
    except Exception as e:
        print(f"lỗi khi mở file gif '{gif_path}': {e}")
        return

    frame = []

    for frame in ImageSequence.Iterator(img):
        gray_frame = frame.convert("L")
        width, height = gray_frame.size
        aspect_raito = height / width
        output_height = int(output_width * aspect_raito * 0.55)

        for pixel_value in pixels:
            brightness = pixel_value / 255.0
            ascii_char = get_ascii_char(brightness, ascii_chars)
            ascii_frame_chars.append(ascii_char)
        
        ascii_str = ""
        for i in range(len(ascii_frame_chars)):
            ascii_str += ascii_frame_chars[i]
            if(i+1) % output_width == 0:
                ascii_str += "\n"
        frames.append(ascii_str)

    print("\n" * 2)

    try:
        while True:
            for ascii_frame_str in frames:
                print("\033[H\033[J", end = "")
                print(ascii_frame_str)
                time.sleep(frame_delay)
    except KeyboardInterrupt:
        print("\033[H\033[J", end = "")
        print("\nhoạt hình ascii đã dừng")
        print("nhấn Crtl+C để thoát")
    except Exception as e:
        print(f"\nđã xảy ra lỗi: {e}")
if __name__ == "__main__":
    gif_file = "Download-unscreen.gif"
    gif_to_ascii_loop(gif_file, output_width=70, frame_delay=0.04)'''

'''
import math
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(100000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        color("red")
        goto(0,0)
        (done)'''

'''class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):                  #def (show) to show fraction
        print(self.num, "/", self.den)                          #both to transfer fraction into string to show
    def __str__(self):               #def (str) to show fraction
        return str(self.num) + "/" + str(self.den)
fr = Fraction(3,5)
fr.show()'''

'''
def gcd(m,n): 
    while m % n != 0:
        old_m = m
        old_n = n 
        m = old_n
        n = old_m % old_n
    return n

class fraction:
    def __init__ (self,top,bottom):
        self.num = top
        self.den = bottom
    def __str__ (self):
        return str(self.num) + "/" + str(self.den)
    def __add__ (self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return fraction(new_num // common, new_den // common)
    def compare (self,other):
        first_num = self.num * other.den   
        second_num = other.num  * self.den
        if first_num < second_num:
            return str(first_num) + "<" + str(second_num)
        if first_num > second_num:
            return str(first_num) + ">" + str(second_num)
        else:
            return str(first_num) + "=" + str(second_num)
x = fraction(5,12)
y = fraction(60,123456)

print(x + y)
print(x==y)
'''

'''class DienTich:
    def __init__(self, d, r):
        self.chieudai = d
        self.chieurong = r

    def tinhdientich(self):
        return self.chieudai * self.chieurong

hcn = DienTich(10, 5)
dien_tich = hcn.tinhdientich()
print(dien_tich)'''




nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for m in nums1:
            if m == 0:
                nums1.remove(m)
        nums3 = nums1 + nums2
        nums3.sort()
        return nums1
        return nums3
print(merge())