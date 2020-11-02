#!/usr/bin/env python3

import argparse
import cv2
import glob
import numpy as np
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="a opencv test for camera")
    parser.add_argument("camera_id", type=int, metavar="CAMERA_ID")
    parser.add_argument("-H", "--horizontal-flip", action="store_true")
    parser.add_argument("-t", "--title", type=str, default=None)
    args = parser.parse_args()

    print(f"testing /dev/video{args.camera_id}")

    if not glob.glob("/dev/video*"):
        print("no /dev/video* devices found, exit(1)")
        exit(1)

    cap = cv2.VideoCapture(args.camera_id)
    if not args.title:
        args.title = f"/dev/video{args.camera_id}"

    cv2.startWindowThread()
    cv2.namedWindow(args.title)
    while True:
        ret, image = cap.read()
        if not ret:
            break

        if args.horizontal_flip:
            image = cv2.flip(image, 1)

        cv2.imshow(args.title, image)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    print("bye")
