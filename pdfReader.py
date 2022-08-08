from dataclasses import replace
from PyPDF2 import PdfReader
import re

reader = PdfReader("Banking-5-08-22.pdf")
purchase_list_long = []
running_total = 0

for i in range(7):
    page = (reader.pages[i])
    text = page.extract_text()
    text = re.split("\d\d\s\w\w\w\s\d\d\d\d", text)
    purchase_list = []

    for line in text:
        i = line.split('\n')
        i = i[1:]
        if (len(i) > 0):
            i.pop()
        if (len(i) == 3):
            i[0] = i[0].strip()
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
    purchase_list_long = purchase_list_long + purchase_list_fixed
    running_total = running_total + total


not_taken = []
uber_eats = []
deliveroo = []
menulog = []
uber = []
eating_out = []
alcohol = []
subscriptions = []
pubs = []
gaming = []
groceries = []
transport = []
petrol = []
online_orders = []
other = []

for purchase in purchase_list_long:

    if '*EATS' in purchase['type']:
        uber_eats.append(purchase)

    elif 'STEAM' in purchase['type']:
        gaming.append(purchase)
    
    elif 'MCDONALDS' in purchase['type']:
        eating_out.append(purchase)

    elif 'Subway' in purchase['type']:
        eating_out.append(purchase)

    elif 'ZAM' in purchase['type']:
        eating_out.append(purchase)

    elif 'UBER' in purchase['type']:
        uber.append(purchase)
    elif 'MICROSOFT*' in purchase['type']:
        subscriptions.append(purchase)
    elif 'CHEGG' in purchase['type']:
        subscriptions.append(purchase)
    elif 'Spotify' in purchase['type']:
        subscriptions.append(purchase)
    elif 'Netflix' in purchase['type']:
        subscriptions.append(purchase)
    elif 'NETFLIX' in purchase['type']:
        subscriptions.append(purchase)
    elif 'STAN' in purchase['type']:
        subscriptions.append(purchase)
    elif 'Stan' in purchase['type']:
        subscriptions.append(purchase)
    elif 'Disney' in purchase['type']:
        subscriptions.append(purchase)
    elif 'DISNEY' in purchase['type']:
        subscriptions.append(purchase)

print(subscriptions)


