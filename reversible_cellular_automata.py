import numpy as np
import random as rdm
import matplotlib.pyplot as plt


def get_neighbours(i, N):

    if i == 0:

        current = i
        left = -1
        right = 1

    elif i == N - 1:

        current = i
        left = N - 2
        right = 0

    else:

        current = i
        left = i - 1
        right = i + 1

    return current, left, right

def next_state(states, t, N):

    previous_previous = states[t-2]
    previous = states[t-1]
    state = []

    for i in range(N):

        current, left, right = get_neighbours(i, N)

        if not previous[left] and not previous[current] and not previous[right] and not previous_previous[current]:

            state.append(1)

        elif not previous[left] and not previous[current] and previous[right] and not previous_previous[current]:

            state.append(1)

        elif not previous[left] and previous[current] and not previous[right] and not previous_previous[current]:

            state.append(0)

        elif not previous[left] and previous[current] and previous[right] and previous_previous[current]:

            state.append(0)

        elif previous[left] and not previous[current] and not previous[right] and previous_previous[current]:

            state.append(1)

        elif previous[left] and not previous[current] and previous[right] and not previous_previous[current]:

            state.append(1)

        elif previous[left] and previous[current] and not previous[right] and previous_previous[current]:

            state.append(0)

        elif previous[left] and previous[current] and previous[right] and not previous_previous[current]:

            state.append(0)

        elif not previous[current]:

            state.append(0)

        else:

            state.append(1)

    return state


T = 60
N = 63
states = np.ones((T, N), dtype = 'int')

states[0] = np.array([1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1])
states[1] = np.array([1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1])

states_pert = np.ones((T, N), dtype = 'int')
states_pert[0] = np.array([1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1])
states_pert[1] = np.array([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1])

for t in range(2, T):

    states[t] = next_state(states, t, N)
    states_pert[t] = next_state(states_pert, t, N)

fig, (ax, ax_pert) = plt.subplots(1, 2)

ax.imshow(states, cmap='Greys',  interpolation='nearest')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Cellular Automata Reversible Rule 214')

ax_pert.imshow(states_pert, cmap='Greys',  interpolation='nearest')
ax_pert.set_xticks([])
ax_pert.set_yticks([])
ax_pert.set_title('Perturbed on a single site at t = 2')

plt.show()

