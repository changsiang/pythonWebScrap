import bs4 as bs
import mysqlDAO as dao
import datetime

class Units:

    def __init__(self, http_link):
        print('Unit Started....' + datetime.datetime.now().__str__())
        self.getHttp(http_link)
        self.project_name
        self.block_number
        self.room_type

    def getHttp(self, http_link):
        # headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
        # response = requests.get(http_link, headers=headers)
        # sauce = response.text
        sauce = open('listUNITS.html', encoding='utf-8', errors='ignore')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        # print(soup)
        self.get_project_details(soup)

    def blue_or_red(self, color):
        if color == '#cc0000':
            return 'Taken'
        elif color == '#000099':
            return 'Available'
        else:
            return 'Unknown'

    def get_project_details(self, soup):
        # Get Project Name, Block Number, Room Type
        href = soup.find('a', {'class': 'mobile-nav-back js-mobile-nav-back'})
        hyperlink = href.get('href')[:-1]
        sArray = hyperlink.split('&')
        sArray = sArray[1: sArray.__len__() - 1]
        projParam = {}
        for param in sArray:
            projParam[param.split('=')[0]] = param.split('=')[1].replace(
                '+', '%20').replace('%28', '(').replace('%29', ')').replace('%2F', '/')
        query_link = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?' + 'Town=' + projParam['selectedTown'] + '&Flat_Type=' + projParam['Flat_Type'] + '&DesType=' + projParam[
            'DesType'] + '&ethnic=' + projParam['EthnicA'] + '&Flat=' + projParam['Flat'] + '&ViewOption=' + projParam['ViewOption'] + '&dteBallot=' + projParam['dteBallot'] + '&projName='
        self.project_name = dao.get_project_name_by_hyperlink(query_link)
        self.block_number = projParam['Block']
        self.room_type = projParam['Flat']
        self.getUnits(soup)

    def getUnits(self, soup):
        # Get List of Units (font tag within a font tag)
        unitArray = {}
        p_td = soup.find_all('td')
        for td in p_td:
            units = td.find_all('font')
            for unit in units:
                if unit.text.strip()[0] == '#' and unit.get('color') != None:
                    unitArray[str(unit.text).strip().split(
                        '\n')[0]] = unit.get('color')
            # print(unit.get('color'), '->', str(unit.text).strip().split('\n')[0])
            # print(str(unit.text).strip().split('\n')[0])
        self.get_availability_status(unitArray, soup)

    def get_availability_status(self, unitArray, soup):
        # Get Availabity Status
        for unit in unitArray:
            status = self.blue_or_red(unitArray[unit])
            # print(unit, status) # file DAO here
            # Get Price for the corrosponding unit
            if(status != 'Taken'):
                data_selector = soup.find_all('span', {'data-selector': unit})
                for ds in data_selector:
                    priceArray = ds.get('title').replace('_', '').split('<br>')
                    size = priceArray[priceArray.__len__() - 1].replace('Sqm', '')
                    # print('size', size)
                    for price in priceArray[:-2]:
                        # priceSplit = price.split('-')
                        unit_price = price.split('-')[0].strip().replace('$', '').replace(',', '')
                        # print(unit_price)
                        year_of_lease = price.split('-')[1].strip()[:-6]
                        # print(year_of_lease)
                        # print(self.block_number, str(unit).split('-')[0].replace('#', ''), str(unit).split('-')[1] ,self.project_name, status, datetime.datetime.now(), datetime.datetime.now(), self.room_type, unit_price, year_of_lease, size)
                        dao.insert_units_info(self.block_number, str(unit).split('-')[0].replace('#', ''), str(unit).split('-')[1] ,self.project_name, status, datetime.datetime.now(), datetime.datetime.now(), self.room_type, unit_price, year_of_lease, size)
            else:
                dao.insert_units_info(self.block_number, str(unit).split('-')[0].replace('#', ''), str(unit).split('-')[1] ,self.project_name, status, datetime.datetime.now(), datetime.datetime.now(), self.room_type, -1, -1, -1)

#dao.insert_units_info(self.block_number, str(unit).split('-')[0].replace('#', ''), self.project_name, status, datetime.datetime.now(), datetime.datetime.now(), self.room_type, unit_price, year_of_lease, size)
# def insert_units_info(self.block, floor, unit, self.project_name, isTaken, date_taken, date_updated, self.room_type, price, year_of_lease, size):
# Get Price for the corrsoponding units
# test = soup.find_all('span', {'data-selector': '#15-126'})
# for t in test:
#    priceArray = t.get('title').replace('_', '').split('<br>')
#    print(t.get('title').replace('_', '').split('<br>'))
# for price in priceArray:
#    print((price.split('-')[0]).strip(), (price.split('-')[1]).strip())
