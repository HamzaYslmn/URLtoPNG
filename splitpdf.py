import PyPDF2

def split_pdf(pdf_path, pages_per_split):
    # Open the source PDF
    with open(pdf_path, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        number_of_splits = len(reader.pages) // pages_per_split + (1 if len(reader.pages) % pages_per_split else 0)

        for i in range(number_of_splits):
            writer = PyPDF2.PdfWriter()
            # Calculate the range of pages for the current split
            start_page = i * pages_per_split
            end_page = start_page + pages_per_split
            for page_num in range(start_page, min(end_page, len(reader.pages))):
                writer.add_page(reader.pages[page_num])
            
            # Save the current split PDF
            with open(f'C:\\Users\\HamzaY\\Downloads\\split_part_{i + 1}.pdf', 'wb') as outfile:
                writer.write(outfile)

pdf_path = r"C:\Users\HamzaY\Downloads\images.pdf"
split_pdf(pdf_path, 20)
