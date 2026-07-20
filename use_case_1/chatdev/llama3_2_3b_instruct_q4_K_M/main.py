class Main:
    def __init__(self):
        # Initialize main application state
        self.root = tk.Tk()
        self.game = Game()
    def run(self):
        # Run main application loop
        while True:
            if not self.game.update():
                break
            self.game.draw()
            self.root.after(100, lambda: self.game.draw())