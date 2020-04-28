""""
Vlad R.
28 Apr. 2020
Script to download the filtered search results from link.springer.com

You have to manually scrub the csv file for special characters such as , and /
Working with dictionaries would've taken more time than I wanted to spend and manually opening the .csv file in Excel
to replace all occurrences of special characters was less time consuming.

"""
import requests
import csv

def download(url,file_name):
    url = url.replace('book','content/pdf') + '.pdf'
    file_download = requests.get(url)
    with open(file_name+'.pdf','wb') as file:
        file.write(file_download.content)
    file.close()

def main():
    book_list = open('SearchResults.csv','r',encoding='utf-8')
    book_list = iter(book_list)
    next(book_list)

    for line in book_list:
        fields = line.split(',')

        file_name = fields[0].strip('\"')
        url = fields[8].strip('\"')
        print(file_name, url)

        download(url,file_name)
        print('Book Done.')

if __name__ =='__main__':
    main()

