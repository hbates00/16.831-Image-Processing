# Image Processing, REIF-SAT

For detailed information about our approach, please visit our [wiki](https://github.mit.edu/Reif-Sat/image-processing/wiki).

## Main Pipeline

The image processing tasks were broken down into the following categories:

![alt text][OpticsPipeline]

- Stitching/Merging: Tonio + Haley
- Data Handling (Synthetic Data/Camera Back-End): Haley + Marek
- Data Association: Rachel + Tonio
- Performance Analysis: Marek + Rachel


## Important Subsystem Characteristics:


- Frame acquisition time = 0.5 [ms]
- System rotation rate = 30 [deg/s]
- Max rotation per integration time = 0.015 [deg]
- Max pixel smear (0.5 h_px tan(0.015); rotational blur) = 0.32 [px]
- Jitter (linear blur) = ??? [px]
- Total line of sight error budget = 164.8 [milliarcseconds]

## Accumulated Tasks from Last Semester:

- [ ] Formalize run time analysis of image processing algorithm
- [ ] Introduce noise into different stages of the image processing algorithms to demonstrate robustness
    - [ ] Quantify jitter in terms of pixel blur
    - [ ] Quantify radial smear due to rotation during exposure
    - [ ] Quanitfy error created by a rapidly evolving scene
    - [ ] Determine how to georegistrate frames and rerotate frames in the event of a moving camera
- [ ] Compare and contrast image processing algorithms, namely MSE and PMAP
    - [ ] Compare single frame PMAP (SF-PMAP) and multi frame PMAP (MF-PMAP)
    - [ ] Compare different methods of selecting the initial image estimate when using the PMAP algorithm
- [ ] Assess methods used to compare the synthesized image and the circular aperture equivalent image
    - [ ] Histogram method that take advantage of vector math
    - [ ] Pixel-to-pixel direct comparison method
    - [ ] Perceptual hash (pHash) method
    - [ ] Keypoint Matching method, that utilizes image features similar to the SIFT algorithm
- [ ] Develop a plot that shows how accuracy of image processing varies depending on the number of frames used
- [ ] Implement the image processing algorithms on the Raspberry Pi itself 
- [ ] Demonstrate the ability to recover color images using the Wiener Filter approach





[OpticsPipeline]: figures/OpticsPipeline.png?raw=true
