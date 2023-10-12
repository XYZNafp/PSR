#!/usr/bin/env python3

import cv2
import argparse
from colorama import Fore, Back, Style


def main():
      parser = argparse.ArgumentParser(description='Script display images')
      parser.add_argument('-i','--image',action= 'store_true',required=True, help='Input path of the image you want to display')
      args=vars(parser.parse_args())

      image_filename='args["image"]'
      image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

      cv2.imshow('window',image)
      cv2.waitKey(0)

if __name__ == "__main__":
        main()