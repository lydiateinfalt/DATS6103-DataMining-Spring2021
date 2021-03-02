# %% 1- Load the image.png into python and convert it to grey scale then print the data type.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q1" + 20* "-")
# Reference: https://www.kite.com/python/answers/how-to-convert-an-image-from-rgb-to-grayscale-in-python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.figure as fig
# Reference: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
# Formula Y' = 0.299 R + 0.587 G + 0.114 B
rgb_weights = [0.2989, 0.5870, 0.1140] #Convert to gray scale
imagex = matplotlib.image.imread("image.png")
print("Data type", type(imagex))
grayscale_image = np.dot(imagex[...,:3], rgb_weights)




# %% 2- Plot the image and explain the features of the figure (color or black and white, size of the image, resolution)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q2" + 20* "-")
plt.imshow(grayscale_image, cmap=plt.get_cmap("gray"))
plt.show()
fig = plt.gcf()
size = fig.get_size_inches()*fig.dpi
print(size)
print(fig.get_size_inches)
print(fig.dpi)
print(grayscale_image.shape)

# %% 3- Flip the image 90, 180, 270 degree by using numpy.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q3" + 20* "-")

grayscale_image_90 = np.rot90(grayscale_image)
plt.imshow(grayscale_image_90, cmap=plt.get_cmap("gray"))
plt.show()
grayscale_image_180 = np.rot90(grayscale_image_90)
plt.imshow(grayscale_image_180, cmap=plt.get_cmap("gray"))
plt.show()
grayscale_image_270 = np.rot90(grayscale_image_180)
plt.imshow(grayscale_image_270, cmap=plt.get_cmap("gray"))
plt.show()

# %% 4- Remove the background and try to find the camera man in the picture (set the background to white or black)
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q4" + 20* "-")
# Reference: https://scikit-image.org/docs/dev/user_guide/numpy_images.html

nrows, ncols = grayscale_image.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 5, ncols / 5
outer_disk_mask = ((row - cnt_row)**2 + (col - cnt_col)**2 >
                  (nrows / 2)**2)
grayscale_image[outer_disk_mask] = 0
plt.imshow(grayscale_image, cmap=plt.get_cmap("gray"))
plt.show()


# %% 5- Keep the background and try color the cameraman by white colors.
# ---------------------------------------------------------------------------------------------------------------------
print(20* "-" + "Q5" + 20* "-")
print(grayscale_image.shape)
dim = np.zeros((512,512))
R = np.stack((grayscale_image,dim, dim), axis=2)
plt.imshow(R)
plt.show()