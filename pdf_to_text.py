import PyPDF2

pdfname = 'xxx' #PDF Name on the Same Directory
pdf_Obj = open(pdfname, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf_Obj)

for page_Num in range(pdfReader.numPages):
    page_Obj = pdfReader.getPage(page_Num)
    convert = page_Obj.extractText()
    print(convert)
    
