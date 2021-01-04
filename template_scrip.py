import glob
import csv
import json
import shutil
output = []
countryname = []
'''
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')'''

with open('europe.txt') as json_file:
    data = json.load(json_file)
    for countryname in data:
        for row in csv.reader(open('data.csv', "rb"), delimiter=","):
            #if current rows 2nd value is equal to input, print that row
            if countryname == row[0]:
                safename = ''.join(e for e in row[1] if e.isalnum())
                final_filename = (row[1] + ".html").lower().replace(" ","-")
                shutil.copy("template.html", final_filename)
                print ("Created: " + final_filename)



'''for countryname in glob.glob("*.png"):
    #print(flag_file.lower())
    flag_name = flag_file[:-4]
    for row in csv.reader(open('data.csv', "rb"), delimiter=","):
        #print row
        #if current rows 2nd value is equal to input, print that row
        if flag_name.upper() == row[0]:
            final_flag = row[0].lower() + ".png"
            #print final_flag
            final_CountryName = row[1]
            #print final_CountryName
            print ('\
<section>\n\
    <span class="image fit"><img src="flags/' + final_flag + '"></img></span>\n\
    <h3>' + final_CountryName + '</h3>\n\
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dui turpis, cursus eget orci amet aliquam congue semper. Etiam eget ultrices risus nec tempor elit.</p>\n\
</section>')
'''
