from pathlib import Path

import rasterio
import rasterio.windows
import shapefile
from rasterio.transform import Affine


def dice(img_path: str, tile_index: str, out_dir: str):
    """
    Crop the image at img_path to multiple small images using bounds defined by the polygon bounding boxes in tile_index
        and writes the resulting images to the out_dir.

    :param img_path:
        The path to the image to crop.
    :param tile_index:
        The path to the tile_index.shp file containing the polygons.
    :param out_dir:
        The path to the directory where output shapes should be written.
    :return:
        None
    """
    # Open the image
    img = rasterio.open(img_path)

    # Open the shapefile
    sf = shapefile.Reader(tile_index)
    if sf.shapeTypeName not in ['POLYGON', 'POLYGONM', 'POLYGONZ']:
        raise RuntimeError("Shapefile must contain polygons")

    # Create the path maker object
    outpath = _OutPath(out_dir, img_path)

    # Create the cropped images
    img_saved = [_crop_img_to_shp(img, shape, outpath) for shape in sf.shapes()]
    print(f"{sum(img_saved)} images created")

    sf.close()
    img.close()


class _OutPath(object):
    def __init__(self, out_dir: str, img_path: str):
        super().__init__()
        self.path = Path(out_dir).joinpath(Path(img_path).name)

    def crop_path(self, left: int, bottom: int) -> str:
        return str(self.path.with_name(f'{self.path.stem}_{left}_{bottom}{self.path.suffix}'))


class _BBox(object):
    def __init__(self, left, bottom, right, top):
        super().__init__()
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    def __repr__(self):
        return f'{self.left=}, {self.bottom=}, {self.right=}, {self.top=}'

    @property
    def is_valid(self):
        return self.right > self.left > 0 and self.top > self.bottom > 0

    def intersect(self, other: '_BBox') -> '_BBox':
        return self.__class__(
            max(self.left, other.left),
            max(self.bottom, other.bottom),
            min(self.right, other.right),
            min(self.top, other.top)
        )

    def img_coords(self, img: rasterio.DatasetReader) -> tuple:
        return img.index(self.left, self.top), img.index(self.right, self.bottom)

    def to_window(self, img: rasterio.DatasetReader):
        lt, rb = self.img_coords(img)
        return rasterio.windows.Window(lt[1], lt[0], rb[1] - lt[1], rb[0] - lt[0])


def _crop_img_to_shp(img: rasterio.DatasetReader, shape: shapefile.Shape, out_path: _OutPath) -> bool:
    # Get the bbox to crop to
    shp_bbox = _BBox(*[round(v) for v in shape.bbox])
    img_bbox = _BBox(*list(img.bounds))
    bbox = shp_bbox.intersect(img_bbox)

    if not bbox.is_valid:
        return False

    # Crop the image
    window = bbox.to_window(img)
    data = img.read(window=window)

    # Write to the output directory
    out = out_path.crop_path(shp_bbox.left, shp_bbox.bottom)
    transform = Affine.translation(bbox.left, bbox.top) * Affine.scale(img.transform.a, img.transform.e)

    with rasterio.open(out, 'w',
                       driver=img.driver,
                       height=window.height,
                       width=window.width,
                       count=img.count,
                       dtype=img.dtypes[0],
                       crs=img.crs,
                       transform=transform,
                       nodata=img.nodata,
                       mask_flag_enums=img.mask_flag_enums,
                       ) as writer:
        writer.write(data)
        writer.colorinterp = img.colorinterp

    print(f'Created: {out}')
    return True
