import pygame, random
from pygame.locals import*

def on_grid_random(): #uma função que vai gerar um número aleatório, mas vai estar sempre no grid
    x = random.randint(0,590)
    y = random.randint(0,590)

    #a ideia aqui é gerar uma posição aleatória, mas sempre um inteiro, o x//10 retorna um inteiro e o *10 faz ser múltiplo de 10
    return (x//10 * 10, y//10 * 10)

#função para detectar colisão
def collision(c1, c2): #duas células onde vai passar a cabeça da cobra e a maça
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

#A maça pode vir em lugares aleatórios como na posição 427 e meus quadrados da cobra são a cada 10
apple_pos = on_grid_random() #gero uma posição aleatória no grid
apple = pygame.Surface((10,10)) #uma maça
apple.fill((255, 0, 0))

my_direction = LEFT
#para limitar a velocidade na tela
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
#para controlar conforme aciono uma tecla
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT
    if collision(snake[0], apple_pos): #colisão entre a cobra e a maça for verdade
        apple_pos = on_grid_random() #gero uma nova posição para a maça
        snake.append((0,0)) #aumento o tamanho da cobra, n importa o valor aqui porque as direções abaixo ja fazem isso, ela vai tomar a posição da cauda anterior
    # cada posição da cobra vai ocupar uma posição que o corpo da frente tava ocupando antes
    # pra fazer isso começo do rabo, e ele vai ocupar a posição -1 a anterior
    for i in range(len(snake) - 1, 0, -1): #comprimento da cobra, 0 n é incluso e decremento pra ir ao contrário
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1]-10) #a minha cabeça é [0] e como sobe y diminui
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])



    screen.fill((0,0,0)) #é necesário atualizar a tela várias vezes
    screen.blit(apple, apple_pos)
    for pos in snake: #pra plotar a cobra
        screen.blit(snake_skin, pos) #passo uma superfície e a posição que quero plotar, passei um quadrinho tam 10x10

    pygame.display.update()
