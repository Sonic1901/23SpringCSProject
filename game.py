# Ethan Nguyen bga6xn

# Concept - World’s Hardest Game.
# Our idea consists of a character moving around trying to get to the end of a level with enemies that inhibit its
# progress. Touching an enemy or when the timer runs out will cause a game over and the player can restart the character
# at the start and so the character must avoid all the enemies and reach the end point in order to “complete” and
# proceed to the next level.
# EDIT1: Added description to include mention of the timer.

# User Input: There will be a main menu and a level select screen that will be interacted with by keyboard using the
# space bar and numbers. During gameplay, the player will be a square that moves in 4 directions, up, down, left, and
# right using arrow keys. If the player dies or does not reach the goal in time, they will fail the level and can either
# return to the main menu or restart by clicking on the screen, or quickly restart by pressing R.
# EDIT1: Change main menu and level select navigation to keyboard and not mouse.

# Game Over: During a level, if the player runs out of time or comes into contact with an enemy, then they will lose and
# must restart from the beginning of the level to try and complete it again.

# Graphics/Images: The main menu and level select screen will be large images that will be displayed during their
# appropriate times.
# EDIT1: Only main menu and level select will be images now.

# Restart from Game Over: Once the player touches an enemy, the game will see this as a level “game over” and ask the
# user to press “R” to start the level again, resetting the player’s position to the initial starting point of the
# level. Bonus: Added that when completing a level, player can press "N" to go to the next level.
# EDIT2: Added bonus

# Enemies: The enemies will be obstacles that upon the player touching them will cause a level “game over.” Simply put,
# the enemies will inhibit the player’s progress by resetting their position to the initial starting point of the level.

# Timer: A timer will be shown in the corner of the screen which will count down starting from a specified amount of
# time after which once the timer reaches 0, it will cause a “game over” and ask the user to restart the level.

# Multiple levels: There will be a level select screen which will ask the user to choose a level to play. Each level
# will have its own layout and play through, likely 3-5 total levels.

import uvage

camera = uvage.Camera(800, 600)
player = uvage.from_color(400, 550, "red", 50, 50)
playfield = [uvage.from_color(400, 0, "white", 800, 1),
             uvage.from_color(400, 600, "white", 800, 1),
             uvage.from_color(0, 0, "white", 1, 1200),
             uvage.from_color(800, 0, "white", 1, 1200)
             ]
fps = 60
level = 0
title_screen = True
level_select = False
game_over = True
move = 0
time = 1
goal = uvage.from_color(0, 0, "green", 0, 0)
enemies = []
levelobjects = []


def levelstart():
    global game_over, level_select, time, enemies, levelobjects, goal
    game_over = False
    level_select = False
    if level == 1:
        time = 20
        enemies = [
            [uvage.from_color(50, 200, "blue", 50, 50), uvage.from_color(50, 350, "blue", 50, 50)],
            uvage.from_color(750, 275, "blue", 50, 50)
        ]
        levelobjects = [
            uvage.from_color(350, 525, "white", 700, 250), uvage.from_color(450, 25, "white", 700, 250)
        ]
        goal = uvage.from_color(700, 550, "green", 200, 200)
    if level == 2:
        time = 20
        enemies = [
            [uvage.from_color(125, 50, "blue", 50, 50), uvage.from_color(275, 50, "blue", 50, 50),
             uvage.from_color(425, 50, "blue", 50, 50), uvage.from_color(575, 50, "blue", 50, 50)],
            [uvage.from_color(200, 550, "blue", 50, 50), uvage.from_color(350, 550, "blue", 50, 50),
             uvage.from_color(500, 550, "blue", 50, 50), uvage.from_color(650, 550, "blue", 50, 50)]
        ]
        levelobjects = [
            uvage.from_color(25, 100, "white", 100, 225), uvage.from_color(25, 500, "white", 100, 225),
            uvage.from_color(750, 100, "white", 100, 225), uvage.from_color(750, 500, "white", 100, 225)
        ]
        goal = uvage.from_color(800, 300, "green", 100, 175)
    if level == 3:
        time = 40
        enemies = [
            [uvage.from_color(275, 50, "blue", 40, 40), uvage.from_color(350, 50, "blue", 40, 40),
             uvage.from_color(425, 50, "blue", 40, 40), uvage.from_color(425, 125, "blue", 40, 40),
             uvage.from_color(425, 200, "blue", 40, 40), uvage.from_color(350, 200, "blue", 40, 40),
             uvage.from_color(275, 200, "blue", 40, 40)], [uvage.from_color(550, 445, "blue", 50, 50),
                                                           uvage.from_color(650, 445, "blue", 50, 50),
                                                           uvage.from_color(550, 545, "blue", 50, 50)],
            [uvage.from_color(290, 445, "blue", 50, 50), uvage.from_color(390, 445, "blue", 50, 50),
             uvage.from_color(390, 545, "blue", 50, 50)]
        ]
        levelobjects = [
            uvage.from_color(75, 295, "white", 325, 410), uvage.from_color(400, 380, "white", 600, 50),
            uvage.from_color(350, 125, "white", 50, 50), uvage.from_color(400, 250, "white", 150, 10),
            uvage.from_color(650, 50, "white", 350, 410), uvage.from_color(695, 450, "white", 10, 150),
            uvage.from_color(475, 550, "white", 75, 150)

        ]
        goal = uvage.from_color(50, 550, "green", 100, 100)


