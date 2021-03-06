# Springer-Downloader
I made this script to quickly download the books Springer have publicly made available during the Covid 19 pandemic.

They have made the books available [here](https://link.springer.com/search/page/2?facet-content-type=%22Book%22&package=mat-covid19_textbooks&facet-language=%22En%22&sortOrder=newestFirst&showAll=true).

In order to download a set of books, you can add filters for your interests. After that, click on the "Download search results(CSV)" button (highlighted below in green). 

![Download Button](DownloadButton.png)

Save the .csv file and the Python script in the same folder, then modify line 22 in the script to match your .csv file name, if you did not keep the default "SearchResults.csv" name. Simply run the script and wait for your books to download.

# **Important:** 
The script will return an error if any fields other than the URL contain the comma (,) or slash (/) characters, so you have to manually open the .csv file in Microsoft Excel, select all columns **except** the URL column and find and replace all (Ctrl + H) instances of these characters to something else.

