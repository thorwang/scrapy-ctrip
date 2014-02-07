# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class hotelReview(Item):
    # define the fields for your item here like:
    # name = Field()

    #hotel profile
    hotel_name = Field()
    e_name = Field()
    avg_price = Field()
    url = Field()
    total_overall_rating = Field()
  	#review
    u_id = Field()
    content = Field()
    u_type = Field()
    date = Field()
    helpful = Field()
    review_overall_rating = Field()
    clean = Field()
    service = Field()
    facility = Field()
    location = Field()
    user_agent = Field()
    rooms_type = Field()
