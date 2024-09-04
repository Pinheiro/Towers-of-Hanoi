import pygame
import const
from tower import Tower

# TO DO
# create counters for the number of successful movements, and the number of failed movements
# detect when all disks have being moved to another tower and announce the end of the game (show counters)

pygame.init()
FONT = pygame.font.SysFont("comicsans", 50)
MSG_FONT = pygame.font.SysFont("comicsans", 20)
WIN = pygame.display.set_mode((const.WIN_WIDTH, const.WIN_HEIGHT))
pygame.display.set_caption("Towers of Hanoi")

def moveDisk(fromTower, toTower):
    movement = f"move disk from tower {fromTower.label} to tower {toTower.label}"
    fail = False
    result = f", successful"
    # movement fails if there are no disks in the tower you are moving the disk from
    if len(fromTower.disks) == 0:
        fail = True
        result = f", failed - tower {fromTower.label} has no disks"
    # get the size of the disk you are trying to move
    sourceDisk = fromTower.disks[-1]
    # movement fails if the top disk in the destination tower is smaller than the disk you are trying to move to that tower
    if len(toTower.disks) != 0:
        destinationDisk = toTower.disks[-1]
        if sourceDisk > destinationDisk:
            fail = True
            result = f", failed - you can't put a disk on top of a smaller disk"
    # transfer disk from one tower to the other
    if not fail:
        fromTower.disks = fromTower.disks[:-1]
        toTower.disks.append(sourceDisk)
    # clear selected towers
    fromTower.isSource = False
    toTower.isDestination = False
    # return a message to the player with the result of this movement
    return f"{movement}{result}"

def main():
    running = True
    clock = pygame.time.Clock()
    tower1 = Tower("1", const.COLOR_WHITE, const.TOWER_X[0], const.TOWER_Y, const.TOWER_WIDTH, const.TOWER_HEIGHT, [8, 7, 6, 5, 4, 3, 2, 1])
    tower2 = Tower("2", const.COLOR_WHITE, const.TOWER_X[1], const.TOWER_Y, const.TOWER_WIDTH, const.TOWER_HEIGHT, [])
    tower3 = Tower("3", const.COLOR_WHITE, const.TOWER_X[2], const.TOWER_Y, const.TOWER_WIDTH, const.TOWER_HEIGHT, [])
    message = "Have a good game!"

    while running:
        clock.tick(const.FPS)

        # draw background
        WIN.fill(const.COLOR_BLACK)
        # draw base
        pygame.draw.rect(WIN, const.COLOR_WHITE, (0, const.WIN_HEIGHT-const.BASE_HEIGHT, const.WIN_WIDTH, const.BASE_HEIGHT))
        # draw each tower, including label and any disks in that tower
        tower1.draw(WIN, FONT)
        tower2.draw(WIN, FONT)
        tower3.draw(WIN, FONT)
        # draw message for the player
        text = MSG_FONT.render(message, 1, const.COLOR_WHITE)
        WIN.blit(text, (const.WIN_WIDTH // 2 - text.get_width() // 2, 100))
        # update surface
        pygame.display.update()

        for event in pygame.event.get():
            # exit the game
            if event.type == pygame.QUIT:
                running = False
                break
            # get key pressed only once per key
            if event.type == pygame.KEYDOWN:
                # select source tower
                if not (tower1.isSource or tower2.isSource or tower3.isSource):
                    if event.key == pygame.K_1:
                        tower1.isSource = True
                    if event.key == pygame.K_2:
                        tower2.isSource = True
                    if event.key == pygame.K_3:
                        tower3.isSource = True
                    break
                # select destination tower
                if (tower1.isSource or tower2.isSource or tower3.isSource):
                    if event.key == pygame.K_1:
                        tower1.isDestination = True
                    if event.key == pygame.K_2:
                        tower2.isDestination = True
                    if event.key == pygame.K_3:
                        tower3.isDestination = True

        # attempt to move a disk
        if tower1.isSource and tower1.isDestination: message = moveDisk(tower1, tower1)
        if tower1.isSource and tower2.isDestination: message = moveDisk(tower1, tower2)
        if tower1.isSource and tower3.isDestination: message = moveDisk(tower1, tower3)
        if tower2.isSource and tower1.isDestination: message = moveDisk(tower2, tower1)
        if tower2.isSource and tower2.isDestination: message = moveDisk(tower2, tower2)
        if tower2.isSource and tower3.isDestination: message = moveDisk(tower2, tower3)
        if tower3.isSource and tower1.isDestination: message = moveDisk(tower3, tower1)
        if tower3.isSource and tower2.isDestination: message = moveDisk(tower3, tower2)
        if tower3.isSource and tower3.isDestination: message = moveDisk(tower3, tower3)

    pygame.quit()

if __name__ == '__main__':
    main()