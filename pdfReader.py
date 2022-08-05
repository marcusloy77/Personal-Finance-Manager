from dataclasses import replace
from PyPDF2 import PdfReader
import re

reader = PdfReader("Banking-5-08-22.pdf")

pages = (reader.pages[1])

text = pages.extract_text()
text = re.split("\d\d\s\w\w\w\s\d\d\d\d", text)
purchase_list = []

for line in text:
    i = line.split('\n')
    i = i[1:]
    if (len(i) > 0):
        i.pop()
    if (len(i) > 2):
        i[1] = i[1].strip()
        i[2] = i[2].replace('$', '')

        purchaseDict = {
            'type': i[0],
            'location': i[1],
            'amount': float(i[2])
        }
    else:
        purchaseDict = -1
    purchase_list.append(purchaseDict)

purchase_list.pop()
purchase_list = purchase_list[1:]

total = 0.0
purchase_list_fixed = []
for purchase in purchase_list:
    if (purchase != -1):
        purchase_list_fixed.append(purchase)

for purchase in purchase_list_fixed:
    total = total + purchase["amount"]


