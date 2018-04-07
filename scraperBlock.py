import bs4 as bs
import mysqlDAO as dao
import datetime


class Blocks:

    def __init__(self, filename, hyperlink):
        # Declare all using variables
        print('Block Started....' + datetime.datetime.now().__str__())
        self.address = ''
        self.block = ''
        self.availability = ''
        self.project_name = ''
        self.postal_code = '000000'
        self.project_hyperlink = hyperlink
        self.getHttp(filename)

    def getHttp(self, filename):
        # headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
        # response = requests.get(http_link, headers=headers)
        # sauce = response.text
        sauce = open(filename,
                     encoding='utf-8', errors='ignore')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        self.get_block_number(soup)

    def get_block_number(self, soup):
        # Get list of Block Number
        p_font = soup.find_all('font')

        for p in p_font:
            fonts = p.find_all('font')
            title = p.get('title')
            if title != None:
                address = title
                # print(address)
                hyperlink = self.project_hyperlink
                project_name = dao.get_project_name_by_hyperlink(hyperlink)
            # print(project_name)
            for font in fonts:
                availability = self.blue_or_red(str(font.get('color')))
                block = font.text
                # print(font.text + ' ' + color)
                # print('Project: ' + project_name + ' Block ' + block + ' ' + address +
                #      ' Status: ' + availability + ' Hyperlink ' + self.get_block_hyperlink(soup, block))
                dao.insert_block_info(self.postal_code, block, project_name, address,
                                      availability, self.get_block_hyperlink(soup, block, self.project_hyperlink))
        print('Block Ends... With', self.project_hyperlink)

    def blue_or_red(self, color):
        if color == '#cc0000':
            return 'Fully Taken'
        elif color == '#000099':
            return 'Available'
        else:
            return 'Unknown'

    def get_address(self, tooltip, soup):
        span = soup.find_all('span', {'data-selector': tooltip})
        for sp in span:
            return(sp.get('title'))

    def get_project_hyperlink(self, soup):
        # Get Project Hyperlink
        a_tags = soup.find(
            'a', {'class': 'mobile-nav-back js-mobile-nav-back'})
        hyperlink = a_tags.get('href')[:-1]
        return hyperlink

    def get_block_hyperlink(self, soup, block, project_hyperlink):
        div = soup.find_all('div')
        for d in div:
            di = d.get('onclick')
            if(di != None):
                check_blk = str(di).replace('checkBlk', '').replace(
                    '\'', '').replace('(', '').replace(')', '').replace(';', '').split(',')
                if(check_blk[0] == block):
                    return self.block_hyperlink(soup, block, check_blk[1], check_blk[2], project_hyperlink)

    def block_hyperlink(self, soup, block, neighbourhood, contract, project_hyperlink):
        project_link = project_hyperlink
        sArray = str(project_link).split('&')
        projParam = {}
        for param in sArray:
            projParam[param.split('=')[0].replace('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?', '')] = param.split('=')[1].replace(
                '+', '%20').replace('%28', '(').replace('%29', ')').replace('%2F', '/')
        # print(projParam)
        # hyperlink = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?'\
        #     .join('Town=').join(projParam['Town'])\
        #     .join('&Flat_Type=').join(projParam['Flat_Type'])\
        #     .join('&selectedTown=').join(projParam['Town'])\
        #     .join('&Flat=').join(projParam['Flat'])\
        #     .join('&ethnic=Y&ViewOption=A')\
        #     .join('&Block=').join(block)\
        #     .join('&DesType=').join(projParam['DesType'])\
        #     .join('&EthnicA=Y&EthnicM=&EthnicC=&EthnicO=&numSPR=')\
        #     .join('&dteBallot=').join(projParam['dteBallot'])\
        #     .join('&Neighbourhood=').join(neighbourhood)\
        #     .join('&Contract=').join(contract)\
        #     .join('&BonusFlats1=N&searchDetails=&brochure=false')
        hyperlink = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?'\
            + 'Town=' + projParam['Town']\
            + '&Flat_Type=' + projParam['Flat_Type']\
            + '&selectedTown=' + projParam['Town']\
            + '&Flat=' + projParam['Flat']\
            + '&ethnic=Y&ViewOption=A'\
            + '&Block=' + block\
            + '&DesType=' + projParam['DesType']\
            + '&EthnicA=Y&EthnicM=&EthnicC=&EthnicO=&numSPR='\
            + '&dteBallot=' + projParam['dteBallot']\
            + '&Neighbourhood=' + neighbourhood\
            + '&Contract=' + contract\
            + '&BonusFlats1=N&searchDetails=&brochure=false'
        return hyperlink
