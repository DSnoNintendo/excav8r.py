import excav8r

scraper = excav8r.Excva8r()


# Will save a maximum of 500 images from DuckDuckGo with keyword "single orange png"
# to a folder called excav8r in the working directory
scraper.getDuckDuckGo("single orange png", max=500)

# Will save images from both DuckDuckGo and Google Images with keyword "hot dog"
# to a folder called ScrapedImages in the working directory
# The function will return all images found in a 30 second timeframe
scraper.getAll("hot dog png", destination="ScrapedImages", timeout=30)

#Will return a list of up to 20 PIL Image objects from Google Images with keyword "oranges"
#timeout argument is null if as_list is True
images = scraper.getGoogle("oranges", as_list=True, max=20)

#close headless browser when
scraper.closeBrowser()

