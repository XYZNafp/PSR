#!/usr/bin/env python3

import cv2
import argparse
from colorama import Fore, Back, Style



def main():

      # Initialization
      capture=cv2.VideoCapture(0)
      window_name='Aula5-Ex2'
      cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)



      # Execution
      _, image = capture.read()

      # Visualization
      cv2.imshow(window_name,image)
      cv2.waitKey(0)
  

if __name__ == "__main__":
        main()