import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
print(getText('c:\\users\\nicho\\Desktop\\PythonPrograms\\TestFiles\\demo.docx'))

#Gets all text from a word file
