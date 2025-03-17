import os
import requests
from django.core.files.base import ContentFile
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AmazonScraperSerializer
from .models import AmazoneDataScrape
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from django.conf import settings
import time

class AmazoneViewSet(viewsets.ModelViewSet):
    queryset = AmazoneDataScrape.objects.all()
    serializer_class = AmazonScraperSerializer

def download_image(image_url):
    """Download image from the URL and save it locally in Django's media directory"""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            # Extract filename from URL
            image_name = os.path.basename(urlparse(image_url).path)
            image_content = ContentFile(response.content)
            return image_name, image_content
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None, None

def amazonscrapedata(request):
    search_query = input("Which product details do you want?: ")

    # Configure Selenium options
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.amazon.in')

    product_data = []

    try:
        # Find the search box and perform search
        search_box = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Wait until search results load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"]')))

        # Loop through first 10 products
        for i in range(1, 11):
            try:
                product = driver.find_element(By.XPATH, f'//div[@data-component-type="s-search-result"][{i}]')

                # Extract product details
                product_name = product.find_element(By.XPATH, './/h2//span').text
                
                try:
                    product_price = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
                except:
                    product_price = "N/A"

                try:
                    product_delivery_time = product.find_element(By.XPATH, './/span[contains(text(), "delivery")]').text
                except:
                    product_delivery_time = "Delivery time not available"

                try:
                    product_image_url = product.find_element(By.XPATH, './/img').get_attribute('src')
                except:
                    product_image_url = None
                
                # Download and save image if available
                if product_image_url:
                    image_name, image_content = download_image(product_image_url)

                    if image_content:
                        # Create a new instance of AmazoneDataScrape
                        amazon_product = AmazoneDataScrape(
                            product_name=product_name,
                            product_price=product_price,
                            product_time=product_delivery_time
                        )
                        # Save image to the "products/" directory under media
                        amazon_product.product_image.save(f"products/product_{i}_{image_name}", image_content, save=True)
                        
                        # Save other details
                        amazon_product.save()

                        # Append to data to display
                        product_data.append({
                            "name": product_name,
                            "price": product_price,
                            "time": product_delivery_time,
                            "image": amazon_product.product_image.url
                        })

            except Exception as e:
                print(f"Error scraping product {i}: {e}")
                continue

    except Exception as e:
        print(f"Error loading search results: {e}")
    
    finally:
        driver.quit()

    context = {
        'products': product_data
    }
    return render(request, 'product_result.html', context)
