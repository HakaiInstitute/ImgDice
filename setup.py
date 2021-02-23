from setuptools import setup

with open('VERSION', 'r') as file:
    version = file.read().replace('\n', '')

setup(
    name='img-dice',
    version=version,
    py_modules=['img_dice'],
    install_requires=['rasterio', 'pyshp', 'gdal'],
    url='github.com/tayden/img-dice-py',
    license='MIT',
    author='Taylor Denouden',
    author_email='taylor.denouden@hakai.org',
    description='Dice tif images into smaller sections using a shapefile of polygons'
)
