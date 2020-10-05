import PyPDF2, os
#Does not extract perfectly, maybe not even open

os.chdir('c:\\users\\nicho\\Desktop\\PythonPrograms\\TestFiles')

pdfFile = open('meetingminutes1.pdf', 'rb')
#read binary mode
#can also write 'c:\\users\\nicho\\Desktop\\meetingminutes1.pdf'

reader = PyPDF2.PdfFileReader(pdfFile)
#Storers a pdf File Reader object in reader
print(reader.numPages)
#Retursn number of pages

page = reader.getPage(0)
#Creating a page object

print(page.extractText())
#Not perfect

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
