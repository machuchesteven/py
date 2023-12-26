import PyPDF2
import os

# Open the PDF file
def extract_data(filename:str):
    complete_file_path = os.path.join(os.getcwd(), 'invoices', filename)
    with open(complete_file_path, 'rb') as pdfFileObj:
        print(pdfFileObj)
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[0]
        for page in pdfReader.pages:
            print(page.extract_text())
            print('\n\n\n\nPage completed \n\n\n')
        data = pageObj.extract_text()
        return data



def main():
    data = extract_data(filename='invoice.pdf')
    print(data)



if __name__ == '__main__':
    main()
