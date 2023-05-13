#!/usr/local/bin/python
# 
# Run locally on Mac to filter input files for whisper
#
import json
import os
import shutil
import PyPDF2

PATH_PDF_ARCHIVE = '/Users/Chris/Documents/PDF.ARCHIVE'
PATH_TRANSCRIPTS = './transcripts'
PATH_TRANSCRIPTS = './pdf'

list_pdfs = os.listdir(PATH_PDF_ARCHIVE)
for pdf in list_pdfs:

    if '.pdf' not in pdf:
        print(f'Skipping non-pdf file {pdf}')
        continue
    if '.eml' in pdf:
        print(f'Skipping non-pdf file {pdf}')
        continue


    path_pdf = os.path.join(PATH_PDF_ARCHIVE, pdf)
    transcript = pdf.replace('.pdf', '.mp3.txt')
    path_transcript = os.path.join(PATH_TRANSCRIPTS, transcript)


    # if no txt transcript for this pdf, read the pdf text and create one
    if os.path.exists(path_transcript) == False:
        pdf_file = open(path_pdf, 'rb')
        print(f'reading pdf {path_pdf}')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # Loop through each page and extract the text
        full_text = ''
        for page in pdf_reader.pages:
            # Extract the text from the page
            text = page.extract_text()
            full_text += text
    
        #print(full_text)
        # Close the PDF file
        pdf_file.close()

        print(f'Outputing transcript {path_transcript}')
        with open(path_transcript, 'w') as fd:
            fd.write(full_text)




