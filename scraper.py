import bs4 as bs
import mysqlDAO as dao
# import urllib.request
# import requests
# import codecs
# headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0"}
# response = requests.get('https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13SEstateSummary?sel=BTO', headers=headers)
# sauce = response.text
sauce = open('listBTO.htm', encoding='utf-8', errors='ignore')
soup = bs.BeautifulSoup(sauce, 'lxml')
# print(soup.find_all('a'))
string_list = []
for href in soup.find_all('a'):
    # print(href.get('href'))
    if ((href.get('href')[:4]) == 'java'):
        string_list.append(href.get('href')[68:-1])

# print('string_list')

for string in string_list:
    print(string)

tables = soup.find_all('table')
for table in tables:
    if table.findParent("table") is None:
        print(str(table).replace(u'\xa0', u' '))

print("------------------ Line Break ---------------------")

project_count = 0

tbody = soup.find_all('tbody')
for rows in tbody:
    table_row = rows.find_all('tr')
    for tr in table_row:
        td = tr.find_all('td')
        count = tr.find_all('td', colspan='6')
        if(count.__len__() > 0):
            project_count += count.__len__()
        a = tr.find_all('a')
        href = [i.get('href')[68:-1] for i in a]
        row = [i.text for i in td]
        print(href)
        print(row)


# table_row = table.find_all('tr')

# for tr in table_row:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

town = 'Sengkang'
flat_type = 'BTO'
des_type = 'A'
ethnic = 'Y'
flat = '3-Room%20(income%20ceiling%20$6,000)'
view_option = 'A'
dteBallot = '201708'
projName = ''


url = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=' + town + '&Flat_Type=' + flat_type + '&DesType=' + \
    des_type + '&ethnic=' + ethnic + '&Flat=' + flat + '&ViewOption=' + \
    view_option + '&dteBallot=' + dteBallot + '&projName=' + projName

print(url)
print(project_count)

town_list = []

existing_town_list = dao.get_town_list()
# Capture Town Name and Insert into Database
# H5 tag contains town name
h5 = soup.find_all('h5')
for town in h5:
    town_list.append(town.text)
# Ensure the list has no duplication
town_list = list(set(town_list))
# Iterate through the list and perform db insertion
for town in town_list:
    # Check again existing list making sure no duplicated entry
    if town not in existing_town_list:
        dao.insert_town_info(town)

# Declare all necessary variables
ROOT_URL = 'https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?'
array = []
project_url = ""
project_info_array = []

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
            project_info_array = str(tr['id']).split(';')
            # Find URL for specific project
            atag = tr.find_all('a')
            for href in atag:
                project_url = ROOT_URL + href.get('href')[68:-18]
        # This is to get the various number attribute of flats offered
        td = tr.find_all('td')
        for cells in td:
            for cell in cells:
                # There are other string contamination for <td></td> tag
                # I'm only interested in numbers. Use If condition to exclude non int values
                if str(cell).isdigit():
                    array.append(cell)

        print('----------------------------------------------------------------------')

        if project_info_array.__len__() > 0:
            print('Project ID: ' + project_info_array[0])
            print('Town: ' + project_info_array[1])
            print('Room Type: ' + project_info_array[2])
            print('Project Name: ' + project_info_array[3])

        print('Project URL: ' + project_url)

        if array.__len__() > 0:
            print('Units Offered: ' + array[0])
            print('Units Available: ' + array[1])
            print('Chinese Quota: ' + array[2])
            print('Malay Quota: ' + array[3])
            print('Others Quota: ' + array[4])
