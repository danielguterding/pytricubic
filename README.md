# pytricubic

pytricubic is a simple Python wrapper for the tricubic interpolation algorithm
by Lekien and Marsden based on the implementation by David Kirkby
(https://github.com/deepzot/likely). Performance compared to the reference 
implementation has been improved drastically by doing the matrix multiplication with
the linear algebra template library Eigen.

The tricubic interpolation scheme is described in:

  Lekien, F. and Marsden, J.: Tricubic interpolation in three dimensions.
                              In: International Journal for Numerical Methods
                              in Engineering (2005), No. 63, p. 455-471

## 0. Building

This chapter assumes that you are working in a standard Linux environment with
tools like g++ and cmake already installed. The template libraries Eigen3 for
linear algebra and pybind11 for binding to Python are now included in the thirdparty
subfolder. Threfore, no external requirements exist.

Installing pytricubic is as easy as:  

  git clone git://github.com/danielguterding/pytricubic.git  
  cd pytricubic  
  mkdir build  
  cd build  
  cmake ../  
  cmake --build ../  

## 1. Usage

An example of how to use the interpolator class is given in example.py. Only Python lists are
supported as inputs. Numpy arrays first have to be converted to Python lists.