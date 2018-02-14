import pygame,sys
from pygame.locals import*

#number of frames per second
# Change this value to speed up or slow down your game
FPS=300

display_width=800
display_hight=600
lineThickness = 10
paddleSize = 80
paddleOffest= 30
increaseSpeed=1
paddle_change=0
# Set up the colours
black     = (0  ,0  ,0  )
white     = (255,255,255)

#Draws the arena the game will be played in. 
def drawArena():
    display.fill((0,0,0))
    #Draw outline of arena
    #((0,0),(WINDOWWIDTH,WINDOWHEIGHT)) defines a rectangle. (0,0) are the (left, top) co-ordinates, and (WINDOWWIDTH,WINDOWHEIGHT) are the width and height of the rectangle
    pygame.draw.rect(display, white, ((0,0),(display_width,display_hight)), lineThickness*2)
    #Draw centre line
    # ((WINDOWWIDTH/2),0) are the starting (x,y) co-ordinates of the line and ((WINDOWWIDTH/2),WINDOWHEIGHT) are the end co-ordinates
    pygame.draw.line(display, white, ((display_width/2),0),((display_width/2),display_hight), (lineThickness//4))
    

    

#Draws the paddle
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > display_hight - lineThickness:
        paddle.bottom = display_hight - lineThickness
    #Stops paddle moving too high
    elif paddle.top < lineThickness:
        paddle.top = lineThickness
    #Draws paddle
    pygame.draw.rect(display, white, paddle)
  
#draws the ball
def drawBall(ball):
    pygame.draw.rect(display, white, ball)
    
#move the ball return new position
def moveBall(ball,ballDirX,ballDirY):
    ball.x+=(ballDirX *increaseSpeed)
    ball.y+=(ballDirY*increaseSpeed)
    return ball



def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (lineThickness) or ball.bottom == (display_hight - lineThickness):
        ballDirY = ballDirY * -1
    if ball.left == (lineThickness) or ball.right == (display_width - lineThickness):
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY


#Checks is the ball has hit a paddle
def checkHitBall(ball,paddle1,paddle2, ballDirX):
    if ballDirX==-1 and paddle1.right==ball.left and paddle1.top<ball.top and paddle1.bottom>ball.bottom:
        return -1
    elif ballDirX==1 and paddle2.left==ball.right and paddle2.top<ball.top and paddle2.bottom > ball.bottom:
        return -1
    else:
        return 1
    

def checkPointScore(paddle1, ball,score,ballDirX):
    if ball.left == lineThickness:
        score+=1
        return score
    

        
    #if no points scored, return score unchanged
    else:
        return score
        
    

def checkPointScore2(paddle2, ball,score2,ballDirX):
    if ball.right == 790  :
        
        score2+=1
        return score2
    else:
        return score2





#def artificialIntelligence(ball,ballX,paddle1):
    #if ballX==1:
        #if paddle1.centery<display_width/2:
            #paddle1.y+=1
        #elif paddle1.centery>display_width/2:            
            #paddle1.y-=1
    #elif ballX==-1:
        #if paddle1.centery<ball.centery:
            #paddle1.y+=1
        #else:
            #paddle1.y-=1
    #return paddle1        


#Displays the current score on the screen
def displayScore(score):
    resultSurf = basicFont.render('Score  = %s' %(score), True, white)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (display_width - 150, 25)
    display.blit(resultSurf, resultRect)
            

def displayScore2(score2):
    resultSurf2 = basicFont.render('Score  = %s' %(score2), True, white)
    resultRect2 = resultSurf2.get_rect()
    resultRect2.topright = (display_width-600, 25)
    display.blit(resultSurf2, resultRect2)

            



        



#main functon
def main():
    pygame.init()
    global display #adding global allows us to modify the value later on
    global basicFont,basicFontsize
    
    basicFontsize=20
    paddle_change=0
    paddle2_change=0
    


    basicFont = pygame.font.Font('freesansbold.ttf', basicFontsize)


    FPSCLOCK=pygame.time.Clock() 
    display=pygame.display.set_mode((display_width,display_hight))
    pygame.display.set_caption('Pong')
    
    #initiate variable and set staring position
    ballX=display_width/2-lineThickness/2
    ballY=display_hight/2-lineThickness/2
    playerOnePosition=(display_hight-paddleSize)/2
    playerTwoPosition=(display_hight-paddleSize)/2
    score=0
    score2=0

    
    #move the ball
    ballDirX=-1 #left=right
    ballDirY=-1 #up=down
    



    


    #Creates Rectangles for ball and paddles
    paddle1=pygame.Rect(paddleOffest,playerOnePosition,lineThickness,paddleSize)
    paddle2=pygame.Rect(display_width-paddleOffest-lineThickness,playerTwoPosition,lineThickness,paddleSize)
    ball=pygame.Rect(ballX,ballY,lineThickness,lineThickness)



    #draws the starting position of the arena
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    
    pygame.mouse.set_visible(0)



    
    

    
    



    
    while True: #main game loop
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit
            #if event.type == MOUSEMOTION:
                #mousex, mousey = event.pos
                #paddle2.y = mousey



                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    paddle_change-=2
                if event.key==pygame.K_DOWN:
                    paddle_change+=2
                    
            if event.type==pygame.KEYUP:
                if event.key ==pygame.K_UP or event.key == pygame.K_DOWN  :
                    paddle_change=0





            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    paddle2_change-=2
                if event.key==pygame.K_s:
                    paddle2_change+=2


            if event.type==pygame.KEYUP:
                if event.key ==pygame.K_w or event.key == pygame.K_s  :
                    
                    paddle2_change=0
        
        

                    
                    
                    


                
        








                    
        paddle2.top+=paddle_change
        paddle1.top+=paddle2_change
                    




                
        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX,ballDirY = checkEdgeCollision(ball,ballDirX,ballDirY)
        score= checkPointScore(paddle1, ball, score, ballDirX)
        score2= checkPointScore2(paddle2, ball, score2, ballDirX)


        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        #paddle1 = artificialIntelligence (ball, ballDirX, paddle1)


        displayScore2(score2)

        displayScore(score)





        
        pygame.display.update()
        FPSCLOCK.tick(FPS) # tell our program to set the Frames Per Second
        
if __name__=='__main__':
    main()

                
                
    

    






            
    
