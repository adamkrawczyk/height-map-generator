# Diamond-Square Algorithm

import numpy as np


def diamond_square(size_x, size_y, roughness):
    data = np.zeros((size_x, size_y))

    # Initial random corners
    data[0, 0] = np.random.rand() * roughness
    data[0, size_y-1] = np.random.rand() * roughness
    data[size_x-1, 0] = np.random.rand() * roughness
    data[size_x-1, size_y-1] = np.random.rand() * roughness

    step_x = size_x - 1
    step_y = size_y - 1
    while step_x > 1 or step_y > 1:
        # Diamond step
        for x in range(0, size_x-1, step_x):
            for y in range(0, size_y-1, step_y):
                if x + step_x < size_x and y + step_y < size_y:
                    midpoint = ((data[x, y] + data[x + step_x, y] +
                                data[x, y + step_y] + data[x + step_x, y + step_y]) / 4)
                    data[x + step_x // 2, y + step_y // 2] = midpoint + \
                        (np.random.rand() - 0.5) * \
                        max(step_x, step_y) * roughness

        # Square step
        for x in range(0, size_x, step_x if step_x > 1 else 1):
            for y in range((x + step_x // 2) % step_x, size_y, step_y if step_y > 1 else 1):
                s_x = step_x // 2
                s_y = step_y // 2
                surrounding = []
                if x - s_x >= 0:
                    surrounding.append(data[(x - s_x), y])
                if x + s_x < size_x:
                    surrounding.append(data[(x + s_x), y])
                if y + s_y < size_y:
                    surrounding.append(data[x, (y + s_y)])
                if y - s_y >= 0:
                    surrounding.append(data[x, (y - s_y)])

                avg = sum(surrounding) / len(surrounding)
                avg += (np.random.rand() - 0.5) * \
                    max(step_x, step_y) * roughness
                data[x, y] = avg

        step_x = step_x // 2 if step_x > 1 else 1
        step_y = step_y // 2 if step_y > 1 else 1

    return data

# Example terrain_data = diamond_square(513, 100, 0.6)  # 513 is 2^9 + 1, and 0.6 is a roughness value
