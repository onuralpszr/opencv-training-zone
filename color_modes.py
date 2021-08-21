import cv2 as cv
from dataclasses import dataclass
import numpy as np
import sys


@dataclass
class ColorMod:
    def __init__(self) -> None:
        self.starry_img: str = cv.samples.findFile("starry_night.jpg")
        self.img: np.ndarray = cv.imread(self.starry_img, cv.IMREAD_UNCHANGED)

    def colorType(self, _, colorType: int) -> None:
        """ Control Needs to open with  Ctrl+P"""
        self.img = cv.imread(self.starry_img, colorType)
        cv.imshow("Starry Night", self.img)

    def colorMode(self) -> None:
        """ Change color mode of the picture when opened"""

        if self.img is None:
            sys.exit("Could not read the image.")

        cv.namedWindow("Starry Night", cv.WINDOW_NORMAL)
        cv.imshow("Starry Night", self.img)
        cv.createButton("GrayScale", self.colorType, cv.IMREAD_GRAYSCALE, cv.QT_PUSH_BUTTON, 1)
        cv.createButton("RGB Color", self.colorType, cv.IMREAD_COLOR, cv.QT_PUSH_BUTTON, 1)

        key: int = cv.waitKey(0)
        if key == ord("q"):
            cv.destroyAllWindows()


def main() -> None:
    """ Execute main program """
    colormod: ColorMod = ColorMod()
    colormod.colorMode()


if __name__ == "__main__":
    main()
