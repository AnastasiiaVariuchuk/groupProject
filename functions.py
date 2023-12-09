import random

from classes import Parcel, Recipient, Roads


def generate_random_parcel():
    random_width = random.randint(0, Parcel.LENGTH)
    random_weight = random.randint(0, Parcel.HEIGHT)
    return Parcel(random_width, random_weight)


def generate_random_parcels(number_of_parcels):
    parcels = []
    for _ in range(number_of_parcels):
        parcel = generate_random_parcel()
        parcels.append(parcel)
    return parcels

def generate_random_recipient():
    address = random.randint(1000, 9999)
    return Recipient(address)


def generate_random_recipients(number_of_recipients):
    recipients = []
    for _ in range(number_of_recipients):
        recipient = generate_random_recipient()
        recipients.append(recipient)
    return recipients


def generate_random_recipient():
    address = random.randint(1000, 9999)
    return address


# def generate_random_recipients(number_of_recipients):
#     recipients = []
#     for _ in range(number_of_recipients):
#         recipient = generate_random_recipient()
#         recipients.append(recipient)
#     return recipients
#

# def generate_random_roads(number_of_roads):
#     addresses = generate_random_recipients(number_of_roads * 2)
#     random.shuffle(addresses)
#     random_roads = []
#     for i in range(0, len(addresses), 2):
#         address1, address2 = addresses[i], addresses[i + 1]
#         road_length = random.randint(1, 50)
#         road = Roads(address1, address2, road_length)
#         random_roads.append(road)
#     return random_roads


def generate_random_recipients(number_of_recipients):
    recipients = []
    for _ in range(number_of_recipients):
        address = random.randint(1000, 9999)
        recipient = Recipient(address)
        recipients.append(recipient)
    return recipients


def generate_road_matrix(recipients):
    road_matrix = {}
    for i, recipient1 in enumerate(recipients):
        for j, recipient2 in enumerate(recipients):
            if i != j:
                road_length = random.randint(1, 50)
                road_matrix[(recipient1.address, recipient2.address)] = road_length
    return road_matrix