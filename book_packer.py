
import urllib2
from operator import itemgetter

from bs4 import BeautifulSoup


class DataScraper(object):
    """Scrapes the data from an Amazon url"""

    def __init__(self, url=None):
        self.url = url
        self.soup = None

    def set_url(self, url):
        # Sets the url
        self.url = url
        self.soup = None

    def make_soup(self):
        # BeautifulSoup reads the url
        if self.url == None:
            print 'DataScraper has no URL'
        try:
            self.soup = BeautifulSoup(urllib2.urlopen(self.url).read())
        except:
            print 'DataScraper could not get data'
        return self.soup

  #      self.soup = BeautifulSoup(self.page.read())
  #      return self.soup


    def book_title(self):
        """ Gets the book title from an Amazon url """

        # Read the title of the url
        book_info = self.soup.title.contents[0]

        # Make an array of the url title info, remove everything except the title
        book_info = book_info.split(":")
        book_info.pop()
        book_info.pop()
        book_info.pop()
        book_info.pop()
        title = str(': '.join(book_info))
        return title


    def book_author(self):
        """Gets the book author from an Amazon url"""

        # Read the url title
        book_info = self.soup.title.contents[0]

        # Make an array of the url title info, extract the author
        book_info = book_info.split(":")
        author = str(book_info[len(book_info) - 4])
        return author


    def book_isbn(self):
        """ Gets the book isbn from an Amazon url """

        # Scrape ISBN-10 from the html code
        isbn = self.soup.find('b', text='ISBN-10:').next_sibling
        return isbn


    def book_price(self):
        """ Gets the book price from an Amazon url """

        # Scrape the price from the html code
        price = self.soup.findAll('span', {'class': 'bb_price'})[0].contents[0]
        price = str(price.split("$")[1])
        return price


    def book_weight(self):
        """ Gets the book weight from an Amazon url """

        # Scrape the shipping weight from the html code
        weight = self.soup.find('b', text='Shipping Weight:').next_sibling
        weight = float(weight.split("p")[0])
        return weight


    def book_info(self):
        """ Creates a dictionary entry for a book from an Amazon url"""

        # Scrape the title, author, isbn, price, and weight of the book
        title = DataScraper.book_title(self)
        author = DataScraper.book_author(self)
        isbn = DataScraper.book_isbn(self)
        price = DataScraper.book_price(self)
        weight = DataScraper.book_weight(self)

        # Create a dictionary entry
        book = {'title': title,
                'author': author,
                'isbn': isbn,
                'price': price,
                'weight': weight}
        return book


class BoxOrder(object):
    """ Places the books in a box, each box weighs less than 10 lbs"""

    def __init__(self, item_list):
        self.item_list = item_list
        self.weight = 10

    def boxes(self):
    # Sorts items into boxes

        # Sort items from heaviest to lightest
        self.item_list.sort(key=itemgetter('weight'))
        self.item_list.reverse()

        # Initialize boxes and associated weight by starting with one empty box
        boxes = [[]]
        boxes_weight = [0]

        # Divide items in to boxes. Start by adding items to one box.
        for item in self.item_list:
            weight = item['weight']

            # Loop over boxes and put item in box if weight limit is not exceeded
            box_iter = 0
            while box_iter < len(boxes):
                if boxes_weight[box_iter] + weight < self.weight:
                    # Weight limit is not exceeded, put book in box
                    boxes_weight[box_iter] += weight
                    boxes[box_iter].append([item])
                    break

                else:
                    # Weight limit is exceeded, check the next box
                    box_iter += 1

            if box_iter == len(boxes):
                # Book exceeded weight limit for all boxes, make a new box
                boxes.append([item])
                boxes_weight.append(weight)
        return boxes
