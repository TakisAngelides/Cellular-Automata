import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 35
T_steps = 1000

def initialize_state():

    return np.random.randint(0, 2, size = (N, N)) # random NxN matrix of 0 and 1

def initialize_Simkin_glider_gun():

    state = np.zeros((N, N))

    state[1][2] = 1
    state[2][1] = 1
    state[1][1] = 1
    state[2][2] = 1

    state[4][5] = 1
    state[4][6] = 1
    state[5][5] = 1
    state[5][6] = 1

    state[1][8] = 1
    state[1][9] = 1
    state[2][8] = 1
    state[2][9] = 1

    state[10][23] = 1
    state[10][24] = 1
    state[11][22] = 1
    state[12][22] = 1
    state[13][22] = 1
    state[13][23] = 1
    state[13][24] = 1

    state[10][26] = 1
    state[10][27] = 1
    state[11][28] = 1
    state[12][29] = 1
    state[13][28] = 1
    state[14][27] = 1

    state[12][32] = 1
    state[12][33] = 1
    state[13][32] = 1
    state[13][33] = 1

    state[18][21] = 1
    state[18][22] = 1
    state[19][21] = 1
    state[20][22] = 1
    state[20][23] = 1
    state[20][24] = 1
    state[21][24] = 1

    return state

def get_neighbours():

    neighbours = {}

    for row in range(N):
        for col in range(N):
            # Using periodic boundary conditions, meaning if N = 3 the left neighbour of cell (0,0) is (0,2) and similar for all other neighbours
            neighbours[(row, col)] = (np.array([(row+1, col), (row, col+1), (row+1, col+1), (row-1, col), (row, col-1), (row-1, col-1), (row+1, col-1), (row-1, col+1)])) % N # modulo N for when we are on the boundary and need the neighbour from periodic boundary conditions

    return neighbours

neighbours = get_neighbours()

def get_alive_neighbours(state, neighbours, row, col):

    alive = 0 # will store number of alive neighbours of cell at (row, col)
    # neighbour_list = list(neighbours[(row, col)])

    for neighbour in neighbours[(row, col)]:
        alive += state[neighbour[0]][neighbour[1]]

    return alive

def update(state, neighbours):

    tmp_state = state.copy() # this copy will not change as we sweep the configuration, the changes will be made to the state variable given as input

    for row in range(N):
        for col in range(N):

            alive = get_alive_neighbours(tmp_state, neighbours, row, col)
            current_cell = tmp_state[row][col]

            if current_cell and alive < 2:
                state[row][col] = 0 # underpopulation
            elif current_cell and alive > 3:
                state[row][col] = 0 # overpopulation
            elif not current_cell and alive == 3:
                state[row][col] = 1 # reproduction

    return state

def evolve():

    # state = initialize_state()
    state = initialize_Simkin_glider_gun()
    neighbours = get_neighbours()
    data = [state] # will hold all the states from t = 0 to t = T_steps-1
    for _ in range(T_steps): # underscore means we don't care about the dummy variable, it will not be used in the for loop
        state = update(state.copy(), neighbours)
        data.append(state)

    return data

data = evolve()

fig, ax = plt.subplots()
animation_plot = plt.imshow(data[0], cmap='Greys',  interpolation='nearest')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Conway\'s Game of Life')

def animate(i):

    animation_plot.set_array(data[i])
    return animation_plot

animation = FuncAnimation(fig, animate, interval = 0.001)
plt.show()