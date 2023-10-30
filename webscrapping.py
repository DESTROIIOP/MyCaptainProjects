import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the no. of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the name of db", type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-chennai/?page="
page_num_MAX = args.page_num_max
scrapped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url = oyo_url +str(page_num)
    print("Get request for: " + url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, "html.paser")
    all_hotels = soup.find_all("div", {"class": "HotelCardListing"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"] = hotel.find("h3",{"class": "ListingHotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span",{"itemprop": "streetaddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class": "ListingPrice_finalPrice"}).text

        try:
            hotel_dict["rating"] = hotel.find("span",{"class": "HotealRating_ratingsummary"}).text
        except AttributeError:
            pass

        parent_amenities_element = hostel.find("div",{"class": "amenityWrapper"})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div",{"class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"]= ','.join(amenities_list[:-1])

        scrapped_info_list.append(hotel_dict)

dataframe = pandas.DataFrame(scrapped_info_list)
print("Creating csv file......")
dataframe.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)