def movement():
    if uvage.is_pressing("left arrow"):
        player.x -= 5
    if uvage.is_pressing("right arrow"):
        player.x += 5
    if uvage.is_pressing("up arrow"):
        player.y -= 5
    if uvage.is_pressing("down arrow"):
        player.y += 5
    if player.touches(playfield[0]):
        player.move_to_stop_overlapping(playfield[0])
    if player.touches(playfield[1]):
        player.move_to_stop_overlapping(playfield[1])
    if player.touches(playfield[2]):
        player.move_to_stop_overlapping(playfield[2])
    if player.touches(playfield[3]):
        player.move_to_stop_overlapping(playfield[3])


def startingposition():
    if level == 1:
        player.x = 50
        player.y = 50
    if level == 2:
        player.x = 50
        player.y = 300
    if level == 3:
        player.x = 150
        player.y = 50


def enemies1():
    global game_over, level, enemies, move
    if level == 1 and not game_over:
        if enemies[0][1].x >= 750:
            move = 1
        if enemies[0][1].x <= 50:
            move = 0
        for enemy in enemies[0]:
            if move == 0:
                enemy.x += 10
            if move == 1:
                enemy.x -= 10
            camera.draw(enemy)
            if player.touches(enemy):
                game_over = True
        if move == 1:
            enemies[1].x += 10
        if move == 0:
            enemies[1].x -= 10
        camera.draw(enemies[1])
        if player.touches(enemies[1]):
            game_over = True
    if level == 2 and not game_over:
        if enemies[0][1].y >= 575:
            move = 1
        if enemies[0][1].y <= 25:
            move = 0
        for enemy in enemies[0]:
            if move == 0:
                enemy.y += 10
            if move == 1:
                enemy.y -= 10
        for enemy in enemies[1]:
            if move == 1:
                enemy.y += 10
            if move == 0:
                enemy.y -= 10
        for i in range(0, 2):
            for enemy in enemies[i]:
                camera.draw(enemy)
                if player.touches(enemy):
                    game_over = True
        # Enemies movement based on list of list/position
    if level == 3 and not game_over:
        for enemy in enemies[0]:
            if enemy.x < 425 and enemy.y == 50:
                enemy.x += 1.25
            if enemy.x == 425 and enemy.y < 200:
                enemy.y += 1.25
            if enemy.x > 275 and enemy.y == 200:
                enemy.x -= 1.25
            if enemy.x == 275 and enemy.y > 50:
                enemy.y -= 1.25
        for enemy in enemies[1]:
            if enemy.x < 650 and enemy.y == 445:
                enemy.x += 2.5
            if enemy.x == 650 and enemy.y < 545:
                enemy.y += 2.5
            if enemy.x > 550 and enemy.y == 545:
                enemy.x -= 2.5
            if enemy.x == 550 and enemy.y > 445:
                enemy.y -= 2.5
        for enemy in enemies[2]:
            if enemy.x > 290 and enemy.y == 445:
                enemy.x -= 2.5
            if enemy.x == 390 and enemy.y > 445:
                enemy.y -= 2.5
            if enemy.x < 390 and enemy.y == 545:
                enemy.x += 2.5
            if enemy.x == 290 and enemy.y < 545:
                enemy.y += 2.5
        for i in range(0, 3):
            for enemy in enemies[i]:
                camera.draw(enemy)
                if player.touches(enemy):
                    game_over = True


