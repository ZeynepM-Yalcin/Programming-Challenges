import csv
from pathlib import Path
from operator import index


def read_html(path):
    with open (path, 'r') as file:
        htmlFile = file.read()
        return htmlFile

def transfer(csv, html):
    indexNameList = [[0,'link'], [1, 'initials'], [2, 'name']]
    for currentItem in indexNameList:
        for x in range (5):
            Name = currentItem[1] + str(x+1)
            html = html.replace (Name, csv[x][currentItem[0]])
    return html

def write(path, html):
    with open (path, 'w') as htmlfile:
        htmlfile.write(html)

if __name__ == "__main__":   
    csv = read_csv(csv_path='south.csv')
    html = read_html(path='south.html')
    html = process(csv, html)
    write_html(path="south2.html", html=html)
