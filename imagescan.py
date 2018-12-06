# import packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

class Scanner:

    def extract(self, file):

        img = cv2.imread(os.path.join(os.getcwd(), 'files', file))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("image", gray)

        # To apply thresholding to preprocess the image
        # if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


        # elif args["preprocess"] == "blur":
        #     gray = cv2.medianBlur(gray, 3)

        # Write the grayscale image to disk as a temporary file so further we can apply OCR to it
        filename = "{}.png".format(os.getpid())
        print(filename)
        cv2.imwrite(filename, gray)

        # Load the image using PIL (Python Imaging Library), Apply OCR, and then delete the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)

        # Show the output images
        ##cv2.imshow("Image", img)
        # cv2.imshow("Output", gray)
        # cv2.waitKey(0)
        return text


    def extract_old():
        # Construct and Parse The Argument
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--image", required=True, help="Path to the image")
        parser.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")

        args = vars(parser.parse_args())

        img = cv2.imread(args["image"])

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image", gray)

        # To apply thresholding to preprocess the image
        if args["preprocess"] == "thresh":
            gray = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


        elif args["preprocess"] == "blur":
            gray = cv2.medianBlur(gray, 3)

        # Write the grayscale image to disk as a temporary file so further we can apply OCR to it
        filename = "{}.png".format(os.getpid())
        print(filename)
        cv2.imwrite(filename, gray)

        # Load the image using PIL (Python Imaging Library), Apply OCR, and then delete the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        print(text)

        # Show the output images
        ##cv2.imshow("Image", img)
        cv2.imshow("Output", gray)
        cv2.waitKey(0)