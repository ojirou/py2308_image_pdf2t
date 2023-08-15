import os
import subprocess
import PyPDF2
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        resource_manager = PDFResourceManager()
        text_stream = io.StringIO()
        laparams = None
        device = TextConverter(resource_manager, text_stream, laparams=laparams)
        interpreter = PDFPageInterpreter(resource_manager, device)
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)
        text = text_stream.getvalue()
    text=text.replace('。', '。 \n')
    text='\n'.join(filter(None, text.split('\n')))
    return text
if __name__=="__main__":
    folder_path = r"C:\Users\user\python\IMAGE\pdf_file"
    output_folder_path = r"C:\Users\user\python\PDF\text_output"
    os.makedirs(output_folder_path, exist_ok=True)
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            all_page_text=extract_text_from_pdf(file_path)
            file_name_without_extension=os.path.splitext(file_name)[0]
            output_file_path = os.path.join(output_folder_path, f"output_{file_name_without_extension}.txt")
            with open(output_file_path, "w", encoding="utf-8") as f:
                 f.write(all_page_text)
            subprocess.Popen(["notepad.exe", output_file_path])