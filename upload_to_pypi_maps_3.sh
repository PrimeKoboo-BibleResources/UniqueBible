#!/usr/bin/env bash
# pip install wheel twine
python3 setup_maps_3.py sdist bdist_wheel
twine upload dist/*