import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class Plot:
    def __init__(self, f, h_position=40) -> None:
        self.f = f
        self.h_position = h_position

    def plot_line(self, output, mode="R") -> None:
        im = Image.open(self.f)
        w, h = im.size
        rgb_data = np.array(im)

        r_data, g_data, b_data = [], [], []

        for i in range(h):
            for j in range(w):
                r_data.append(rgb_data[i][j][0])
                g_data.append(rgb_data[i][j][1])
                b_data.append(rgb_data[i][j][2])

        line_r = [0] * w
        line_g = [0] * w
        line_b = [0] * w

        for j in range(w):
            line_r[j] = rgb_data[self.h_position][j][0]
            line_g[j] = rgb_data[self.h_position][j][1]
            line_b[j] = rgb_data[self.h_position][j][2]

        fig = plt.figure()
        left = list(range(0, w, 1))
        height = line_r

        if mode == "R":
            plt.scatter(left, height, s=1, color="red")
        if mode == "G":
            plt.scatter(left, line_g, s=1, color="green")
        if mode == "B":
            plt.scatter(left, line_b, s=1, color="blue")
        if mode == "RGB":
            plt.scatter(left, line_r, s=1, color="red")
            plt.scatter(left, line_g, s=1, color="green")
            plt.scatter(left, line_b, s=1, color="blue")

        plt.xlabel("position")
        plt.ylabel(f"value of {mode}")
        plt.title(f"{self.f}  h_position={self.h_position}px")

        plt.xticks(np.arange(0, w, 50))
        fig.savefig(output)


if __name__ == "__main__":
    # plot = Plot("img2-1024/1024_1.bmp")
    # plot.plot_line("3/plot_1024_1R.jpg", mode="RGB")
    plot = Plot("3/1000_1.bmp")
    plot.plot_line("3/1001_1plot.jpg", mode="RGB")
