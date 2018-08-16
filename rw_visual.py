import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making a new walks, as long as the program is active.
while True:

    # Make a randome walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    KEEP_RUNNING = raw_input("Make another walk?(y/n): ")
    if KEEP_RUNNING == 'n':
        break