def levelobjects1():
    for boundaries in levelobjects:
        if player.touches(boundaries):
            player.move_to_stop_overlapping(boundaries)
    for boundaries in levelobjects:
        camera.draw(boundaries)


def timer():
    global level, game_over, time
    if game_over and fps <= 60:
        time -= 1 / fps
    else:
        time -= 1 / 60
    if time <= 0:
        game_over = True


def gameplay():
    global game_over
    if not game_over:
        movement()
    if game_over:
        lost()
    if player.touches(goal):
        game_over = True
        win()


def lost():
    global game_over, level_select, level, time
    camera.clear("black")
    camera.draw(uvage.from_text(400, 150, "Game Over", 80, "Red", bold=False))
    camera.draw(uvage.from_text(400, 300, "Press R to Restart Level", 60, "Red", bold=False))
    camera.draw(uvage.from_text(400, 450, "Press Space to Go to Level Select", 60, "Red", bold=False))
    if uvage.is_pressing("r"):
        startingposition()
        levelstart()
    if uvage.is_pressing("space"):
        camera.clear("black")
        game_over = False
        level = 0
        level_select = True


def win():
    global game_over, level_select, level, time
    camera.clear("black")
    camera.draw(uvage.from_text(400, 150, "You Beat the Level!", 80, "Red", bold=False))
    camera.draw(uvage.from_text(400, 450, "Press Space to Go to Level Select", 60, "Red", bold=False))
    if level != 3:
        camera.draw(uvage.from_text(400, 300, "Press N to go to the Next Level", 60, "Red", bold=False))
    if uvage.is_pressing("n") and level != 3:
        level += 1
        startingposition()
        levelstart()
    if uvage.is_pressing("space"):
        camera.clear("black")
        game_over = False
        level = 0
        level_select = True


def tick():
    global title_screen, level_select, game_over, level, time, levelobjects, goal
    camera.clear("black")
    if title_screen:
        camera.draw(uvage.from_image(400, 300, "titlescreen.png"))
        if uvage.is_pressing("space"):
            title_screen = False
            level_select = True
    if level_select:
        camera.draw(uvage.from_image(400, 300, "levelselect.png"))
        if uvage.is_pressing("1"):
            level = 1
            startingposition()
            levelstart()
        if uvage.is_pressing("2"):
            level = 2
            startingposition()
            levelstart()
        if uvage.is_pressing("3"):
            level = 3
            startingposition()
            levelstart()
    if level == 1:
        timer()
        enemies1()
        levelobjects1()
        camera.draw(goal)
        camera.draw(player)
        camera.draw(uvage.from_text(450, 125, str("Go to the green square to beat the level!"), 50, "Red", bold=False))
        camera.draw(uvage.from_text(250, 475, str("Use the arrow keys to move!"), 50, "Red", bold=False))
        camera.draw(uvage.from_text(300, 525, str("Finish the level before time runs out!"), 48, "Red", bold=False))
        camera.draw(uvage.from_text(750, 50, str(int(time)), 50, "Red", bold=True))
        gameplay()
    if level == 2:
        timer()
        enemies1()
        levelobjects1()
        camera.draw(goal)
        camera.draw(player)
        camera.draw(uvage.from_text(750, 50, str(int(time)), 50, "Red", bold=True))
        gameplay()
    if level == 3:
        timer()
        enemies1()
        levelobjects1()
        camera.draw(goal)
        camera.draw(player)
        camera.draw(uvage.from_text(750, 50, str(int(time)), 50, "Red", bold=True))
        gameplay()
    camera.display()


uvage.timer_loop(fps, tick)
