import fitz  # PyMuPDF library

def trim_pdf_left(filename, left_cut_rate=0.1, out_filename=None):
    if out_filename is None:
        output_pdf_path = filename.replace('.pdf', '_trimmed.pdf')

    # PDF ファイルを開く
    pdf_document = fitz.open(filename)

    # 最初のページのサイズを取得してクロップエリアを設定
    first_page = pdf_document[0]
    page_width, page_height = first_page.rect.width, first_page.rect.height

    # クロップ領域を設定 (ページの幅の left_cut_rate 倍を左側からクロップして行番号を取り除く)
    line_number_crop_margin = page_width * left_cut_rate

    # 各ページの処理
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        # 左側の狭い部分をクロップして行番号を取り除く
        page.set_cropbox(fitz.Rect(line_number_crop_margin, 0, page_width, page_height))

    # クロップ後の PDF を保存
    pdf_document.save(output_pdf_path)
    pdf_document.close()

if __name__ == '__main__':
    trim_pdf_left('files/iclr0001.pdf', left_cut_rate=0.15)