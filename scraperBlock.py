import bs4 as bs
import mysqlDAO as dao

sauce = open('listBLOCK.html', encoding='utf-8', errors='ignore')
soup = bs.BeautifulSoup(sauce, 'lxml')

# Declare all using variables
address = ''
block = ''
availability = ''
project_name = ''
postal_code = '000000'

def blue_or_red(color):
    if color == '#cc0000':
        return 'Fully Taken'
    elif color == '#000099':
        return 'Available'
    else:
        return 'Unknown'

def get_address(tooltip):
    span = soup.find_all('span', {'data-selector':tooltip})
    for sp in span:
        return(sp.get('title'))

def get_project_hyperlink():
    # Get Project Hyperlink
    a_tags = soup.find('a', {'class':'mobile-nav-back js-mobile-nav-back'})
    hyperlink = a_tags.get('href')[:-1]
    return hyperlink

# Get list of Block Number
p_font = soup.find_all('font')
for p in p_font:
    fonts = p.find_all('font')
    tooltip = p.get('aria-describedby')
    if str(tooltip).__len__() > 4:
        address = get_address(str(tooltip))
        # print(address)
        hyperlink = get_project_hyperlink()
        project_name = dao.get_project_name_by_hyperlink(hyperlink)
        # print(project_name)
    for font in fonts:
        availability = blue_or_red(str(font.get('color')))
        block = font.text
        # print(font.text + ' ' + color)
        print('Project: '+ project_name + ' Block ' + block + ' ' + address + ' Status: ' + availability )
        # dao.insert_block_info(postal_code, block, project_name, address, availability)


        



