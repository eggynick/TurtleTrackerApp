#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Nicholas Fairbairn (nbf9@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable point to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the filename
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file object
file_object.close()

date_dict = {}
location_dict = {}

#Extract one data line into a variable
for lineString in line_list:

    #Check to see if the lineString is a data line
    if  lineString.startswith('#') or lineString.startswith('u')==True:
        continue
    else:
        #Split lineString into a list of items
        lineData = lineString.split()
        
        #Assign variables to items in the lineData list
        record_id = lineData[0]
        obs_date = lineData[2]
        obs_lc = lineData[4]
        obs_lat = lineData[6]
        obs_lon = lineData[7]
        
        #Print information to the user
        print(f'Record {record_id} indicates Sara was seen and {obs_lat}N, {obs_lon}W  on {obs_date}. ')
        
        #add items to dictionaries
        date_dict[record_id]=obs_date
        location_dict[record_id]=(obs_lat,obs_lon)
        
       
       
       
       
       