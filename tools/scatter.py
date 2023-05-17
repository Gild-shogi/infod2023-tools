import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, DrawingArea, OffsetImage, TextArea
from similar import SimilarOfDegree, SimilarOfDegree64


class Scatter:
    def __init__(
        self,
        f1="img2-1024/1024_1.bmp",
        fl=["img2-1024/1024_2.bmp", "img2-1024/1024_3.bmp"],
    ) -> None:
        data_x = []
        data_y = []
        for f in fl:
            data_x.append(SimilarOfDegree(f1, f))
            data_y.append(SimilarOfDegree64(f1, f))
        self.data_x = data_x
        self.data_y = data_y
        self.f1 = f1
        self.fl = fl

    def get_data(self):
        for f, i, j in zip(self.fl, self.data_x, self.data_y):
            print(f, i, j)

    def plot(self, output="1024_scatter.jpg"):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(self.data_x, self.data_y)
        ax.set_xlim(0, 1.0)
        ax.set_ylim(0, 1.0)

        ax.set_xlabel("RGB", fontsize=14)
        ax.set_ylabel("64 colors", fontsize=14)

        for i in range(len(self.fl)):
            filename = self.fl[i]
            img = plt.imread(filename)
            imagebox = OffsetImage(img, zoom=0.1)
            ab = AnnotationBbox(imagebox, (self.data_x[i], self.data_y[i]))
            ax.add_artist(ab)
            plt.draw()

        img = plt.imread(self.f1)
        imagebox = OffsetImage(img, zoom=0.1)
        ab = AnnotationBbox(imagebox, (1.0, 1.0))
        ax.add_artist(ab)
        plt.draw()

        fig.savefig(output)


if __name__ == "__main__":
    sc = Scatter()
    sc.get_data()
    sc.plot("3/1024_scatter.jpg")
