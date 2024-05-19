# Text-Extraction-from-Images-using-Python-and-OpenCV


## Overview
This Python script utilizes the OpenCV library along with Tesseract OCR to extract text from images. The process involves preprocessing the image, identifying contours, and then extracting text from each contour region.

## How it Works
Importing Libraries: The required libraries cv2 (OpenCV) and pytesseract are imported.

Reading Image: The script reads the image file from which text needs to be extracted.

## Preprocessing:

Grayscale Conversion: The image is converted to grayscale for easier processing.
Thresholding: OTSU thresholding is applied to create a binary image, which helps in separating the text from the background.
Dilation: Morphological dilation is performed to enhance the text regions for better recognition.
Finding Contours: Contours are identified in the processed image using the cv2.findContours function.

Text Extraction Loop:

For each contour identified:
A bounding rectangle is drawn around the contour.
The region within the bounding rectangle is cropped.
Tesseract OCR is applied to extract text from the cropped region.
Extracted text is appended to a string (doc_text).
## Output:

The extracted text (doc_text) is printed to the console.
Parameters and Adjustments
The size of the rectangular kernel (rect_kernel) can be adjusted to detect smaller or larger text regions.
Language for OCR can be modified by changing the lang parameter in the image_to_string function call.
## Usage
Ensure that the required libraries (cv2 and pytesseract) are installed.
Provide the path to the image file (img = cv2.imread("path_to_image.jpg")).
Run the script, and the extracted text will be printed to the console.
Example
An example usage of the script is provided below:

## Read image from which text needs to be extracted
img = cv2.imread("example_image.jpg")

## Dependencies
OpenCV (cv2): Open Source Computer Vision Library
Tesseract OCR (pytesseract): Optical Character Recognition Engine
## Limitations
Performance may vary depending on the quality and complexity of the input image.
Accuracy of text extraction may decrease for images with poor lighting, complex backgrounds, or distorted text.
## Conclusion
This script offers a straightforward method for extracting text from images using Python and OpenCV, making it useful for various applications such as document digitization, text recognition in images, and data extraction from scanned documents. With appropriate adjustments and parameter tuning, it can be adapted to different use cases and scenarios.
