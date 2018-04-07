import scraper as scraper
import scraperBlock as scraperBlock
import scraperUnits as scraperUnits
import mysqlDAO as dao
import datetime
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def retrieveHTML(prev_http_link, http_link, syntex):
    project_filename = './HTML_FILES/' + syntex + \
        str(datetime.datetime.now().isoformat().__str__()).replace(
            ':', '-').replace('.', '') + '.html'
    try:
        options = Options()
        print('Options: ', datetime.datetime.now().__str__())
        options.add_argument("--headless")
        print('Add Argument: ', datetime.datetime.now().__str__())
        driver = webdriver.Firefox(
            firefox_options=options, executable_path="C:\\Utility\\geckodriver.exe")
        print('Driver: ', datetime.datetime.now().__str__())
        driver.get(prev_http_link)
        driver.get(http_link)
        file = open(project_filename, 'w')
        file.write(driver.page_source)
        file.close()
        # opener = urllib.request.build_opener()
        # opener.addheaders = [
        #    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')]
        # urllib.request.install_opener(opener)
        # urllib.request.urlretrieve(http_link, project_filename)
        return project_filename
    except:
        print('retrieveHTML Exception')
        return 1


startTime = datetime.datetime.now()
# btoselection = retrieveHTML('http://www.google.com','https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO', 'BTOSelection-')
# scraper.Project(btoselection)

# project_list = dao.get_all_project_hyperlink()
# for hyperlink in project_list:
#     scraperBlock.Blocks(retrieveHTML('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO',hyperlink, 'BTOBlocks-'), hyperlink)

block_list = dao.get_all_block_hyperlink()
print('Time Taken: ', datetime.datetime.now().__str__())
for hyperlink in block_list:
    print('Time Taken: ', datetime.datetime.now().__str__())
    # print(hyperlink)
    scraperUnits.Units(retrieveHTML(
        'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName=', hyperlink, 'BTOUnits-'), hyperlink)

endTime = datetime.datetime.now()
diffTime = (endTime - startTime).__str__()
print('Time Taken: ', diffTime)


# for block in block_list:
# scraper.Project()
# scraperBlock.Blocks('Hello', 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName=')
# scraperUnits.Units('Hello', '')


# headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
# q = urllib.request.Request('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO')
# q.add_header("user-agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0")
# a = urllib.request.urlretrieve(q, filename)
# urllib.request.urlopen('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO', )
# response = requests.get(http_link, headers=headers)
