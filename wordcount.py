# import sys

# # Get the command line arguments
# args = sys.argv[1:]

# # Join the arguments into a single string
# text = ' '.join(args)

# # Split the text into words
# words = text.split()

# # Print the word count
# print("Word count:", len(words))

# python word_count.py Hello world

# Word count: 2


# def print_hello():
#     print("Hello World")

# # Call the function to print 'Hello World'
# print_hello()


# def verify_data(data):
#     if data.strip():
#         return True
#     else:
#         return False

# user_input = input("Enter some data: ")

# if verify_data(user_input):
#     print("Welcome to the user!")
# else:
#     print("Invalid input. Please enter some data.")




string_list = []

string_list.append("Apple")
string_list.append("Peach")
string_list.append("Strawberry")

for string in string_list:
    print(string)






from collections import Counter
import re

with open('sample.txt', 'r') as file:
    text = file.read()

text = re.sub(r'[^\w\s]', '', text.lower())

words = text.split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(5)  

for word, count in most_common_words:
    print(f"{word}: {count}")



Hello world, hello python. Python is a programming language. World is beautiful.




class MyClass:
    def my_print(self):
        print("Hello from MyClass!")

# Create an object of the class
obj = MyClass()

# Call the print function defined in the class
obj.my_print()






import pygame
import math
# Initialize Pygame
pygame.init()
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elliptical Orbits")
# Clock for controlling the frame rate
clock = pygame.time.Clock()
# Ellipse parameters
ellipse_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
semimajor_axis = 200
semiminor_axis = 100
angle = 0
# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the position of the orbiting object
    x = ellipse_center[0] + semimajor_axis * math.cos(math.radians(angle))
    y = ellipse_center[1] + semiminor_axis * math.sin(math.radians(angle))
        
    # Draw the ellipse    
    pygame.draw.ellipse(screen, WHITE, (ellipse_center[0] - semimajor_axis, ellipse_center[1] - semiminor_axis, semimajor_axis *2, semiminor_axis * 2), 1)

    # Draw the orbiting object    
    pygame.draw.circle(screen, RED, (int(x), int(y)), 5)

    # Update the angle for the next frame    
    angle += 1

    # Update the display    
    pygame.display.flip()

    # Control the frame rate    
    clock.tick(60)
# Quit Pygame

pygame.quit()











import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Ball parameters
ball_radius = 20
ball_color = RED
ball_position = [random.randint(ball_radius, SCREEN_WIDTH -
ball_radius), random.randint(ball_radius, SCREEN_HEIGHT -
ball_radius)]
ball_velocity = [random.randint(-5, 5), random.randint(-5, 5)]

# Main loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the position of the ball
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
      
    # Bounce the ball if it hits the edges of the screen
    if ball_position[0] <= ball_radius or ball_position[0] >= SCREEN_WIDTH - ball_radius:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] <= ball_radius or ball_position[1] >= SCREEN_HEIGHT - ball_radius:
        ball_velocity[1] = -ball_velocity[1]
    
    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]),int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()


def print_string_parameter(string_param):
    print("String parameter:", string_param)

if __name__ == "__main__":
    
    # Call the function and pass a string parameter
    print_string_parameter("Hello, world!")