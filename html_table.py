import os
from openpyxl import load_workbook


wb = load_workbook(filename="eRACTS Complaint.xlsx")
ws = wb["mail"]

# contains content in HTML format
html = """
<html><body><h1>Pl find the current list of eRACTS complaint which have not yet been resolved, pl go through each case and provide current status of complaint and target date of rectification:</h1>
"""

for whole_row in ws.iter_rows(min_row=1, max_row=1):
    html += "<table border=1><tr>"
    for row in whole_row:
        html += f'<th>{row.value}</th>'
    html += "</tr>"

for whole_row in ws.iter_rows(min_row=2):
    html += "<tr>"
    for row in whole_row:
        html += f'<td>{row.value}</td>'
    html += "</tr>"

html += "</table></body></html>"
# print(html)

with open("Simple.html", "w", encoding="utf-8") as filehtml:
    filehtml.write(html)

os.system("Simple.html")
