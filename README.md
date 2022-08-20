# Time to Cross Reference Endangered and Threatened Species

The goal of this project is to cross reference a list of species against two governmental databases in order to identify specimens from threatened and endangered species from the list of specimens for the Cal Poly Humboldt Museum of Vertibrate Zoology collecting permit. 

We reference the 2022 State of California Natural Resources Agency Special Animals List referred to as the CNDDB. https://nrm.dfg.ca.gov/FileHandler.ashx?DocumentID=109406&inline

We also reference another list which we don't yet have access to.

## Step 1
Pulling data from CNDDB which means dealing with PDFs which generally suck. We used [tabula](https://tabula.technology/) to convert the tables in CNDDB_Special_Animals_List.pdf into a csv file. This file was then processed using conver_cnddb_data.py to remove newline characters, remove header rows, and convert to json.

We verified that this likely pulled all the data because the file lists 924 taxa and our resulting json contains 924 records.

## Step 2 
Pulling the species list from CA_SCP_Hawkins_VM06-2019-06-2022.pdf which is hell on earth because it is a scanned document. Hopefully we can use the OCR in Adobe Acrobat DC to conver this to a usable file or get access to the original digital copy.

## Step 3
Locating an excel spreadsheet with more species information

## Step 6
Just sorta mashing them all together

## Contributors
- Jacob Oakman
- Ezra Alberts