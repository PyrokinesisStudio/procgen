#!/usr/bin/env python
from progress.bar import Bar
from map import Color, NormalMap, HeightMap, TopographicMap

def main():
    h = 1024

    heightmap = HeightMap(h, h, 70.0)
    heightmap.to_image('heightmap.png')

    normalmap = NormalMap.from_heightmap(heightmap)
    normalmap.to_image('normalmap.png')

    topography = TopographicMap.from_heightmap(heightmap)
    topography.to_image('topography.png')

if __name__ == '__main__':
    main()
