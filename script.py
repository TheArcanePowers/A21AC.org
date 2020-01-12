import glob
import csv

output = []

for flag_file in glob.glob("*.png"):
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
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dui turpis, cursus eget orci amet aliquam congue semper. Etiam eget ultrices risus nec tempor elit.\n\
</section>')

