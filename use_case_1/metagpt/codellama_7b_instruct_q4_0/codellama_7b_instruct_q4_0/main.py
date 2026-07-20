from game import Game

def main():
    game = Game()
    game.start()
    while True:
        events = get_events()
        game.handle_events(events)
        game.update()
        game.render()

if __name__ == "__main__":
    main()
