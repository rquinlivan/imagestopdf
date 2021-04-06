from fpdf import FPDF
from PIL import Image
import os
import time

images = os.listdir('images')
images = sorted(images)
print(f"Processing the following images in the images directory: {images}")
pdf = FPDF()
for image in images:
    pdf.add_page()
    pdf.image(f"images/{image}", 0, 0, 210, 297)
pdf.output("output.pdf", "F")

