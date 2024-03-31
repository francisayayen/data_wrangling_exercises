# An example of reading data from a fixed-width file with Python.
# The source file for this example comes from NOAA and can be accessed here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
# The metadata for the file can be found here:
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

# import the `csv` library, to create our output file
import csv

filename = "C:\\Users\\f_ayx\\OneDrive\\Documents\\data_wrangling_exercises\\chapter_4_examples\\standalone_files\\ghcnd-stations"

# reading from a basic text file doesn't require any special libraries
# so we'll just open the file in read format ("r") as usual
source_file = open(filename+".txt", "r")

# the built-in "readlines()" method does just what you'd think:
# it reads in a text file and converts it to a list of lines
stations_list = source_file.readlines()

# create an output file for our transformed data
output_file = open(filename+".csv","w")

# use the `csv` library's "writer" recipe to easily write rows of data
# to `output_file`, instead of reading data *from* it
output_writer = csv.writer(output_file)

# create the header list
headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG",
 "HCNCRN_FLAG","WMO_ID"]

# write our headers to the output file
output_writer.writerow(headers)

# loop through each line of our file (multiple "sheets" are not possible)
for line in stations_list:
    # create an empty list, to which we'll append each set of characters that
    # makes up a given "column" of data
    new_row = []
    # ID: positions 1-11
    new_row.append(line[0:11])
    # LATITUDE: positions 13-20
    new_row.append(line[12:20])
    # LONGITUDE: positions 22-30
    new_row.append(line[21:30])
    # ELEVATION: positions 32-37
    new_row.append(line[31:37])
    # STATE: positions 39-40
    new_row.append(line[38:40])
    # NAME: positions 42-71
    new_row.append(line[41:71])
    # GSN_FLAG: positions 73-75
    new_row.append(line[72:75])
    # HCNCRN_FLAG: positions 77-79
    new_row.append(line[76:79])
    # WMO_ID: positions 81-85
    new_row.append(line[80:85])

    # now all that's left is to use the
    # `writerow` function to write new_row to our output file
    output_writer.writerow(new_row)

# officially close the `.csv` file we just wrote all that data to
output_file.close()
