import sys
import pygame

class AlienInvasion:
    """класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """инициалирует игру и зоздает игровые ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            #Отслеживание событий кливатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #отображение послежнего прорисованого экрана
            pygame.display.flip()

if __name__ == '__main__':
    #создание экхемпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()    