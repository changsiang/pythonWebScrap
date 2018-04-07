import scraper as scraper
import scraperBlock as scraperBlock
import scraperUnits as scraperUnits
import mysqlDAO as dao
import datetime
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import bs4 as bs

browser = webdriver.Chrome()
browser.get('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName=')

def retrieveHTML(http_link, syntex):
    project_filename = './HTML_FILES/' + syntex + \
        str(datetime.datetime.now().isoformat().__str__()).replace(
            ':', '-').replace('.', '') + '.html'
    try:
        browser.get(http_link)
        time.sleep(5)
        source_code = browser.execute_script(
            "return document.getElementsByTagName('html')[0].innerHTML")
        file = open(project_filename, 'w')
        file.write(source_code.__str__().replace('\xa9', '').replace('\xa0', ''))
        file.close()
        return project_filename
        # opener = urllib.request.build_opener()
        # opener.addheaders = [
        #    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')]
        # urllib.request.install_opener(opener)
        # urllib.request.urlretrieve(http_link, project_filename)
    except Exception as e:
        print('retrieveHTML Exception', str(e))
        return 1


startTime = datetime.datetime.now()
btoselection = retrieveHTML('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO', 'BTOSelection-')
scraper.Project(btoselection)

project_list = dao.get_all_project_hyperlink()
for hyperlink in project_list:
    scraperBlock.Blocks(retrieveHTML(hyperlink, 'BTOBlocks-'), hyperlink)

block_list = dao.get_all_block_hyperlink()
for hyperlink in block_list:
     scraperUnits.Units(retrieveHTML(hyperlink, 'BTOUnits-'), hyperlink)


# retrieveHTML('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&DesType=A&ethnic=Y&Flat=4-Room&ViewOption=A&dteBallot=201711&projName=',
#              'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Punggol&Flat_Type=BTO&selectedTown=Punggol&Flat=4-Room&ethnic=Y&ViewOption=A&Block=401A&DesType=A&EthnicA=Y&EthnicM=&EthnicC=&EthnicO=&numSPR=&dteBallot=201711&Neighbourhood=S4&Contract=C5&BonusFlats1=N&searchDetails=&brochure=false', 'BTOUnits-')

endTime = datetime.datetime.now()
diffTime = (endTime - startTime).__str__()
print('Time Taken: ', diffTime)

# sauce = open('./HTML_FILES/BTOUnits-2018-04-07T21-03-10747642.html',
#             encoding='utf-8', errors='ignore')
# soup = bs.BeautifulSoup(sauce, 'lxml')
# print(soup)
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
