WIDTH = 1059
HEIGHT = 504
SIZE = (WIDTH, HEIGHT)

SCROLL_THRESH = 200
screen_scroll = 0
bg_scroll = 0

FPS = 60

GRAVITY = 1

#definerer antall steg i hver animasjon

# Litt usikker på om animation_steps starter på 0 eller 1. Her har jeg tatt utgangspunkt i at det starter på 0
# Dersom den starter på 1 blir lista: [4, 8, 4, 3, 2, 4, 4, 9, 10, 15]. Dette er også antall frames som er oppgitt i nettsiden
SAMURAI_ANIMATION_STEPS = [3, 7, 3, 2, 1, 3, 3, 8, 9, 14]
SAMURAI_SIZE = [23, 25]
SAMURAI_SCALE = 2
SAMURAI_OFFSET = [5, 5]
SAMURAI_DATA = [SAMURAI_SIZE, SAMURAI_SCALE, SAMURAI_OFFSET]