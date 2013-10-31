import json

from book_packer import DataScraper
from book_packer import BoxOrder

# Open the list of websites
html = open('html_list.txt', 'r')

# Create a DataScraper object for each site
site1 = DataScraper(html.readline())
site2 = DataScraper(html.readline())
site3 = DataScraper(html.readline())
site4 = DataScraper(html.readline())
site5 = DataScraper(html.readline())
site6 = DataScraper(html.readline())
site7 = DataScraper(html.readline())
site8 = DataScraper(html.readline())
site9 = DataScraper(html.readline())
site10 = DataScraper(html.readline())
site11 = DataScraper(html.readline())
site12 = DataScraper(html.readline())
site13 = DataScraper(html.readline())
site14 = DataScraper(html.readline())
site15 = DataScraper(html.readline())
site16 = DataScraper(html.readline())
site17 = DataScraper(html.readline())
site18 = DataScraper(html.readline())
site19 = DataScraper(html.readline())
site20 = DataScraper(html.readline())

# Interpret the site
site1.make_soup()
site2.make_soup()
site3.make_soup()
site4.make_soup()
site5.make_soup()
site6.make_soup()
site7.make_soup()
site8.make_soup()
site9.make_soup()
site10.make_soup()
site11.make_soup()
site12.make_soup()
site13.make_soup()
site14.make_soup()
site15.make_soup()
site16.make_soup()
site17.make_soup()
site18.make_soup()
site19.make_soup()
site20.make_soup()

# Make a list of all books
library = [site1.book_info(), site2.book_info(), site3.book_info(),
               site4.book_info(), site5.book_info(), site6.book_info(),
               site7.book_info(), site8.book_info(), site9.book_info(),
               site10.book_info(), site11.book_info(), site12.book_info(),
               site13.book_info(), site14.book_info(), site15.book_info(),
               site16.book_info(), site17.book_info(), site18.book_info(),
               site19.book_info(), site20.book_info()]

# Print the order in json format
print(json.dumps(BoxOrder(library).boxes(), sort_keys=True, indent=2))