import pygame
import random
import time

def rectangleDraw(color):
	for i in range(len(toSort)):
		pygame.draw.rect(screen,color,((40*i),0,40,(40*toSort[i])))
	pygame.display.flip()

pygame.init()  
pygame.display.set_caption("Bubble Sort")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

toSort = []
for i in range(20):
	number = random.randrange(20)
	while numbers[number] == 0:
		number = random.randrange(20)
	toSort.append(numbers[number])
	numbers[number] = 0

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

for i in range(len(toSort)):
	screen.fill(BLACK)
	rectangleDraw(WHITE)
	for j in range(len(toSort)):
		pygame.draw.rect(screen,RED,((40*j),0,40,(40*toSort[j])))
		pygame.display.flip()
		pygame.draw.rect(screen,BLACK,((40*j),0,40,(40*toSort[j])))
		if toSort[i] <= toSort[j]:
			save = toSort[i]
			toSort[i] = toSort[j]
			toSort[j] = save
		time.sleep(.02)
		pygame.draw.rect(screen,WHITE,((40*j),0,40,(40*toSort[j])))

for i in range(len(toSort)):
	time.sleep(.03)
	pygame.draw.rect(screen,GREEN,((40*i),0,40,(40*toSort[i])))
	pygame.display.flip()

#... - .- -. -.- -.--

rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE) # 
time.sleep(.2)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE) #
time.sleep(.2)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE) 
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE) # 
time.sleep(.2)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE) # 
time.sleep(.2)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE) # 
time.sleep(.2)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #.
time.sleep(.1)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #-
time.sleep(.3)
rectangleDraw(WHITE)
rectangleDraw(GREEN) #-
time.sleep(.3)
