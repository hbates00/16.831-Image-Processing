#!/usr/bin/python3

'''
Title: 		synthetic-data-demo.py
Author: 	Antonio Teran
Date:  		02/21/2018
Description:    Demo for visualizing the synthetic data creation process.
'''

# Useful includes:
import cv2 				# for image processing functions
import numpy as np			# for general math/matrix magic
from matplotlib import pyplot as plt	# for general plotting tools
import sys, os				# for handling directories and custom imports
import imutils				# for rotating images (masks)

# Locate the repo in system:
REPO_PATH = os.getcwd().split('tests')[0]

# Custom includes:
sys.path.insert(0, REPO_PATH + '/src/helperFunctions/')
from opticsFunctions import calculateMTF

# Include path to images:
MASKS_PATH = REPO_PATH + '/figures/masks/'
TEST_IM_PATH = REPO_PATH + '/figures/test-images/'

''' Global Variables '''
PLOT_ROWS 	= 2
PLOT_COLUMNS 	= 3 

''' -------------
     "Main"
------------- '''

# Read in masks and images:
recMask       = cv2.imread(MASKS_PATH + 'smallRectangularMask.png', 0)
recMaskMTF    = calculateMTF(recMask)
recRotMask    = imutils.rotate(recMask, 90) # rotate rectangular mask by 90 degs
recRotMaskMTF = calculateMTF(recRotMask)
cirMask       = cv2.imread(MASKS_PATH + 'smallCircularMask.jpg', 0)
cirMaskMTF    = calculateMTF(cirMask)
# --
# testImage  = cv2.imread(TEST_IM_PATH + 'small-star-chart-bars-square.png', 0)
testImage  = cv2.imread(TEST_IM_PATH + 'test-lines.png', 0)
testImageF = np.fft.fft2(testImage)

# Create output image:
recOutF    = testImageF * recMaskMTF
recOut     = np.fft.ifft2(recOutF)
recRotOutF = testImageF * recRotMaskMTF
recRotOut  = np.fft.ifft2(recRotOutF)
# -- 
cirOutF    = testImageF * cirMaskMTF
cirOut     = np.fft.ifft2(cirOutF)




# Save & plot everything
plt.figure(figsize=(15,10))
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 1), plt.imshow(abs(testImage), cmap='gray')
plt.title('Original Test Image'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 2), plt.imshow(abs(recMask), cmap='gray')
plt.title('Rectangular Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 3), plt.imshow(abs(recOut), cmap='gray')
plt.title('Output Image (rect)'), plt.xticks([]), plt.yticks([])

plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 4), plt.imshow(abs(testImage), cmap='gray')
plt.title('Original Test Image'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 5), plt.imshow(abs(recRotMask), cmap='gray')
plt.title('Rotated Rectangular Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 6), plt.imshow(abs(recRotOut), cmap='gray')
plt.title('Output Image (rect+rot)'), plt.xticks([]), plt.yticks([])
plt.savefig(TEST_IM_PATH + 'test-lines-rectangular-plots.png', bbox_inches='tight')

plt.figure(figsize=(15,5))
plt.subplot(PLOT_ROWS/2,PLOT_COLUMNS, 1), plt.imshow(abs(testImage), cmap='gray')
plt.title('Fourier Transform of Circular Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS/2,PLOT_COLUMNS, 2), plt.imshow(abs(cirMask), cmap='gray')
plt.title('Circular Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS/2, PLOT_COLUMNS, 3), plt.imshow(abs(cirOut), cmap='gray')
plt.title('Output Image (circular)'), plt.xticks([]), plt.yticks([])
plt.savefig(TEST_IM_PATH + 'test-lines-circular-plots.png', bbox_inches='tight')

plt.show()

# plt.imshow(abs(recOut), cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.savefig(TEST_IM_PATH + 'fuzzy-test-tree.png', bbox_inches='tight')
# plt.imshow(abs(np.fft.fftshift(maskMTF)), cmap='gray'),  plt.xticks([]), plt.yticks([])
# plt.savefig(MASKS_PATH + 'smallRectangularMaskMTF.png', bbox_inches='tight')

# plt.imshow(abs(np.fft.fftshift(circF)), cmap='gray'), plt.xticks([]), plt.yticks([])
# plt.savefig(MASKS_PATH + 'bigCircularMaskFT.png', bbox_inches='tight')
# plt.imshow(abs(np.fft.fftshift(circMTF)), cmap='gray'),  plt.xticks([]), plt.yticks([])
# plt.savefig(MASKS_PATH + 'bigCircularMaskMTF.png', bbox_inches='tight')

