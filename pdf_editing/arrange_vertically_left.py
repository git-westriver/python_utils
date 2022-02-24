# -*- coding: utf-8 -*-
"""
    同ディレクトリ内にあるfilesに編集したいファイルをすべて移す
    その状態でこのファイルを実行すれば所望のファイルが，ファイル名に"_vertical"を付与されて生成される
"""

import PyPDF2

# def process_pdf(size, input_file_path='sample/slide_sample.pdf', output_file_path='arr_left.pdf'):
def process_pdf(input_file_path='sample/slide_sample.pdf', output_file_path='arr_left.pdf'):
    """
    縦540, 横720のスライド用。他のサイズの場合は適宜調整の必要あり。
    その場合はスライドサイズごとのパラメータを記録するか, 別ファイルとして作成すること。
    <改訂> 引数でサイズを指定
    <改訂> 自動化にあたりもとに戻した
    """
    a4_height = 841.8897637795
    a4_width = 1190.5511811024 / 2

    # 出力ファイル
    pdf_writer = PyPDF2.PdfFileWriter()

    with open(input_file_path,'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # size_info = (list(pdf_reader.getPage(0).mediaBox))[2:]
        # print(size_info)
        size = list(map(float,(list(pdf_reader.getPage(0).mediaBox))[2:]))
        print(size)

        if size == [720, 540]:
            # 縦/横 = 4/3
            scale = 0.4
            p1 = 30
            p2 = 600
            p3 = 290
        elif size == [362.83, 272.13]:
            # [720, 540]と比率は同じ
            scale = 0.8
            p1 = 30
            p2 = 600
            p3 = 280
        elif size == [841.89, 595.28]:
            # 縦/横 = 1.4143
            scale = 0.366
            p1 = 30
            p2 = 600
            p3 = 280
        elif size[0]/size[1] < 1.36:
            scale = 0.4 * size[0]/720
            p1 = 30
            p2 = 600
            p3 = 290
        else:
            # 縦/横 = 1.4143
            scale = 0.366*size[0]/841.89
            p1 = 30
            p2 = 600
            p3 = 280

        page_num = pdf_reader.getNumPages()
        

        for i in range((page_num+2)//3):
            # A4の台紙を生成
            base_page = PyPDF2.pdf.PageObject.createBlankPage(width=a4_width, height=a4_height)

            # 3in1
            for j in range(min(3, page_num - 3*i)):
                page_obj = pdf_reader.getPage(3*i+j)
                base_page.mergeRotatedScaledTranslatedPage(page_obj, rotation=0, scale=scale, tx=p1, ty=p2 - p3*j, expand=False)

            pdf_writer.addPage(base_page)
            # print(i,pdf_writer.getNumPages())

        with open(output_file_path,'wb') as pdf_output_file:
            pdf_writer.write(pdf_output_file)


if __name__ == '__main__':

    import glob

    files = glob.glob("files/*.pdf")
    for file in files:
        out_file = "out_" + file[:-4] + "_vertical.pdf"
        process_pdf(file, out_file)
        # print(file)

    
    """
    # 情報理論
    head_file_name = '/Users/nishikawanaoki/Google_westriver/3A/21_情報理論/lecture_'

    base_file_names = [
            '{}{}_handout_rev1'.format(head_file_name,i) for i in (1,2,4,5,6,8,10,11,12)
        ] + [
            '{}{}_handout'.format(head_file_name,i) for i in (3,7,9,13)
        ]

    for base_file_name in base_file_names:
        process_pdf(
            size = [362.83, 272.13],
            input_file_path='{}.pdf'.format(base_file_name),
            output_file_path='{}_edited.pdf'.format(base_file_name)
        )
    """