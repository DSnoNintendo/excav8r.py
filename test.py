import excav8r
scraper = excav8r.Excva8r()

# Will save a maximum of 10 images from DuckDuckGo with search term "american flag transparent"
scraper.getDuckDuckGo("american flag transparent", max=10)
scraper.getDuckDuckGo("mexican flag transparent", max=10)