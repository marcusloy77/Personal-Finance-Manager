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
            i[0] = i[0].strip().upper()
            i[1] = i[1].strip().upper()
            i[2] = i[2].replace('$', '').upper()

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

food_delivery_list = ['*EATS', 'MENULOG', 'DELIVERO', 'EASI', 'ONLINE ORDERING']
eating_out_list = ['THE HORDEN', 'KEBAB', 'OXFORD UNDERGROUND', 'BERESFORD', 'BEANS', 'PIZZERIA', 'MCDONALDS', 'SUBWAY', 'ZAM', 'RESTURANT', 'PIZZA', 'PASTA', 'THAI', 'ITALIAN', 'RESTURANT', 'PAVILION', 'CAFE', 'PUB', 'BAR', 'CLUB', 'COFFEE', 'HOTEL', 'FOOD', 'BEER', 'SOUL ORIGIN', 'MUMBAI EXPRESS', 'SOUL ORIGIN', 'GUZMAN', 'HABERFIELD HOT BR', 'SANDWICHES', 'TACO', 'SPANISH', 'BURRITO', 'KFC', 'RED ROOSTER', 'OPORTO', 'CHICKEN', 'CHIPS', 'FISH', 'SUSHI', 'JAPANESE', 'CHINESE', 'VIETNAMESE', 'NOODLE', 'KOREAN', 'INDIAN', 'AMERICAN', 'BURGER', 'FRIES', 'CHEESECAKE', 'EATERY', 'STEAK', 'WINE', 'CHEESE', 'RICE', 'POKE', 'SALAD', 'BITE']
subscriptions_list = ['PATREON', 'ONLYFANS', 'CHEGG', 'SPOTIFY', 'NETFLIX', 'STAN', 'DISNEY', 'PRIVATEINTERNET']
activities_list = ['CINEMA', 'HOYTS', 'GOLF', 'MOSHTIX', 'BOULDERING', 'CLIMBING', 'GYM', 'MUSEUM']
gaming_list = ['STEAM', 'BLIZZARD', 'MICROSOFT*']
groceries_list = ['COLES', 'FOUR SQUARE', '7-ELEVEN', 'SMKT', 'WOOLWORTHS']
transport_list = ['UBER', 'TRANSPORT','TRANSPORTNSW', 'RIDESHARE', 'PARKING']
petrol_list = [' BP ', 'AMPOL']
online_orders_list = ['AMAZON MARKETPLACE']
transfer_list = ['OSKO']
medical_list = ['DENTAL', 'DOCTOR', 'MEDICAL', 'HOSPITAL', 'PRACTICE', 'NURSE', 'RESPIRITORY', 'CLINIC']


food_delivery = []
eating_out = []
subscriptions = []
activities = []
gaming = []
groceries = []
transport = []
petrol = []
online_orders = []
transfer = []
medical = []
other = []

for purchase in purchase_list_long:
    not_assigned = True

    if not_assigned:
        for foods in food_delivery_list:
            if foods in purchase['type']:
                food_delivery.append(purchase)
                not_assigned = False
                break
    
    if not_assigned:
        for transport_type in transport_list:
            if transport_type in purchase['type']:
                transport.append(purchase)
                not_assigned = False
                break            

    if not_assigned:
        for venue in eating_out_list:
            if venue in purchase['type']:
                eating_out.append(purchase)
                not_assigned = False
                break

    if not_assigned:
        for sub in subscriptions_list:
            if sub in purchase['type']:
                subscriptions.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for activity in activities_list:
            if activity in purchase['type']:
                activities.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for game in gaming_list:
            if game in purchase['type']:
                gaming.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for grocery in groceries_list:
            if grocery in purchase['type']:
                groceries.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for pertrol_station in petrol_list:
            if pertrol_station in purchase['type']:
                petrol.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for order in online_orders_list:
            if order in purchase['type']:
                online_orders.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for trans in transfer_list:
            if trans in purchase['type']:
                transfer.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        for health_item in medical_list:
            if health_item in purchase['type']:
                medical.append(purchase)
                not_assigned = False
                break
    if not_assigned:
        other.append(purchase)
print(other)


