from setuptools import setup, Extension

setup(
    # Information
    name = "tricubic",
    version = "1.0.0",
    url = "https://github.com/danielguterding/pytricubic",
    author = "Daniel Guterding",
    license = "MIT",
    keywords = "tricubic cubic interpolation",
    # Build instructions
    ext_modules = [Extension("tricubic",
                             ["src/tricubic.cpp"],
                             include_dirs=["include/", "thirdparty/eigen3", "thirdparty/pybind11"])]
)