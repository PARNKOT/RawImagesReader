import cv2 as cv
import numpy as np
import os
import argparse


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dir", type=str, default="snapshot", help="Patho to the dir with raw images")
    ap.add_argument("-r", "--rows", type=int, default=1024, help="Высота изображения")
    ap.add_argument("-c", "--columns", type=int, default=1280, help="Ширина изображения")
    ap.add_argument("-f", "--fps", type=int, default=25, help="Скорость воспроизведения кадров")
    ap.add_argument("-s", "--scale", type=float, default=1.0, help="Масштаб")

    args = vars(ap.parse_args())

    rows = args["rows"]
    cols = args["columns"]
    fps = args["fps"]
    dir_ = args["dir"]

    for file in os.listdir(dir_):
        if file.endswith(".raw"):
            with open(f"{dir_}/{file}", "rb") as f:
                img = np.fromfile(f, dtype=np.uint8, count=rows*cols).reshape((rows, cols))

            new_width = int(img.shape[1]*args["scale"])
            new_height = int(img.shape[0]*args["scale"])
            img = cv.resize(img, (new_width, new_height))

            cv.imshow("Frame", img)

            if cv.waitKey(1000//fps) in [ord('q'), ord('Q')]:
                break

    cv.destroyAllWindows()
