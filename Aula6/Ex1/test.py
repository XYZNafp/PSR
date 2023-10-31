#!/usr/bin/env python3

import cv2
import argparse
from colorama import Fore, Back, Style

def mouseCallback(event, x, y, flags, *userdata):
       print('event='+str(event))

       if event == cv2.EVENT_LBUTTONDOWN:
       print('x='+str(x),' , y='+str(y))


def main():

      # Initialization
      parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
      parser.add_argument('-if', '--image_filename', type=str, help='', required=False, 
                        default='../images/atlascar.png')

      args = vars(parser.parse_args()) # creates a dictionary
      print(args)

      # Execution
      image_filename = args['image_filename']
      image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image


      # Visualization
      cv2.imshow('image_rgb', image_rgb)  # Display the image
      cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == "__main__":
        main()