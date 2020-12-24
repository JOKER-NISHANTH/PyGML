'''
import requests
from bs4 import BeautifulSoup   # ref 2
import csv

# url = "https://www.amazon.com/b?node=16225007011&pf_rd_r=12Z9QG1ZJXF7WACMZGJB&pf_rd_p=a13f1949-dc1c-4090-9236-ef9627cd9724"


def ExtractData(url):
    response = requests.get(url=url).content  # ref 1
    soup = BeautifulSoup(response=response, parse_only="lxml") # Now we create bs4 object , soup is variable , 1st argument ah html content pass
                                                            # painnaroim so we pass response variable  -- then we tell the parse type (html.parse--htmlfile lib---lxml)

    # table = soup.find("table")
    table = soup.find("table", {"Class/ID":""})   # It's used to get particular table with help of CLASS / ID
    #print(table)

#-----------x--------------------------x------------------------------x--------------------------x-------------------------x-
    # find the particular tag , so we create thead variable

    # thead = table.find("thead")
    # print(thead)

    # thead = table.find("thead").find("tr")   # Its return 1st element
    # print(thead)

#-------------x--------------------x---------FIND_ALL---------x---------------------x-------------------x--------------x-----
    thead = table.find("thead").find_all("tr")
    # print(thead)

# ------x---------------------x------------Filter the head (head Scraping)----------------x-----------------------x---------------------x------------
   # table_head = [ for th in thead]  # One by one ah print painnuim ethula particular words vanuim naa
    table_head = [th.text for th in thead]
    #print(table_head)

'''
#-----------X---How to scraping the datas in table---------------X----------------------------
'''
#      # table_body=table.find("tbody")

    #table_body = table.find("tbody").find_all("tr")
    #print(table_body)

    table_body = table.find("tbody").find_all("tr")
    for tr in table_body
        #print(tr)

        #table_data = [ for td in tr.find_all('td')]
        #table_data = [td for td in tr.find_all('td')]
        #table_data = [ td.text for td in tr.find_all('td')]  # It's display the tr tag values only and show space , \n and \t

        # How to avoid the space and sepcial characters use strip
        table_data = [ td.text.strip() for td in tr.find_all('td')]
        print((table_data))

        # How to convert CSV file  top ref 3 (import csv modules)

    with open("report.csv", "w" , newline=" ") as csv_file:   # ref 4
        # how to craete heading in csv file using(writer) , 1st create object ,
        #  csv_write is variable and the give input csv_file
        csv_write = csv.writer(csv_file)

        # Now we write the heading using (writerow) , this get one list input , above we already get head files in table_head
        csv_write.writerow(table_head)

        for tr in table_body:
            table_data = [td.text for td in tr.find_all("tr")]
            # print(table_data)

            #  next data writing process , in for loop we already get a data in list format using(table_data = variable) now we write it

            csv_write.writerow(table_data) # Run the this program successfully ,and go to check your file place one new csv file created
                                            # but that file extra one whitespace between heading and values ,so now we remove that
                                             # ref top 4 (with open method add newline function empty string)

#


        # Table_data is variablen = list compersion
# Logic Part

ExtractData(url="https://www.instagram.com/cristiano/?hl=en")  # Get HTML page and  Get content ref 1

    print(response)
# print(dir(BeautifulSoup))

# How to filter the tag ? , We use BS4   ref top 2
'''

# ======X====> How to download the images <====X======


import requests
from bs4 import BeautifulSoup
import csv


def ImageDownloader(url):
    response = requests.get(url=url).content

    # BeautifulSoup  Object (soup is variable)

    soup = BeautifulSoup(response, parse_only="lxml")

    # Extract Img tag

    images = soup.find_all("img", {
        "": ""
    })

    # print(images)   # Show the all id tag images

    # How get attribute in tag   -- ( use for loop to iterated the the tag )

    for img in images:
    # print(img)    # It's show all tag in one by one , here you need only one particular attribute in tag ,
                    #  we use dic format to get the value , eg: print(img["src"])

        # print(img["src"])       # Suppose we made mistake in attribute like (scr)  its through key error,
        # print(img.get["src"])     # This  statement we can fix it  , now we can handle the error
        # Now we find the path of img , from help of above statement, and domain name already in the link
    img_url= url + img.get("src")     # Now we add the input url +  Img path
    # print(img_url)               # Here we get complete url ,then we send again url requrest , get byte code then we convert it img
                                    # So we create one variable (response)
    response = requests.get(url="img_url").content  # Here we pass image url img_url , then add content to get the content of yhe pages

    # print(response)  # Now here reads the images, with bytes codes

    # Now we get img bytes , then we need to write the img ,so we get the img name , so craete onm variable img_name

    img_name =img.get("src")  # here we grt img src
    # print(img_name)  # We print the img src , with full link but we need img name only

    # Now we use (split string method ) with base of (/)
    # print(img_name.split("/"))  # Here the url link split the base of / but need only last img name only

    print(img_name.split("/")[-1])  # use -1  to retuen last value
    # Or  img_name =img.get("src").split("/")[-1]


    # Now we use file handling to get the img

    flie = open(img_name, mode="wb")
    file.write(response=response)  # Here we give 1st byte object , we already get the byte , with help of response

ImageDownloader(url="https://www.instagram.com/cristiano/?hl=en")

# Finally we get the imag