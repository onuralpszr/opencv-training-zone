import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


def main():
    """ Open sample image and split color channels  """
    image: np.ndarray = cv.imread(cv.samples.findFile("starry_night.jpg"), cv.IMREAD_UNCHANGED)

    rcParams['figure.figsize'] = (6.0, 6.0)
    rcParams['image.cmap'] = 'gray'

    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    plt.imshow(rgb_image)

    # Split the image into B,G,R components
    b, g, r = cv.split(image)

    plt.figure(figsize=[20, 5])
    plt.subplot(141)
    plt.imshow(b)
    plt.title("Blue Channel")

    plt.subplot(142)
    plt.imshow(g)
    plt.title("Green Channel")

    plt.subplot(143)
    plt.imshow(r)
    plt.title("Blue Channel")

    img_merged = cv.merge((b, g, r))

    plt.subplot(144)
    plt.imshow(img_merged[:, :, ::-1])
    plt.title("Color Channel Merged")

    # Open plots
    plt.show()

if __name__ == '__main__':
    main()
