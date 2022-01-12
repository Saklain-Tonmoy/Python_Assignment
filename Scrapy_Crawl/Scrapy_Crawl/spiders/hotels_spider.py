import scrapy

import json

import mysql.connector

#connect the db
connection = mysql.connector.connect(
  host = "localhost",
  database = "mydb",
  user = "root",
  password = ""
)

mycursor = connection.cursor()


def storeBestHotels(name, image, location, neighbor, price, stars, score, amenities):
    sql = "SELECT * FROM best_hotels WHERE name = %(value1)s AND location = %(value2)s"
    params = {'value1':name, 'value2':location}
    mycursor.execute(sql, params)
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        sqlQuery = "INSERT INTO best_hotels (name, image, location, neighborhoodName, price, stars, score, amenities) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sqlQuery, (name, image, location, neighbor, price, stars, score, amenities))
        connection.commit()
        print(mycursor.rowcount, " record stored")
        print()
    else:
        print("Data already exists")

def storeLandmarkHotels(name, image, location, landmark, neighbor, price, stars, score, amenities):
    sql = "SELECT * FROM landmark_hotels WHERE name = %(value1)s AND location = %(value2)s"
    params = {'value1':name, 'value2':location}
    mycursor.execute(sql, params)
    myresult = mycursor.fetchall()
    if(len(myresult) == 0):
        sqlQuery = "INSERT INTO landmark_hotels (name, image, location, landmark, neighborhoodName, price, stars, score, amenities) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sqlQuery, (name, image, location, landmark, neighbor, price, stars, score, amenities))
        connection.commit()
        print(mycursor.rowcount, " record stored")
        print()
    else:
        print("Data already exists")

def storeHotelDeals(place, image, location, price, stars):
    sql = "SELECT * FROM hotel_deals WHERE place = %(value1)s AND location = %(value2)s"
    params = {'value1':place, 'value2':location}
    mycursor.execute(sql, params)
    myresult = mycursor.fetchall()
    if(len(myresult) <= 1):
        sqlQuery = "INSERT INTO hotel_deals (place, image, location, price, stars) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sqlQuery, (place, image, location, price, stars))
        connection.commit()
        print(mycursor.rowcount, " record stored")
        print()
    else:
        print("Data already exists")
    

