import scraper as scraper
import scraperBlock as scraperBlock
import scraperUnits as scraperUnits
import mysqlDAO as dao
import datetime

startTime = datetime.datetime.now()

# scraper.Project()
# project_list = dao.get_all_project_hyperlink()
# block_list = dao.get_all_block_hyperlink()

# for project in project_list:
#    print(project)
#    scraperBlock.Blocks('Hello')

# for block in block_list:
scraper.Project()
scraperBlock.Blocks('Hello')
scraperUnits.Units('Hello')

endTime = datetime.datetime.now()
diffTime = (endTime - startTime).__str__()
print(diffTime)
