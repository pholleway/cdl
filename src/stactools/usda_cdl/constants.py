from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict

from pystac import Extent, Link, Provider, ProviderRole, SpatialExtent, TemporalExtent


class Frequency(str, Enum):  # update to collection
    base = "base"
    ancillary = "ancillary"


class Variable(str, Enum):
    Cropland = "cropland"
    Confidence = "confidence"
    Cultivated = "cultivated"
    Corn = "corn"
    Cotton = "cotton"
    Soybean = "soybean"
    Wheat = "wheat"


COG_ASSET_TITLES = {
    Variable.Cropland: "Cropland Data Layer (CDL)",
    Variable.Confidence: "Confidence",
    Variable.Cultivated: "Cultivated",
    Variable.Corn: "Corn",
    Variable.Cotton: "Cotton",
    Variable.Soybean: "Soybean",
    Variable.Wheat: "Wheat",
}
COG_ROLES = ["data"]
COG_RASTER_BANDS = {
    Variable.Cropland: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Confidence: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Cultivated: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Corn: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Cotton: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Soybean: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
    Variable.Wheat: [
        {
            "data_type": "uint8",
            "nodata": "nan",
            "spatial_resolution": 30,
        }
    ],
}
RASTER_EXTENSION_V11 = "https://stac-extensions.github.io/raster/v1.1.0/schema.json"

LANDING_PAGE_LINK = Link(
    rel="about",
    target=("https://www.nass.usda.gov/Research_and_Science/Cropland/SARS1a.php"),
    title="Product Landing Page",
)

PROVIDERS = [
    Provider(
        name="United States Department of Agriculture - National Agricultural Statistics Service",
        roles=[ProviderRole.PRODUCER, ProviderRole.LICENSOR],
        url="https://www.nass.usda.gov/",
    )
]

KEYWORDS = [
    "Land Cover",
    "Land Use",
    "USDA",
    "Agriculture",
]

USDA_CDL_COLLECTION: Dict[str, Any] = {
    "id": "usda-cdl",
    "title": "x",
    "description": ("x"),
    "license": "proprietary",
    "keywords": KEYWORDS,
    "extent": Extent(
        SpatialExtent([[-127.887, -74.158, 47.9580, 23.1496]]),
        TemporalExtent([[datetime(2008, 1, 1, tzinfo=timezone.utc), None]]),
    ),
}

USDA_CDL_ANCILLARY_COLLECTION: Dict[str, Any] = {
    "id": "usda-cdl-ancillary",
    "title": "x",
    "description": ("x"),
    "license": "proprietary",
    "keywords": KEYWORDS,
    "extent": Extent(
        SpatialExtent([[-127.887, -74.158, 47.9580, 23.1496]]),
        TemporalExtent([[datetime(2021, 1, 1, tzinfo=timezone.utc), None]]),
    ),
}
