import setuptools

with open("README.md") as fd:
    long_description = fd.read()

setuptools.setup(
    name='Overlayer',
    version='0.1',
    srcipts=[],
    author='Neo Cortex',
    author_email='sschmelz64@gmail.com',
    description='Creates Images for Stream overlays that look like terminal ui',
    long_description=long_description,
    url='https://github.com/StefanSchmelz/StreamOverlay',
    packages=setuptools.find_packages(),
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: MIT License",
      "Operating System :: OS Independent"
    ]
)
