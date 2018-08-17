#!/bin/bash
cd data

# Bureau of Industry and Security Denied Parties List
wget https://www.bis.doc.gov/dpl/dpl.txt

# U.S. Department of the Treasury Specially Designated Nationals And Blocked Persons List (SDN)
wget https://www.treasury.gov/ofac/downloads/sdnlist.txt
