import requests

from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url)  # Pass  one argument (url)
    
    # Now we create  (url instance variable) 
        self.url = url
        
        # Then we need one user agent

        self.user_agent={"User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36



 
# Now we create one object (Iphone)

Iphone11 = PriceTracker(url="https://www.amazon.in/Apple-iPhone-11-64GB-Black/dp/B07XVMDRZY?ref_=Oct_DLandingS_D_6bfd9560_60&smid=A14CZOWI0VEHLG")



