# -*- coding: utf-8 -*-

import PyPDF2
from tqdm import tqdm

def process_pdf(file_path='sample/A4_sample.pdf', output_file_path = "sample/A4_sample_A4_2in1.pdf"):
    a4_width =  841.99
    a4_height = 594.35

    pdf_file = open(file_path,'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    pdf_writer = PyPDF2.PdfFileWriter()

    page_num = pdf_reader.getNumPages()
    for i in tqdm(range((page_num+1)//2)):
        # A4の台紙を生成
        base_page = PyPDF2.pdf.PageObject.createBlankPage(width=a4_width, height=a4_height)

        # A4の左にpdfを配置
        page_obj = pdf_reader.getPage(2*i)
        size = list(map(float,(list(page_obj.mediaBox))[2:]))
        scale = 594.35 / size[1]
        # base_page.mergePage(page_obj, scale=scale)
        base_page.mergeRotatedScaledTranslatedPage(page_obj, rotation=0, scale=scale, tx=0, ty=0, expand=False)

        # A4の右にPDFを配置
        if 2*i+1 != page_num:
            page_obj = pdf_reader.getPage(2*i+1)
            size = list(map(float,(list(page_obj.mediaBox))[2:]))
            scale = 594.35 / size[1]
            base_page.mergeRotatedScaledTranslatedPage(page_obj, rotation=0, tx= a4_width / 2, ty=0, scale=scale, expand=False)

        pdf_writer.addPage(base_page)

    pdf_output_file = open(output_file_path,'wb')
    pdf_writer.write(pdf_output_file)

    pdf_output_file.close()
    pdf_file.close()

if __name__ == '__main__':
    import glob

    files = glob.glob("files/*.pdf")
    for file in files:
        out_file = "out_" + file[:-4] + "_a4_2in1.pdf"
        process_pdf(file, out_file)