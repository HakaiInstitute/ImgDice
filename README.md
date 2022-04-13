<div align="center">
    <h1>ImgDice</h1>
    <img src="img_dice/resources/img-dice.png" alt="LAS-TRX">
</div>

___

<div align="center">
   <h4><i>Section large GeoTIFFs into smaller images using a shapefile polygon grid.</i></h4>
</div>

## Usage

### Assumptions

1. The grid polygons and the image to be sectioned are in the same coordinate reference system.
2. That coordinate reference system uses a UTM projection.

## Installation

### GUI

- Go to the [Releases Page](https://github.com/HakaiInstitute/img-dice-py/releases)
- Download the appropriate executable for your system starting with `ImgDice-...`
- Run the executable. A GUI window should start.

### CLI

- Install the package with `pip install img-dice`
- Run `img-dice --help` from the terminal to see the help page for the CLI

### Python Package

- Install the package with `pip install img-dice`
- Import the dice function into your Python script, e.g.

```
from img_dice import dice

# Get summary of function parameters and options
help(dice)
```
