#!/usr/bin/python3

'''
Title: 		createGroundTruthDataset.py
Author: 	Antonio Teran
Date:  		02/27/2018
Description:    Script that takes in an image and creates an entire
                dataset with a collection of rotated images (noise free).

		Usage: $./createGroundTruthDataset nameOfImage desiredDatasetSize
		Parameters:
			- nameOfImage: string, name of image located in repo/figures/groundTruthImages/
			- desiredDatasetSize: int, number of images that we want in the dataset
'''

# Useful includes:
import cv2 				# for image processing functions
import numpy as np			# for general math/matrix magic
from matplotlib import pyplot as plt	# for general plotting tools
import sys, os				# for handling directories and custom imports
import imutils				# for rotating images (masks)

# Locate the repo in system:
REPO_PATH = os.getcwd().split('image-processing')[0] + 'image-processing'

# Custom includes:
sys.path.insert(0, REPO_PATH + '/src/helperFunctions/')
from opticsFunctions import calculateMTF

# Include path to images:
GT_IM_PATH = REPO_PATH + '/figures/groundTruthImages/'

''' Global Variables '''
PLOT_ROWS 	= 2
PLOT_COLUMNS 	= 3 

''' -------------
     "Main"
------------- '''

if len(sys.argv) != 3:
    print('\n\n**********************')
    print('Stopping! Provided ' + str(len(sys.argv)) + ' arguments, while exactly 3 are needed.')
    print('Usage: $ ' + str(sys.argv[0]) + ' nameOfImage desiredDatasetSize' )
    print('Try again\n\n')

# Load the original image:
im = cv2.imload()


