import PyPDF2


def pdf_read_mode():
    file = open('lorem.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(file)
    # # Get the number of pages in the pdf
    print(f"Number of pages are {reader.numPages}")
    # # Get metadata attached to a pdf file
    print(f"The pdf file has the following metadata: {reader.documentInfo}")

    # Get the page instance (we fetch the first page)
    page = reader.getPage(0)
    # We proceed to fetch the contents of the page by calling the extractText method
    print(page.extractText())


def pdf_write_mode():
    file = open('lorem.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    newpdf = open('new.pdf', 'wb')
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    writer.write(newpdf)
    newpdf.close()


def pdf_merger():
    file = open('lorem.pdf', 'rb')
    file2 = open('mock.pdf', 'rb')
    merger = PyPDF2.PdfFileMerger()
    final_pdf = open('final.pdf', 'wb')
    merger.merge(position=0, fileobj=file2)
    merger.merge(position=2, fileobj=file)
    merger.write(final_pdf)
    final_pdf.close()


if __name__ == '__main__':
    # pdf_read_mode()
    # pdf_write_mode()
    pdf_merger()
