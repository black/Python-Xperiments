import pygame 
 
pygame.init() 

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((500,300))
pygame.display.set_caption('MY GAME BITCH') 
pygame.display.update()
gameExit = False

xx = 250
yy = 150
moveX = False
moveY = False
movenegX = False
movenegY = False
dx = 1.5
dy = 1.5
clock = pygame.time.Clock()
while not gameExit:
	for event in pygame.event.get(): # event handling loop
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				moveX = True
			if event.key == pygame.K_RIGHT:
				movenegX = True
			if event.key == pygame.K_UP:
				moveY = True
			if event.key == pygame.K_DOWN:
				movenegY = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				moveX = False
			if event.key == pygame.K_RIGHT:
				movenegX = False
			if event.key == pygame.K_UP:
				moveY = False
			if event.key == pygame.K_DOWN:
				movenegY = False
    
	#keyboard incement  method

	if moveX: 
		xx	=	xx	-	dx
	if moveY: 
		yy	=	yy	-	dy 
	if movenegX: 
		xx	=	xx	+	dx
	if movenegY: 
		yy	=	yy	+	dy 

 	mouseX,mouseY = pygame.mouse.get_pos()
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, red, [mouseX,mouseY,10,100]) 
	pygame.draw.rect(gameDisplay, red, [xx,yy,10,100]) 
	gameDisplay.fill(blue,rect=[mouseX,mouseY,100,10])
	pygame.display.update()
	clock.tick(30)
pygame.quit() 
quit()

 