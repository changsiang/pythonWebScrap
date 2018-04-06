import bs4 as bs
import mysqlDAO as dao
import urllib.request
import requests
import codecs
import datetime
import scraperBlock

class Project:
    def __init__(self):
        # Declare all necessary variables
        print('Project Started....' + datetime.datetime.now().__str__())
        self.ROOT_URL = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?'
        self.array = []
        self.project_info_array = []
        self.town_list = []
        self.getHttp(
            'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO')

    def getHttp(self, http_link):
        """ This method will open up a Http Page and Download its xml content 
        It is expected the variable http_link to be https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO """
        # headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
        # response = requests.get(http_link, headers=headers)
        # sauce = response.text
        sauce = open('listBTO.htm', encoding='utf-8', errors='ignore')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        self.updateTownList(soup)

    def updateTownList(self, soup):
        """ This method will retrieve the existing town list from the database
        and update with new towns that do not already exist in the database """
        existing_town_list = dao.get_town_list()
        # H5 tag contains town name
        h5 = soup.find_all('h5')
        for town in h5:
            self.town_list.append(town.text)
        # Ensure the list has no duplication
        self.town_list = list(set(self.town_list))
        # Iterate through the list and perform db insertion
        for town in self.town_list:
            # Check again existing list making sure no duplicated entry
            if town not in existing_town_list:
                dao.insert_town_info(town)

        self.updateProjectList(soup)

    def updateProjectList(self, soup):
        """ This method will retrieve the existing project list from the database
        and update with new projects that do not already exist in the database """

        # TODO: Write method for retrieve Project List from the database

        # Update Project List:
        # Capture Project Information and Insert into database
        tbody = soup.find_all('tbody')
        # iterate through each <tbody></tbody> tag found
        # Each <tbody> tag represent projects for each town
        for body in tbody:
            # Find all <tr></tr> for each town project
            tr_attr = body.find_all('tr')
            # Each project has 2 <tr></tr> tag. Iterate through them
            for tr in tr_attr:
                # Get the attribute in the <tr id> tag. The format is <<BTOPeriod;Town;Room Type; Project Name>>
                tr_len = str(tr['id'][:-1]).split(';').__len__()
                # There is contamination from <<BTOPeriod;Town;Project Name>> tag. Use If condition to exclude that tag out
                if tr_len > 3:
                    # Split the string and file it into project_info_array for later usage
                    self.project_info_array = str(tr['id']).split(';')
                    # Find URL for specific project
                    atag = tr.find_all('a')
                    for href in atag:
                        project_url = self.ROOT_URL + href.get('href')[68:-18]
                # This is to get the various number attribute of flats offered
                td = tr.find_all('td')
                array = [i.text for i in td]
                # print('----------------------------------------------------------------------')

                if self.project_info_array.__len__() > 0 and array.__len__() > 5:
                    dao.insert_project_info(self.project_info_array[0], self.project_info_array[1], self.project_info_array[3], self.project_info_array[2], array[1], project_url)
                    dao.insert_project_hx_data(self.project_info_array[3], self.project_info_array[2], array[2], array[3], array[4], array[5])

                    # print('Project ID: ' + self.project_info_array[0])
                    # print('Town: ' + self.project_info_array[1])
                    # print('Room Type: ' + self.project_info_array[2])
                    # print('Project Name: ' + self.project_info_array[3])

                    # print('Project URL: ' + project_url)
                    # print('Units Offered: ' + array[1])
                    # print('Units Available: ' + array[2])
                    # print('Chinese Quota: ' + array[3])
                    # print('Malay Quota: ' + array[4])
                    # print('Others Quota: ' + array[5])
    # def proceed_to_block(self):
    #    town_list = dao.get_town_list()
    #    for town in town_list:
    #        scraperBlock.Blocks(town)
