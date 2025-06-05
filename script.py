from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By

url1 = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=worldwide&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get(url1)

# Loop to scroll through all jobs and click on "Load more results" button for infinite scrolling
i = 2
while i <= int(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        send = driver.find_element_by_xpath("//button[@aria-label='Load more results']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(3)
    except:
        pass
        time.sleep(5)

# Create empty lists for company name, job title, location, and level
companyname = []
titlename = []
locationname = []
linkname = []


# Find and append company name, title, location, and level for each job
for i in range(2, 100):
    try:
        company=driver.find_element(
            by=By.CSS_SELECTOR, value=f".jobs-search__results-list > li:nth-child({i}) > div:nth-child(1) > div:nth-child(3) > h4:nth-child(2) > a:nth-child(1)").text
        title=driver.find_element(
            by=By.CSS_SELECTOR, value=f".jobs-search__results-list > li:nth-child({i}) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)").text
        location=driver.find_element(
            by=By.CSS_SELECTOR, value=f".jobs-search__results-list > li:nth-child({i}) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > span:nth-child(1)").text
        link=driver.find_element(
            by=By.CSS_SELECTOR, value=f".jobs-search__results-list > li:nth-child({i}) > div:nth-child(1) > a:nth-child(1)").get_attribute("href")

        companyname.append(company)
        titlename.append(title)
        locationname.append(location)
        linkname.append(link)

    except Exception as e:
        print(f"Error while processing job {i}: {str(e)}")

# Create dataframes for company name, title, location, and level
companyfinal = pd.DataFrame(companyname, columns=["company"])
titlefinal = pd.DataFrame(titlename, columns=["title"])
locationfinal = pd.DataFrame(locationname, columns=["location"])
linkfinal = pd.DataFrame(linkname, columns=["link"])

# Join the dataframes
x = companyfinal.join(titlefinal)
x = x.join(locationfinal)
x = x.join(linkfinal)

print(x)

# Save data to a CSV file
x.to_csv('linkedin.csv', index=False)

# Close the browser
driver.quit()
