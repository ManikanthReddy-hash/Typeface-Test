# importing libraries
import cv2
import numpy as np
  
# reading the image data from desired directory
img = cv2.imread("https://cortex6-my.sharepoint.com/:i:/g/personal/kishoreb_typeface_ai/Ed_aqlVwoqpIjELK4L8cAPEB5nJ72tlhTTeXIz1N7IJxgA?e=3hA5lp")
cv2.imshow('Image',img)
img = cv2.imread("https://cortex6-my.sharepoint.com/:i:/g/personal/kishoreb_typeface_ai/EcCu_ueplYVOt5o2wdcSko4BILGU4MHrxZQ7B6wRKwxr9Q?e=T2GAnP")
cv2.imshow('Image',img)
# counting the number of pixels
number_of_white_pix = np.sum(img == 0)
number_of_white_pix = np.sum(img == 1)

print('Number of white patches:', number_of_white_patches)
print('Number of white patches:', number_of_white_patches)
