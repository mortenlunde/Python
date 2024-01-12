from turtle_race_header import *

# Variabler i spillet lages her globalt
players = []
setup_turtle = turtle.Turtle()
screen = turtle.Screen()


def setup_game(nr_of_players):
    global players
    players = create_turtles(nr_of_players)
    height = (len(players) * 25)
    create_track(setup_turtle, (START_X, MIN_Y), height, DIRECTION_UP, "Start")
    create_track(setup_turtle, (END_X, MIN_Y), height, DIRECTION_UP, "Finish")

    start = -90
    offset = 25
    for p in players:
        p.penup()
        p.goto(START_X - 20, start)
        start += offset

    # Lage spillere
    # Lage spill- brett, startlinje, mållinje og spillere settes på startstreken


def game_loop():
    running = True
    players_finished = [False] * len(players)
    while running:
        for i, p in enumerate(players):
            if not players_finished[i]:  # Check if the player hasn't finished yet
                p.forward(random.randint(1, 4))
                x = p.xcor()
                if x > END_X:
                    players_finished[i] = True

        # Check if all players have finished
        if all(players_finished):
            running = False
    game_end()
    # Løkke som kjører til en spiller kommer i mål
    # Flytte spillere rndom lengde i x- retning mot høyre
    # Sjekke om en spiller har passert mållinje
    #   Hvis ja - avslutt løkken og gå til game_end()


def game_end():
    global setup_turtle
    result_list = sorted(players, key=sort_by_x_pos, reverse=True)
    write_result(setup_turtle, (-30, 50), result_list)


def main():
    global screen
    pla = turtle.numinput(title="Velg antall spillere",
                          prompt="Hvor mange spillere skal være med? (2-6)", default=2, minval=2, maxval=6)
    setup_game(int(pla))
    screen.listen()
    screen.onkeypress(game_loop, "space")
    turtle.exitonclick()


if __name__ == '__main__':
    main()
