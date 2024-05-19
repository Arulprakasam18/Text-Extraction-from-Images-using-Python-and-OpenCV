import cv2
import pytesseract

# Read image from which text needs to be extracted
img = cv2.imread("/path/to/your/image.jpg")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

doc_text = ""  # Initialize empty string to store extracted text

# Looping through the identified contours
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    # Extracting text using Tesseract OCR
    text_eng = pytesseract.image_to_string(cropped, lang='eng')

    # Appending extracted text to doc_text
    doc_text += text_eng.strip() + " "  # Append with a space for separation

# Print the extracted text
print("Extracted Text:", doc_text)
