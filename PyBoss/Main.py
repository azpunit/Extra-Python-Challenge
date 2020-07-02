# The following code allowed us to locate and create files. 
import csv
import os

# The following code allowed us to locate the employee_data.csv excel file. 
csvpath = os.path.join("/Users/azpunit/Desktop/Extra-Python-Challenge/PyBoss/employee_data.csv")

# The follwing code allowed us to store all the lists that are going to be appended to store the values that 
# are going to be populated in our new excel file. 
First_Name = []
Second_Name = []
Name = []
Employee = []
Date = []
New_Date = []
SSN = []
New_SSN = []
States = []
States_Initials = []

# This following code allowed us to create a dictionary to replace the lists of states by a list of the states initials. 
Rubric = {}
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# The following code was designed to append all the lists that we are going to zip in order to populate our columns in terminal 
# and then in our new excel file. 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
       Name = str(row[1]).split(" ")
       First_Name.append(str(Name[0]))
       Second_Name.append(str(Name[1]))
       Employee.append(int(row[0]))
       Date = str(row[2]).split("/")
       Date = format(str(Date[0]) + "-" + str(Date[1]) + "-" + str(Date[2]))
       New_Date.append(Date) 
       SSN = str(row[3]).split("-")
       SSN = format(f"***-**-{SSN[2]}")
       New_SSN.append(SSN)
       States = (f"{us_state_abbrev[row[4]]}")
       States_Initials.append(States)
       Zip_Object = zip(Employee, First_Name, Second_Name, New_Date, New_SSN, States_Initials)
       for Employee_i, First_Name_i, Second_Name_i, New_Date_i, New_SSN_i, States_Initials_i in Zip_Object:
           print(f"{Employee_i}, {First_Name_i}, {Second_Name_i}, {New_Date_i}, {New_SSN_i}, {States_Initials_i}")

# The following code allowed us to create the employee_customized.csv excel file. 
output_file = os.path.join("/Users/azpunit/Desktop/Extra-Python-Challenge/PyBoss/empleyee_customized.csv")

# The following code allowed us to zip all the list that we thereafter populated on our new excel file. 
cleaned_csv = zip(Employee, First_Name, Second_Name, New_Date, New_SSN, States_Initials)

# The following code allowed us to populate all the lists that we previously created and zipped together. 
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First_Name", "Second_Name", "DOB", "SSN", "State"])
    writer.writerows(cleaned_csv)
