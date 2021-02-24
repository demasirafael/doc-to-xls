import document_to_text



converted_doc = document_to_text('TRSABESP.docx')

f = open("converted.txt", "w")
f.write(converted_doc)
f.close()

