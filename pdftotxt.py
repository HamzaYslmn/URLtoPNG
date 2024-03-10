import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os

# Define the path to your PDF and where you want to save the output text
pdf_path = r"C:\Users\HamzaY\Downloads\images.pdf"
txt_output_path = r"C:\Users\HamzaY\Downloads\output.txt"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the PDF file
doc = fitz.open(pdf_path)

# Create or overwrite the output text file
with open(txt_output_path, 'w') as txt_output:

    # Iterate through each page of the PDF
    for page_num in range(len(doc)):
        # Get the page
        page = doc.load_page(page_num)

        # Convert the page to a PIL Image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')

        # Write the text to the output file, add a page break
        txt_output.write(text + '\n\n--- Page Break ---\n\n')

# Close the PDF file
doc.close()
