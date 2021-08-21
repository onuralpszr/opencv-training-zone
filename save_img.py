import cv2 as cv
from dataclasses import dataclass
import numpy as np
import sys


@dataclass
class ColorMode:
    def __init__(self) -> None:
        self.starry_img: str = cv.samples.findFile("starry_night.jpg")
        self.img: np.ndarray = cv.imread(self.starry_img, cv.IMREAD_UNCHANGED)

    def save_img(self):
        """Save the image in jpg format
        Extra information about: https://docs.opencv.org/4.1.0/d4/da8/group__imgcodecs.html#ga292d81be8d76901bff7988d18d2b42ac
        """

        cv.imwrite("img_name.jpg", self.img, cv.IMWRITE_JPEG_QUALITY)

    def colorMode(self) -> None:
        """ Change color mode of the picture when opened"""

        if self.img is None:
            sys.exit("Could not read the image.")

        cv.namedWindow("Starry Night", cv.WINDOW_NORMAL)
        cv.imshow("Starry Night", self.img)

        key: int = cv.waitKey(0)
        if key == ord("q"):
            cv.destroyAllWindows()

        if key == ord("s"):
            self.save_img()


def main() -> None:
    """ Main program """
    colormode: ColorMode = ColorMode()
    colormode.colorMode()


if __name__ == "__main__":
    main()
    sys.exit("Program Finished")
