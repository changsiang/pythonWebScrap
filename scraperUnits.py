import bs4 as bs
import mysqlDAO as dao

sauce = open('listUNITS.html', encoding='utf-8', errors='ignore')
soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup)


def blue_or_red(color):
    if color == '#cc0000':
        return 'Taken'
    elif color == '#000099':
        return 'Available'
    else:
        return 'Unknown'


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
project_name = dao.get_project_name_by_hyperlink(query_link)
block_number = projParam['Block']
room_type = projParam['Flat']

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

# Get Availabity Status
for unit in unitArray:
    unitArray[unit] = blue_or_red(unitArray[unit])
    print(unit, unitArray[unit])

# Get Price for the corrsoponding units
test = soup.find_all('span', {'data-selector': '#15-126'})
for t in test:
    priceArray = t.get('title').replace('_', '').split('<br>')
    print(t.get('title').replace('_', '').split('<br>'))
for price in priceArray:
    print((price.split('-')[0]).strip(), (price.split('-')[1]).strip())