class HotelsSpider(scrapy.Spider):
    name = "hotels"
    location = 'Thailand-Hotels.238.dc.html'
    locationName = location.split('Hotels')[0][0 : len(location.split('Hotels')[0])-1]
    start_urls = [
        'http://www.kayak.co.in/' + location,
    ]

    def parse(self, response):

        print('#####################################################')
        print('Best Hotels Starts')
        print('#####################################################')
        print()

        str_data = response.css('#__R9_HYDRATE_DATA__::text').get()
        if(str_data != None):
            json_data = json.loads(str_data)
            best_hotels = json_data['serverData']['contentState']['bestHotelsModel']['bestHotels']
            for i in range(0, len(best_hotels), 1):
                name = best_hotels[i]['name']
                image = best_hotels[i]['imageUrl'].split('?')[0]
                neighborhoodName = best_hotels[i]['neighborhoodName']
                # if(best_hotels[i]['neighborhoodName'] == ""):
                #     neighborhoodName = self.location.split('-')[0]
                # else:    
                #     neighborhoodName = best_hotels[i]['neighborhoodName']
                price = best_hotels[i]['price']
                stars = best_hotels[i]['stars']
                score = best_hotels[i]['score']/10
                amenities = best_hotels[i]['features']
                storeBestHotels(name, image, self.locationName, neighborhoodName, price, stars, score, (",".join(amenities)))
                print()

            print('####################################################')
            print('LandMark Hotels Starts')
            print('####################################################')
            print()

            landmark_hotels = json_data['serverData']['contentState']['bestHotelsModel']['landmarkHotels']
            landmark = json_data['serverData']['contentState']['bestHotelsModel']['landmark']['name']

            for i in range(0, len(landmark_hotels), 1):
                name = landmark_hotels[i]['name']
                image = landmark_hotels[i]['imageUrl'].split('?')[0]
                neighborhoodName = landmark_hotels[i]['neighborhoodName']
                price = landmark_hotels[i]['price']
                stars = landmark_hotels[i]['stars']
                score = landmark_hotels[i]['score']/10
                amenities = landmark_hotels[i]['features']
                storeLandmarkHotels(name, image, self.locationName, landmark, neighborhoodName, price, stars, score, (",".join(amenities)))
                # print(name, neighborhoodName, price, score, (",".join(amenities)))
                print()
        
        else:
            if(len(response.css('div.Hotels-Region-LatestHotelDeals'))!=0):
                ### Hotel Deals portion starts
                latest_hotels = response.css('div.Hotels-Region-LatestHotelDeals .deals-cities-grid .col-1-3-l')

                for i in range(0, len(latest_hotels)):
                    place = latest_hotels[i].css('div.deal-city a .deal-city-img .deal-city-name::text').get()
                    image_link = 'https://www.kayak.co.in' + latest_hotels[i].css('div.deal-city a .deal-city-img img::attr(src)').get().split('?')[0]
                    for j in range(0,len(latest_hotels[i].css('div.deal-city .deal-city-details .deal-city-detail'))):
                        section = latest_hotels[i].css('div.deal-city .deal-city-details .deal-city-detail')[j]
                        stars = str(section.css('div.col-5-12 span::text').get())
                        price = str(section.css('div.col-5-12 span strong::text').get())
                        storeHotelDeals(place, image_link, self.locationName, stars, price)
                        print()
                    
            if(len(response.css('div.Hotels-Region-HotelsCardList')) !=0 ):
                ### Best Hotel portion starts
                for i in response.css('div.resultCardsListCarousel .slickHotelCard'):
                    image_link = i.css('div.js-hotelCard a img::attr(src)').get().split('?')[0]
                    name = i.css('div.js-hotelCard .js-hotelCardContent div div a::text').get()
                    rating = i.css('div.js-hotelCard .js-hotelCardContent div .js-RatingText::text').get()
                    price = i.css('div.js-hotelCard .js-hotelCardContent .best-hotel ._iBD .js-price::text').get()
                    length = len(price) - 1
                    formattedPrice = price[1:length]
                    storeBestHotels(name, image_link, self.locationName, "", formattedPrice, "", rating, "")
                    print()

        print('#####################################################')
        print('CRAWLING ENDS')
        print('#####################################################')
        print()






        # print('#######################################################')
        # print('MYSQL Table structure')
        # print('#######################################################')
  

        # CREATE TABLE IF NOT EXISTS `best_hotels` (
        #         `id` BIGINT(255) NOT NULL AUTO_INCREMENT,
        #         `name` VARCHAR(255) NOT NULL,
        #         `image` VARCHAR(255) NULL DEFAULT NULL,
        #         `location` VARCHAR(255) NOT NULL,
        #         `neighborhoodName` VARCHAR(255) NULL DEFAULT NULL,
        #         `price` VARCHAR(255) NOT NULL,
        #         `stars`  VARCHAR(255) NULL DEFAULT NULL,
        #         `score` VARCHAR(255) NULL DEFAULT NULL,
        #         `amenities` VARCHAR(255) NULL DEFAULT NULL,
        #         PRIMARY KEY(`id`)
        #       ) COLLATE='utf8_general_ci' ENGINE=INNODB AUTO_INCREMENT=1;




        # CREATE TABLE IF NOT EXISTS `landmark_hotels` (
        #         `id` BIGINT(255) NOT NULL AUTO_INCREMENT,
        #         `name` VARCHAR(255) NOT NULL,
        #         `image` VARCHAR(255) NULL DEFAULT NULL,
        #         `location` VARCHAR(255) NOT NULL,
        #         `landmark` VARCHAR(255) NOT NULL,
        #         `neighborhoodName` VARCHAR(255) NULL DEFAULT NULL,
        #         `price` VARCHAR(255) NOT NULL,
        #         `stars`  VARCHAR(255) NULL DEFAULT NULL,
        #         `score` VARCHAR(255) NULL DEFAULT NULL,
        #         `amenities` VARCHAR(255) NULL DEFAULT NULL, 
        #         PRIMARY KEY(`id`)
        #       ) COLLATE='utf8_general_ci' ENGINE=INNODB AUTO_INCREMENT=1;




        # CREATE TABLE IF NOT EXISTS `hotel_deals` (
        #         `id` BIGINT(255) NOT NULL AUTO_INCREMENT,
        #         `place` VARCHAR(255) NOT NULL,
        #         `image` VARCHAR(255) NULL DEFAULT NULL,
        #         `location` VARCHAR(255) NOT NULL,
        #         `price` VARCHAR(255) NOT NULL,
        #         `stars`  VARCHAR(255) NULL DEFAULT NULL, 
        #         PRIMARY KEY(`id`)
        #     ) COLLATE='utf8_general_ci' ENGINE=INNODB AUTO_INCREMENT=1;