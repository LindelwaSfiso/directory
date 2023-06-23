import PyPDF2 as pdf

reader = pdf.PdfReader('directory.pdf')

print('Number of pages in directory:  ', len(reader.pages))


# random page for demostration
page = reader.pages[99]

print(page.extract_text())

text = page.extract_text()


