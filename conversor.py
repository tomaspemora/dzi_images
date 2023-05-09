#!/usr/bin/env python3

import os

import deepzoom

# Specify your source image
SOURCE = "national-cancer-institute.jpg"

# Create Deep Zoom Image creator with weird parameters
creator = deepzoom.ImageCreator(
    tile_size=128,
    tile_overlap=2,
    tile_format="png",
    image_quality=1.0,
    resize_filter="bicubic",
)

# Create Deep Zoom image pyramid from source
creator.create(SOURCE, "output/nci.dzi")