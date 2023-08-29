import cv2
import matplotlib.pyplot as plt


def scalar_multilpcation(im_path, a):
    im = cv2.imread(im_path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    height, width = im.shape

    scalar_multiples = [0]
    for i in range(1, 256):
        scalar_multiples.append(scalar_multiples[i - 1] + a)
    scalar_multiples = sorted(scalar_multiples)

    plt.subplot(121)
    plt.title("Image")
    plt.imshow(im, cmap="gray")
    plt.axis("off")

    for i in range(height):
        for j in range(width):
            im[i][j] = scalar_multiples[im[i][j]]

    plt.subplot(122)
    plt.title("Scalar Multiplied Image")
    plt.imshow(im, cmap="gray")
    plt.axis("off")  # turn off the axis


im_path = input("Enter a file path: ")
# im_path = '/content/Untitled design (1).png'
a = input("Enter a scalar factor: ")
scalar_multilpcation(im_path,a)