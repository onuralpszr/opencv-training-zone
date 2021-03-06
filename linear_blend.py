import cv2 as cv
import numpy as np


ALPHA_SLIDER_MAX: int = 100
TITLE_WINDOW: str = "Linear Blend"

# Image sizes has to be same
SRC1: np.ndarray = cv.imread(cv.samples.findFile("LinuxLogo.jpg"))
SRC2: np.ndarray = cv.imread(cv.samples.findFile("WindowsLogo.jpg"))


def on_trackbar(val: int) -> None:
    alpha = val / ALPHA_SLIDER_MAX
    beta = 1.0 - alpha
    dst = cv.addWeighted(SRC1, alpha, SRC2, beta, 0.0)
    cv.imshow(TITLE_WINDOW, dst)


def main() -> None:
    cv.namedWindow(TITLE_WINDOW)
    trackbar_name: str = f"Alpha x {ALPHA_SLIDER_MAX}"
    cv.createTrackbar(trackbar_name, TITLE_WINDOW, 0, ALPHA_SLIDER_MAX, on_trackbar)

    # Set trackbar value to 0 to show the picture
    on_trackbar(0)
    # Wait until user press some key
    cv.waitKey()


if __name__ == "__main__":
    main()