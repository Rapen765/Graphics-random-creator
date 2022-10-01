from perlin_noise import PerlinNoise
import pygame as pg


class Generator:
    def __init__(self):
        self.noise_h = PerlinNoise()
        self.noise_l = PerlinNoise()
        self.noise_s = PerlinNoise()

    def generate(self, width, height):
        surf = pg.Surface((width, height))
        for x in range(width):
            for y in range(height):
                surf.set_at((x, y), self.generate_color(x, y))
        return surf

    def generate_color(self, x, y):
        actual_noise_h = self.noise_h((x / 100, y / 100))*1000
        actual_noise_l = self.noise_l((x / 100, y / 100))*1000
        actual_noise_s = self.noise_s((x / 100, y / 100))*1000

        color_h = actual_noise_h % 255
        color_l = actual_noise_l % 255
        color_s = actual_noise_s % 255

        return color_h, color_l, color_s


if __name__ == '__main__':
    screen = pg.display.set_mode((300, 300))
    gen = Generator()
    surface = gen.generate(300, 300)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        pg.display.flip()
