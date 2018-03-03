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

# Capture Project Information and Insert into database
tbody = soup.find_all('tbody')
for rows in tbody:
    table_row = rows.find_all('tr')
    for tr in table_row:
        td = tr.find_all('td')
        count = tr.find_all('td', colspan='6')
        for pn in count:
            print(pn.string)

for rows in tbody:
    table_row = rows.find_all('tr')
    rowlen = table_row.__len__()
    print(rowlen)
    for i in range(1, rowlen, 1):
        tr = table_row[i]
        td = tr.find_all('td')
        a = tr.find_all('a')
        href = [i.get('href')[68:-1] for i in a]
        row = [i.text for i in td]
        row.append(href)
        print(row)
