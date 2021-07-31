import sys
import os
import comtypes.client

wdFormatPDF = 17
parcours = {"PY":"Model-attestation-fin-stage-python.docx",
            "JS":"Model-attestation-fin-stage-javascript.docx",
            "HTMLCSS":"Model-attestation-fin-stage-HTMLCSS.docx",
            "BLOCK":"Model-attestation-fin-stage-blockchain.docx",
            "PHP":"Model-attestation-fin-stage-phpmysql.docx",
            "SQL":"Model-attestation-fin-stage-sql.docx"
            }
pdf = "alan-delaval-blockchain.pdf"
"""
in_file = os.path.abspath(sys.argv[1])  
out_file = os.path.abspath(sys.argv[2])
"""

in_file = "E:\\OneDrive\\_autoentrepreneur_yvon\\formapedia\log-acces-etudiant\\" + parcours['BLOCK']
out_file = "E:\\OneDrive\\_autoentrepreneur_yvon\\formapedia\log-acces-etudiant\\attestation-fin-formation\\" + pdf

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file,FileFormat=wdFormatPDF)
doc.Close()
word.Quit()


