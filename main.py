from datetime import datetime
from math import floor
import pygame
from pygame.locals import *
from sys import exit
now = datetime.now()
month = floor(float(now.month))
m = 0
if now.year % 4 == 0:
    # Predict if it's a leap year
    m = 1
# Add the corresponding days to m depending on the month
if month == 2:
    m += 31
elif month == 3:
    m += 59
elif month == 4:
    m += 9
elif month == 5:
    m += 12
elif month == 6 and now.day < 15:
    m += 151
elif month == 7 or month == 8 or (month == 6 and now.day >= 15) or (month == 9 and now.day < 11):
    # If it's summer, output days till school starts
    if month == 7:
        m += 181
    elif month == 8:
        m += 212
    elif month == 6:
        m += 151
    elif month == 9:
        m += 243
    m += now.day
    m = 254 - m
elif month == 9 and now.day >= 11:
    m += 243
elif month == 10:
    m += 273
elif month == 11:
    m += 304
elif month == 12:
    m += 334
# Add the current day of the month to m, so now we have the place of the current day
# in the year.
# 166 is June 15th.
m += now.day
# If the new year hasn't started, calculate how far it is from December 31th.
if m > 166:
    if now.year % 4 == 0:
        # Don't forget leap years!
        m = 166 + (366 - m)
    else:
        m = 166 + (365 - m)
else:
    m = 166 - m
    # Yay!
windowsize = (360, 360) # The size of the window, um, what didn't you understand?
def center(surface):
    return (windowsize[0] - surface.get_width()) / 2 # Center stuff, I'll need it later.
def getClose():
    for event in pygame.event.get():
        if event.type == QUIT: # Quit if you want to.
            return True
    return False # If the function doesn't return True and end, then return False.
def main():
    # I have no reason to place the code in a func, but why not?
    pygame.init()
    surfacecolor = (0, 80, 250) #Kinda blue
    screen = pygame.display.set_mode(windowsize, DOUBLEBUF)
    pygame.display.set_caption("Days to school")
    font = pygame.font.SysFont("Roboto Slab", 50) # I love Roboto Slab, it's da best for numbers.
    text = font.render(str(m), True, (255,0,0), (255,255,0))
    x = center(text)
    y = 40
    endp = False
    while not endp:
        screen.fill(surfacecolor)
        screen.blit(text, (x, y))
        endp = getClose() # If user clicks on X, endp = True, so program ends. 
                        # Otherwise it's False and we continue.
        pygame.display.update()
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
