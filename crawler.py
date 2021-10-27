# -*- coding: utf-8 -*-
import requests
from lxml import html
import xlsxwriter

workbook = xlsxwriter.Workbook('crawl.xlsx')
worksheet = workbook.add_worksheet()

page_number = 1
row = 1
while True:
    response = requests.get(f"https://www.digikala.com/search/category-men-shirts/?pageno={page_number}&sortby=4").content

    response = html.fromstring(str(response, 'utf-8'))

    titles = response.xpath("/html/body/main/div[2]/div/div[1]/div/div[2]/div/article/div/ul/li/div/div/div[1]/div/a/text()")

    for title in titles:
        worksheet.write_string(row, 0, title)
        row += 1

    page_number += 1
    print(page_number)
    if page_number == 30:
        break

workbook.close()
print("end")
