#!/usr/bin/python3

'''
Title: 		mtf-demo.py
Author: 	Antonio Teran
Date:  		02/21/2018
Description:    Demo for visualizing a mask's modulation
		transfer function, and how to calculate it.
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

''' Global Variables '''
PLOT_ROWS 	= 1
PLOT_COLUMNS 	= 3 

''' -------------
     "Main"
------------- '''

# 1. Read in the mask image:
mask = cv2.imread(MASKS_PATH + 'smallRectangularMask.png', 0)

# 2. Take mask into frequency domain:
maskF = np.fft.fft2(mask)		# Take the fast fourier transform in two dimensions

# 3. Compute the autocorrelation in frequency domain
maskFconj = np.conjugate(maskF)		# complex conjugate of the mask's FT
maskFautoCorr = abs(maskF * maskFconj)	# calculate autocorrelation
maskMTF = np.fft.ifft2(maskFautoCorr) 	# obtain modulation transfer function

# ----------------------
# same, but for circular
# ----------------------
circMask = cv2.imread(MASKS_PATH + 'bigCircularMask.jpg', 0)
circF    = np.fft.fft2(circMask)
circMTF  = calculateMTF(circMask)


# 4. Save & plot everything
plt.figure(figsize=(15,5))
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 1), plt.imshow(abs(mask), cmap='gray')
plt.title('Rectangular Aperture Mask, Vertical'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 2), plt.imshow(abs(np.fft.fftshift(maskF)), cmap='gray')
plt.title('Fourier Transform of Vertical Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 3), plt.imshow(abs(np.fft.fftshift(maskMTF)), cmap='gray')
plt.title('Mask Modulation Transfer Function'), plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'smallRectangularMaskPlots.png', bbox_inches='tight')

plt.figure(figsize=(15,5))
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 1), plt.imshow(abs(circMask), cmap='gray')
plt.title('Circular Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS,PLOT_COLUMNS, 2), plt.imshow(abs(np.fft.fftshift(circF)), cmap='gray')
plt.title('Fourier Transform of Circular Aperture Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(PLOT_ROWS, PLOT_COLUMNS, 3), plt.imshow(abs(np.fft.fftshift(circMTF)), cmap='gray')
plt.title('Circular Mask MTF'), plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'bigCircularMaskPlots.png', bbox_inches='tight')

plt.show()

plt.imshow(abs(np.fft.fftshift(maskF)), cmap='gray'), plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'smallRectangularMaskFT.png', bbox_inches='tight')
plt.imshow(abs(np.fft.fftshift(maskMTF)), cmap='gray'),  plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'smallRectangularMaskMTF.png', bbox_inches='tight')

plt.imshow(abs(np.fft.fftshift(circF)), cmap='gray'), plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'bigCircularMaskFT.png', bbox_inches='tight')
plt.imshow(abs(np.fft.fftshift(circMTF)), cmap='gray'),  plt.xticks([]), plt.yticks([])
plt.savefig(MASKS_PATH + 'bigCircularMaskMTF.png', bbox_inches='tight')

