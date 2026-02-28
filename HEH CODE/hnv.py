'''import pygame
from pygame.locals import *

pygame.init()

HEIGHT = 600
WIDTH = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('hello')

clock = pygame.time.Clock()

BLACK = (0,0,0)
SKY_BLUE = (66, 135, 245)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
    window.fill(SKY_BLUE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit'''


'''n = str(input(""))
ds = n.split()
ds_1 = []
for i in ds:
    if int(i) % 5 == 0:
        ds_1.append(i)
print(ds_1)'''

'''n = str(input(""))
ds = n.split()
for i in range(1, len(ds)-1):
    for j in range(1, len(ds)-1-i):
        if int(ds[j]) > int(ds[i]):
            ds[j], ds[i] = ds[i], ds[j]
print(ds)'''

# bai 1

'''with open("TANGQUA.INP", "r") as f1:
    a = int(f1.readlines([0]))
    b = int(f1.readlines([1]))
    c = int(f1.readlines([2]))
with open("TANGQUA.OUT", "W") as f2:
    A = a+b
    B = a+c
    C = b+c
    if A > B and A > C:
        f2.write(A)
    if B > A and B > C:
        f2.write(B)
    if C > A and C > B:
        f2.write(C)
    f2.write(" ")
    if A < B and A < C:
        f2.write(A)
    if B < A and B < C:
        f2.write(B)
    if C < A and C < B:
        f2.write(C)
'''

'''lis = [1,4,3,2,5]
lis.sort()
print(lis)'''

'''def haichuso(a, b):
    print(a)
    print(b)
a = int(input(""))
b = int(input(""))
haichuso(a,b)'''

'''def st(n):
    if n < 10:
        return " " + str(n)
    else:
        return str(n)
def sp(k):
    return " "*k
def bc():
    for i in range(1, 11):
        for j in range(1, 6):
            print(st(j) + "x" + st(i) + "=" + st(i*j) + sp(2), end=" ")
        print()
    print(" ")
    for i in range(1, 11):
        for j in range(6, 11):
            print(st(j) + "x" + st(i) + "=" + st(i*j) + sp(2), end=" ")
        print()
    print()
bc()'''

'''def giaithua(a):
    ga = 1
    for i in range(1, a+1):
        ga *= i
    print(ga)
giaithua(3)'''

'''xau = str(input(""))
if len(xau) %2 == 0:
    xaucon = ""
    for i in range(len(xau)//2):
        xaucon += xau[i]
    if xaucon.reverse() == xau.delete(xaucon):
        print(1)
    else:
        print(xaucon)
else:
    print(0)'''
'''
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for x in range(20):
    for y in range(20):
        box = Button(color=color.white, model='cube', position=(x,0,y),
            texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                texture=load_texture('assets/grass_block.png'), parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)
app.run()'''

'''
a = [0, 1, 5, 2, 7, 9]
a.insert(4, 6)
a.remove(2)
a.append(3)
print(a)'''

'''
a = [1, 2, 5, 7, 32, 54, 69, 4, 53]
def find(lst):
    if len(lst) == 0:
        return none
    so = lst[0]
    for s in lst:
        if s > so:
            so = s
        return so
print(find(a))'''

'''xau = input("")
for i in range(len(xau)-1):
    j = xau[i]+1
    if 48 <= ord(i) <= 57 and 48 <= ord(j) <= 57:
        so_xet = int(str(i)+str(j))'''

'''print(int(eval(input("enter"))))'''

'''rows = 5
for i in range(1, rows+1):
    print(' ' * (rows - i) + '*' * (2*i-1))'''