import PyPDF2

def merge_pdfs(file_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for path in file_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)

# Provide the file paths of the PDFs you want to merge
file_paths = [r"C:\Users\HamzaY\Desktop\pdf24_images_merged_compressed-1-49.pdf", r"C:\Users\HamzaY\Desktop\pdf24_images_merged_compressed-50-99.pdf", r"C:\Users\HamzaY\Desktop\pdf24_images_merged_compressed-100-149.pdf", r"C:\Users\HamzaY\Desktop\pdf24_images_merged_compressed-150-164.pdf"]

# Specify the output file path
output_path = 'merged_file.pdf'

# Merge the PDFs
merge_pdfs(file_paths, output_path)

print("PDFs merged successfully!")
