# peoplecheck

Takes an input file, and breaks each line into words. If each of the words of a line are in a record of the Bureau of Industry and Security Denied Parties List (DPL)
or the U.S. Department of the Treasury Specially Designated Nationals And Blocked Persons List (SDN), this tool will tell you.

Words much match exactly, case insensitive. Punctuation is removed (except for the @ symbol to ensure email addresses are checked).

The recommended approach is to create a text file with one name per line (business or person) or one email address per line and then run this tool on it.

This approach intentionally eschews edit-distance algorithms such as Levenshtein distance in order to reduce the already high rate of false positives inherent in using these lists. This tool is a cue for further investigation only and should not itself be used to allow or disallow interactions with persons or businesses.

This tool was a simple hack designed to get a straight-forward task done and does not use any pre-computation or indexing. It works and is complete. There are no plans for future improvement. 

## Usage
    ./simple-check.py test.txt
