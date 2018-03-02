# Source code

This is where the source code for all modules resides. The following image demonstrates a pipeline of the code

![alt text](https://github.mit.edu/Reif-Sat/image-processing/blob/master/figures/Image%20processing%20code%20structure.jpg)

## Helper Functions

Every function or method that could be shared between modules (e.g., calculating the MTF of an image, rotating images, ...) should be in here.

## Synthetic Data `syntheticData`

This directory includes all the functions and modules for creating synthetic datasets, et cetera.

## Data Association

Directory that houses the code for aligning (rotation, translation, warping, et cetera) all images of a dataset.

## Merging

Source directory for the distinct merging/stitching methods used to create a final image.

## Performance Analysis

Directory for storing different algorithms for comparing the output image to a ground truth image.

## Back-End

Everything needed for handling the interface with the actual (real) camera, et cetera.




