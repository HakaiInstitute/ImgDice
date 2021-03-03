# IMG Dice

Dice large GeoTIFFs into smaller images using a shapefile polygon grid. This software assumes that both the the grid
polygons and the image to be sectioned are in a common, UTM coordinate-based, reference system.

## Usage

### GUI

- Go to the Releases page
- Download the appropriate executable for your system starting with `ImgDice-...`
- Run the executable, a Graphical User Interface window should start

### CLI

- Go to the Releases page
- Download the appropriate executable for your system starting with `img-dice-...`
- Run the file using the command line or terminal (eg. `./img-dice-v0.1.0-win64.exe`)
- Use the `-h` flag for help and param types

### Python Package

- Install the package with `pip install git@https://github.com/tayden/img-dice-py`
- Import the dice function into your Python script

e.g.
```
from img_dice import dice

# Get summary of function parameters and options
help(dice)
```
