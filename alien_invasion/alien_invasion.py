import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """инициалирует игру и зоздает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            #Отслеживание событий кливатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #при каждом проходе цикла прорисовывать экран в цвете
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #отображение послежнего прорисованого экрана
            pygame.display.flip()

if __name__ == '__main__':
    #создание экхемпляра и запуск игры1
    ai = AlienInvasion()
    ai.run_game()    
<<<<<<< HEAD
=======

    #weqweqwe
>>>>>>> refs/remotes/origin/main
