'''
Title: Jitter_Blur
Author: Hamilton Eng
Date: 11/16/2017
Description: Jitter_Blur takes images and applies linear and rotational blur.
			 The user has the option to apply only linear blur, only rotational
			 blur, or a combination of both. These will be used to assess the
             image processing algorithm to be used on the Optics Testbed.

             This current implementation runs on MacOS High Sierra 10.13.1
'''

### Setup
# Setting up subprocess routine
import sys, os, subprocess, string

# Import the image to be used. Make sure it is in current folder
img = 'boston'

# Determine type of blur to be induced
#	1 = Linear Motion
#	2 = Rotational Motion
#	3 = Both Linear and Rotational Motion
motion_type = 1

# Blur Parameters
rot = '20' # Degrees of Rotational Blur
lin = '0' # Angle of induced Linear Blur (relative to )
rad = '0' # Radius of Linear Blur
sig = '400' # Standard Deviation (sigma) of Linear Motion in # of pixels of blur desired

# Induce Blur
if motion_type == 1:

	# Linear Motion using ImageMagick
	subprocess.call('convert -channel RGBA -motion-blur '+rad+'x'+sig+'+'+lin+' '+img+'.jpg '+img+'_blur_4.jpg', shell=True)

elif motion_type == 2:
	
	# Rotational Motion
	subprocess.call('convert -rotational-blur '+rot+' '+img+'.jpg '+img+'_blur_2.jpg', shell=True)

elif motion_type == 3:

	# Rotational Motion
	subprocess.call('convert -rotational-blur '+rot+' '+img+'.jpg '+img+'_blur_3.jpg', shell=True)
	
	# Linear Motion
	subprocess.call('convert -channel RGBA -motion-blur '+rad+'x'+sig+'+'+lin+' '+img+'_blur_3.jpg '+img+'_blur_3.jpg', shell=True)

# Other Method for Linear Motion

# # Setup
# import sys
# sys.path.append('/usr/local/lib/python2.7/site-packages')

# # Importing Numpy, OpenCV and setting up the subprocess routine
# import numpy as np
# import cv2
# import sys, os, subprocess, string

# # Import the image to be used. Make sure it is in current folder
# img = cv.imread('stata.jpg')

# # Determine type of blur to be induced
# #	1 = Linear Motion
# #	2 = Rotational Motion
# #	3 = Both Linear and Rotational Motion
# motion_type = 2

# # Induce Blur
# if motion_type == 1:
# 	Linear Motion using OpenCV
# 		cv.imshow('Original', img)

# 		# Set the size of the kernel
# 		size = 15

# 		# Generating the kernel
# 		kernel_motion_blur = np.zeros((size, size))
# 		kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
# 		kernel_motion_blur = kernel_motion_blur / size

# 		# Applying the kernel to the input image
# 		output = cv.filter2D(img, -1, kernel_motion_blur)

# 		cv.imshow('Motion Blur', output)
# 		cv.waitKey(0)

# # Other routine that does a more fluid rotational blur but cannot control the angle 
# subprocess.call('convert MIT_Crew_Logo.jpg -virtual-pixel Edge \
#             -set option:distort:scale 4   -distort DePolar -1 \
#             -scale 10%x100%\! -filter Gaussian -resize 1000%x100%\! +filter \
#             -virtual-pixel HorizontalTileEdge -background Black \
#             -set option:distort:scale 0.5 -distort Polar -1\
#             MITCL_rotation_2.jpg', shell=True)
