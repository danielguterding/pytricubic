CMAKE_MINIMUM_REQUIRED(VERSION 3.5)

PROJECT(pytricubic)

SET(EIGEN3_INCLUDE_DIR "thirdparty/eigen3")
SET(PYBIND11_INCLUDE_DIR "thirdparty/pybind11/include")
SET(INCLUDE_DIR "include")
SET(CMAKE_CXX_FLAGS "-O3 -std=c++11 ${CMAKE_CXX_FLAGS}")
INCLUDE_DIRECTORIES(${PYBIND11_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIR} ${INCLUDE_DIR})
LINK_LIBRARIES()

add_subdirectory("thirdparty/pybind11")
pybind11_add_module(tricubic src/tricubic.cpp)
