# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up the executable path for the website
executable_path ={'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Instruct Splinter to visit the website
url = 'http://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Parse the html
# The data Robin wants to collect from this particular website is the most recent news article along with its summary. 
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')    # different way to write 'div', class_='list_test'

# Assign the title and summary text to variables
slide_elem.find('div', class_='content_title')
# slide_elem.find('div.content_title')   # same result
print(slide_elem)

# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()    # .get_text() is used only the test of the element is returned
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com/'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')    # get('src') pulls the link to the image
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Create a new df from the HTML table. read_html specifically searches and returns a list of tables found in the HTML
df = pd.read_html('https://galaxyfacts-mars.com')[0] 
# Assign columns to the new DF for addtional clarity
df.columns=['Description', 'Mars', 'Earth']
# Turn the Description column into the df's index   inplace=True measn that the updated index will remain in place
# without having to assign the df to a new varible.
df.set_index('Description', inplace=True)
df

# Convert the df back into HTML code
df.to_html()

browser.quit()


