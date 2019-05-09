from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    name="stitch_wrapper",
    sources=["stitch_wrapper.pyx", "stitch_rects.cpp", "hungarian/hungarian.cpp"]
)
setup(
    name="stitch_wrapper",
    ext_modules=cythonize([examples_extension])
)