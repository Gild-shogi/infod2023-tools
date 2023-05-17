from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class ColorInfo:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.im = Image.open(filename)
        self.size = self.im.size
        self.width = self.size[0]
        self.height = self.size[1]
        self.rgb_data = np.array(Image.open(filename))
        self.datas = {
            "red": [],
            "green": [],
            "blue": [],
        }
        self.datas = self.get_datas()
        self.rgb = self.get_rgb()
        self.color64 = self.get_color64()

    def get_datas(self) -> Dict:
        for i in range(self.height):
            for j in range(self.width):
                self.datas["red"].append(self.rgb_data[i][j][0])
                self.datas["green"].append(self.rgb_data[i][j][1])
                self.datas["blue"].append(self.rgb_data[i][j][2])
        return self.datas

    def data_parse(self, data: Dict) -> List[dict]:
        red = data["red"]
        green = data["green"]
        blue = data["blue"]
        data_list = []
        for i in range(len(red)):
            data_list.append(
                {
                    "red": red[i],
                    "green": green[i],
                    "blue": blue[i],
                }
            )
        return data_list

    def get_rgb(self, hist_step: int = 20) -> List[int]:
        r_hists = [0] * (255 // hist_step + 1)
        g_hists = [0] * (255 // hist_step + 1)
        b_hists = [0] * (255 // hist_step + 1)
        for data in self.data_parse(self.datas):
            i, j, k = (
                data["red"] // hist_step,
                data["green"] // hist_step,
                data["blue"] // hist_step,
            )
            r_hists[i] = r_hists[i] + 1
            g_hists[j] = g_hists[j] + 1
            b_hists[k] = b_hists[k] + 1
        return r_hists + g_hists + b_hists

    def get_color64(self) -> List[int]:
        sum = 0
        color_data = [0] * 64
        for j in range(self.width):
            for i in range(self.height):
                sum = sum + 1
                r, g, b = 0, 0, 0
                for z in range(3):
                    if self.rgb_data[i][j][z] <= 63:
                        match z:
                            case 0:
                                r = 0
                            case 1:
                                g = 0
                            case 2:
                                b = 0

                    elif self.rgb_data[i][j][z] <= 127:
                        match z:
                            case 0:
                                r = 1
                            case 1:
                                g = 1
                            case 2:
                                b = 1
                    elif self.rgb_data[i][j][z] <= 191:
                        match z:
                            case 0:
                                r = 2
                            case 1:
                                g = 2
                            case 2:
                                b = 2
                    elif self.rgb_data[i][j][z] <= 255:
                        match z:
                            case 0:
                                r = 3
                            case 1:
                                g = 3
                            case 2:
                                b = 3
                color_data[r * 16 + g * 4 + b] += 1
        return color_data


if __name__ == "__main__":
    info = ColorInfo("img2-1024/1024_2.bmp")
    print(info.rgb)
    print(info.color64)
