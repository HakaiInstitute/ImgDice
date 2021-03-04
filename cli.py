import os

import fire

from img_dice import dice

if __name__ == '__main__':
    if os.environ.get('DEBUG', False):
        dice("samples/20-3014-02_OrthoV3_UTM10_sub.tif", "samples/tile_index_sub.shp", "samples/tiled", num_threads=8)
    else:
        fire.Fire(dice)
