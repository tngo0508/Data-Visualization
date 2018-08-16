import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making a new walks, as long as the program is active.
while True:

    # Make a randome walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors=None, s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', cmap=plt.cm.Blues,
                edgecolor='none', s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    KEEP_RUNNING = raw_input("Make another walk?(y/n): ")
    if KEEP_RUNNING == 'n':
        break
