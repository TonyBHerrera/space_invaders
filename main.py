# This allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

screen_width = constants.SCREEN_WIDTH
screen_height = constants.SCREEN_HEIGHT
running = True

def main():
  
  pygame.init()
  screen = pygame.display.set_mode((screen_width, screen_height))
  
  clock = pygame.time.Clock()
  dt = 0


  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill((0,0,0))
    pygame.display.flip()

  dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()