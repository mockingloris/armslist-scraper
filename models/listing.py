from bs4 import BeautifulSoup

class Listing:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')

    @property
    def title(self):
        return self._soup.find('h1').string.strip()

    @property
    def price(self):
        span_contents = self._soup.find('span', {'class': 'price'})
        junk, price = span_contents.string.strip().split('$ ')
        return price

    @property
    def imgs(self):
        image_tags = self._soup.find_all('img', {'class': 'gallery'}) # have to sort out repeats
        return image_tags
        # for image_tag in image_tags:
        #     image_url = image_tag.img['src']
        #     return image_url

    @property
    def location(self):
        location_ul = self._soup.find('ul', {'class': 'location'})
        location_div = location_ul.find_all('div')[1]
        return location_div.text.strip() #coming out as unicode string instead of regular

    @property
    def description(self):
        desc = self._soup.find('div', {'class': 'postContent'})
        return desc.text.strip()


    # cat, man, cali, action, firetype, listed on, postID
    # registered (t/f) or user type private reg, private unreg

    # test URLS
    # http://www.armslist.com/posts/5577404/montgomery-alabama-handguns-for-sale-trade--ruger-44-magnum-7-5--super-blackhawk
    # http://www.armslist.com/posts/5534229/jacksonville-florida-rifles-for-sale--new-sig-sauer-mcx-5-56-rifle
    # http://www.armslist.com/posts/5577694/south-west-florida-handguns-for-sale--ar-pistol