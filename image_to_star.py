
#importing the neccesary modules
import PIL.Image as pi
import numpy as np

#path of the image
path = str(input("Enter the path of array :\n\n"))
#opening the image
img = pi.open(path)

#converting the image to black and white
IMG = img.convert("1")

#converting image to array
a = np.asarray(IMG)
b = np.where(a == True, "*", " ")

# Print the resulting array b using rows and columns
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        print(b[i][j], end=" ")
    print()

