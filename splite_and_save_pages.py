# import packages
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


# Function with file path
def pdf_splitter(path):
    file_name = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)

    input_paths = []
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(file_name, page + 1)
        input_paths.append(output_filename)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

        # Here we merge every 2 pages!
        # You can change the two if you need every other number of pages!
        if page % 2 == 1:
            pdf_merger = PdfFileMerger()  # create pdfilemerger
            for path in input_paths:
                pdf_merger.append(path)  # read the single pages

            # Here we call it pages_N-1_N, so first would be pages_0_1! What happens here is that we the merged pages
            # to a single file will maintain the file name follow by the page numbers eg; filename_1_2.pdf
            output_path = '{}_pages_{}_{}.pdf'.format(file_name, page - 1, page)
            with open(output_path, 'wb') as file_context:
                pdf_merger.write(file_context)  # write the two pages pdf!

            input_paths = []


if __name__ == '__main__':
    pdf_splitter(path='HWN.pdf')
