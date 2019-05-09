SHELL := /bin/bash

default: stitch_wrapper

stitch_wrapper: setup.py stitch_wrapper.pyx
	python3 setup.py build_ext --inplace && rm -f stitch_wrapper.cpp && rm -Rf build

clean:
	rm *.so