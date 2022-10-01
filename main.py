from perlin_noise import PerlinNoise
import pygame as pg


class Generator:
    def __init__(self):
        self.noise_r = PerlinNoise()
        self.noise_g = PerlinNoise()
        self.noise_b = PerlinNoise()

    def generate(self, width, height):
        surf = pg.Surface((width, height))
        for x in range(width):
            for y in range(height):
                surf.set_at((x, y), self.generate_color(x, y))
        return surf

    def generate_color(self, x, y):
        actual_noise_r = self.noise_r((x / 100, y / 100))*1000
        actual_noise_g = self.noise_g((x / 100, y / 100))*1000
        actual_noise_b = self.noise_b((x / 100, y / 100))*1000

        color_r = actual_noise_r % 255
        color_g = actual_noise_g % 255
        color_b = actual_noise_b % 255

        return color_r, color_g, color_b


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
