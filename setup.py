from setuptools import setup

setup(
    name='img-dice',
    version='0.1.0',
    py_modules=['img_dice'],
    install_requires=['rasterio', 'pyshp', 'gdal'],
    url='github.com/tayden/img-dice-py',
    license='MIT',
    author='Taylor Denouden',
    author_email='taylor.denouden@hakai.org',
    description='Dice tif images into smaller sections using a shapefile of polygons'
)
