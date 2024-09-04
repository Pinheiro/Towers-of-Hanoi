import const
import pygame

class Tower:
    COLOR_GREEN = (0, 255, 0)
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, label, color, x, top, width, height, disks):
        self.label = label
        self.color = color
        self.x = x
        self.left = x - const.TOWER_WIDTH // 2
        self.top = top
        self.width = width
        self.height = height
        self.disks = disks
        self.isSource = False
        self.isDestination = False

    def draw(self, win, font):
        # darw label
        if self.isSource:
            text = font.render(self.label, 1, self.COLOR_GREEN)
        else:
            text = font.render(self.label, 1, self.COLOR_WHITE)
        win.blit(text, (self.x - text.get_width() // 2, 20))
        # draw tower
        pygame.draw.rect(win, self.color, (self.left, self.top,self.width, self.height))
        # draw disks
        for i in range(len(self.disks)):
            disk_width = const.DISK_WIDTH_MIN + self.disks[i] * const.DISK_WIDTH_INC
            disk_top = const.WIN_HEIGHT - const.BASE_HEIGHT - (i + 1) * (const.DISK_HEIGHT + 10)
            disk_left = self.x - disk_width // 2
            pygame.draw.rect(win, const.COLOR_WHITE, (disk_left, disk_top, disk_width, const.DISK_HEIGHT))
