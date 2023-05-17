import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


class Average:
    def __init__(self, f: str = "img2-1024/1024_1.bmp") -> None:
        self.f = f

    def get_average(self, output) -> None:
        im = Image.open(self.f)
        w, h = im.size
        rgb_data = np.array(im)
        nd = 8

        m, n = nd, nd
        dm, dn = int(h / nd), int(w / nd)

        total_data = [[[0 for rgb in range(3)] for j in range(n)] for i in range(m)]

        for i in range(h):
            for j in range(w):
                ii, jj = i // dm, j // dn
                total_data[ii][jj][0] = total_data[ii][jj][0] + rgb_data[i][j][0]
                total_data[ii][jj][1] = total_data[ii][jj][1] + rgb_data[i][j][1]
                total_data[ii][jj][2] = total_data[ii][jj][2] + rgb_data[i][j][2]

        average_data = [[[0 for rgb in range(3)] for j in range(w)] for i in range(h)]
        for i in range(h):
            for j in range(w):
                ii, jj = i // dm, j // dn
                average_data[i][j][0] = int(total_data[ii][jj][0] / (dm * dn))
                average_data[i][j][1] = int(total_data[ii][jj][1] / (dm * dn))
                average_data[i][j][2] = int(total_data[ii][jj][2] / (dm * dn))

        im2 = Image.new("RGB", (w, h))
        for i in range(h):
            for j in range(w):
                im2.putpixel(
                    (j, i),
                    (
                        average_data[i][j][0],
                        average_data[i][j][1],
                        average_data[i][j][2],
                    ),
                )
        im2.save(output)


if __name__ == "__main__":
    Average().get_average("3/average_1024_1.bmp")
