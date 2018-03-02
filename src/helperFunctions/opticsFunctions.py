#!/usr/bin/python3

'''
Title: 		opticsFunctions.py
Author: 	Antonio Teran
Date:  		02/21/2018
Description: Optics helper functions to be used throughout the repo.
'''

# Useful includes:
import cv2 				# for image processing functions
import numpy as np			# for general math/matrix magic
from matplotlib import pyplot as plt	# for general plotting tools
import sys, os				# for handling directories and custom imports
#import imutils				# for rotating images (masks)

''' -------------
     "Main"
------------- '''

def calculateMTF(image):
	'''
	Calculates an image's Modulation Transfer Function (MTF)
	input:    images - numpy.ndarray
	returns:     MTF - numpy.ndarray
	'''
	imF = np.fft.fft2(image)
	imAuto = abs(imF * np.conjugate(imF))
	return np.fft.ifft2(imAuto)



