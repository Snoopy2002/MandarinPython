"""
This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
import pygame
import random
import time
import math
 
#Define some colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED  = (205, 0, 0)
BLUE = (0,0,255)
YELLOW = (238, 238, 0)
ORANGE = (255, 128, 0)
VIOLET = (125,38,205)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
MIN = 2
MAX = 10
 
 
class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color=WHITE
        #self.speed=1
        
        
    
        
def ball_collide(ball, ball_list,c): #creates elastic collisions between balls
        t=ball_list.index(ball)
        for i in range(0,len(ball_list)):
           if(i != t):
             d=math.sqrt(pow(ball.x-ball_list[i].x,2)+pow(ball.y-ball_list[i].y,2))
             if  d < max(ball.size, ball_list[i].size)/2: #elastic collision when center distance < ball radius for lg ball
                ball.change_x *=-1
                ball.change_y *=-1
                ball_list[i].change_x *=-1
                ball_list[i].change_y *=-1    
                c = c + 1
        return(c)
 

def make_ball(colors):
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.size=random.randint(MIN,MAX) #make a random ball size
    c=random.randint(0,6) #make a random ball color
    ball.color=colors[c] #assign it to the ball
    ball.x = random.randrange(ball.size, SCREEN_WIDTH - ball.size)
    ball.y = random.randrange(ball.size, SCREEN_HEIGHT - ball.size)
 
    # Speed and direction of ball
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
    #ball.speed=random.randint(1,100)
 
    return ball
 
 
def main():
    """
    This is our main program.
    """
    
    ck=0 #total collisions
    
    pygame.init()
    random.seed(time.clock())
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    
    #array of colors to make them random
    colors=[WHITE, GREEN, RED, BLUE, YELLOW, ORANGE, VIOLET] 
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls: Hit [spacebar] to make new ball.")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    ball_list = [] #create list of balls
 
    ball = make_ball(colors) #make a ball
    ball_list.append(ball) #add it to the list
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball(colors)
                    ball_list.append(ball)
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - ball.size or ball.y < ball.size:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - ball.size or ball.x < ball.size:
                ball.change_x *= -1
                
            ck=ball_collide(ball,ball_list, ck)
                
            
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.size)
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
 
    # Close everything down
    print("Total molecules: ", len(ball_list))
    print("Total collisions: ", ck)
    pygame.quit()

if __name__ == "__main__":
    main()

        