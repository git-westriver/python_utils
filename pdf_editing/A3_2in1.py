# -*- coding: utf-8 -*-

import PyPDF2

def process_pdf(file_path='sample/A4_sample.pdf'):
    a3_width = 1190.5511811024
    a3_height = 841.8897637795

    pdf_file = open(file_path,'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page_obj = pdf_reader.getPage(0)

    # A3の台紙を生成
    base_page = PyPDF2.pdf.PageObject.createBlankPage(width=a3_width, height=a3_height)
    # A3の左にpdfを配置
    base_page.mergePage(page_obj)
    # A3の右にPDFを配置
    base_page.mergeRotatedScaledTranslatedPage(page_obj, 0, 1, a3_width / 2, 0, expand=False)

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(base_page)

    pdf_output_file = open('A3-2in1.pdf','wb')
    pdf_writer.write(pdf_output_file)

    pdf_output_file.close()
    pdf_file.close()

if __name__ == '__main__':
    process_pdf()