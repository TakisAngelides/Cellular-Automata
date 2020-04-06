import random as r
import pyglet

class Board:

    def __init__(self, window_width, window_height, cell_size, num_cells):
        self.window_width = int(window_width / cell_size)
        self.window_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.num_cells = num_cells
        self.cells = self.initialize_cells()
        self.history = [self.cells]

    def initialize_cells(self):
        cells = []
        for i in range(self.num_cells):
            if r.uniform(0, 1) > 0.95:
                cells.append(1)
            else:
                cells.append(0)
        return cells

    # Rule CA - 150
    def evolve(self):
        tmp = [0]*len(self.cells)
        for i in range(len(self.cells)):
            if i == len(self.cells) - 1:
                if self.cells[i-1] == 1 and self.cells[i] == 1 and self.cells[0] == 1:
                    tmp[i] = 1
                if self.cells[i-1] == 1 and self.cells[i] == 0 and self.cells[0] == 0:
                    tmp[i] = 1
                if self.cells[i-1] == 0 and self.cells[i] == 1 and self.cells[0] == 0:
                    tmp[i] = 1
                if self.cells[i-1] == 0 and self.cells[i] == 0 and self.cells[0] == 1:
                    tmp[i] = 1
            elif i == 0:
                if self.cells[len(self.cells) - 1] == 1 and self.cells[i] == 1 and self.cells[i+1] == 1:
                    tmp[i] = 1
                if self.cells[len(self.cells) - 1] == 1 and self.cells[i] == 0 and self.cells[i+1] == 0:
                    tmp[i] = 1
                if self.cells[len(self.cells) - 1] == 0 and self.cells[i] == 1 and self.cells[i+1] == 0:
                    tmp[i] = 1
                if self.cells[len(self.cells) - 1] == 0 and self.cells[i] == 0 and self.cells[i+1] == 1:
                    tmp[i] = 1
            else:
                if self.cells[i - 1] == 1 and self.cells[i] == 1 and self.cells[i+1] == 1:
                    tmp[i] = 1
                if self.cells[i - 1] == 1 and self.cells[i] == 0 and self.cells[i+1] == 0:
                    tmp[i] = 1
                if self.cells[i - 1] == 0 and self.cells[i] == 1 and self.cells[i+1] == 0:
                    tmp[i] = 1
                if self.cells[i - 1] == 0 and self.cells[i] == 0 and self.cells[i+1] == 1:
                    tmp[i] = 1
        self.cells = tmp
        self.history.append(tmp)

    def draw(self):
        col = -1
        for generation in self.history:
            col += 1
            for i in range(len(generation)):
                if generation[i] == 1:
                    row = i
                    col = col % self.window_height
                    square_coords = (row*self.cell_size, col*self.cell_size,
                                     row*self.cell_size, col*self.cell_size + self.cell_size,
                                     row*self.cell_size + self.cell_size, col*self.cell_size,
                                     row*self.cell_size+self.cell_size, col*self.cell_size+self.cell_size)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ('v2i', square_coords))

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(600, 600)
        self.board = Board(self.get_size()[0], self.get_size()[1], int(self.get_size()[0]/50), 50)
        pyglet.clock.schedule_interval(self.update, 1.0/25.0)

    def on_draw(self):
        self.clear()
        self.board.draw()

    def update(self, dt):
        self.board.evolve()

window = Window()
pyglet.app.run()
