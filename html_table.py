# from random import randrange
import os


def wrap(a, tag):
    "Wraps in <td> tag the a"
    tag1 = tag
    if tag == "table":
        tag1 = "table border=1"
    if tag == "td" and a.strip().replace(".", "").isdigit():
        print(a, "is a number")
        tag1 = "td style=\"text-align:right\""
    return f"<{tag1}>{a}</{tag}>"


def split(tab):
    "Splits a multiline string in a list of items divided by comma for line"
    tab = tab.splitlines()
    for n, row in enumerate(tab):
        tab[n] = row.split(",")
    return tab


def table(tab):
    html = ''  # contain HTML
    for n, x in enumerate(tab):
        for a in x:
            html += "<tr>"
    html = wrap(html, "table")
    return html


data = table(split(
    """
    Impiegato, Performance, data
    Rossi Mario, 1000, 1/2/2018
    Baldo Franco, 2000, 1/2/2018
    """
)[1:-1])
print(data)

with open("Simple.html", "w", encoding="utf-8") as filehtml:
    filehtml.write(data)

os.system("Simple.html")
