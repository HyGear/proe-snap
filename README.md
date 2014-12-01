Overview
=========
This script allows the user to create snapshots of a working directory by calling the script with a mapkey (macro) in Pro/Engineer. When the script is launched, it finds the latest version (highest numbered extension) of each file and copies them to a subdirectory (using the current timestamp as the directory name) in the Pro/E working directory. The numbered extension is also reset back to ".1" so that the snapshots can be used in a revision control program such as Subversion.

Usage
====
There are 2 ways to use this script:

1. Copy the proe-snap.py file to your working directory, open a cmd window and type the following:

  python proe-snap.py

2. Create a mapkey in Pro/Engineer and enter the following under the "OS Script" option:

  C:\path\to\python\python.exe C:\path\to\script\proe-snap.py

Revision Control
===============
As stated above, the script will rename the numbered extension (version) of the file back to a ".1". This makes it possible to check into a revision control program since the complete filename will stay the same. If the numbered extension changes, the revision control program will see each new numbered extension as a new file and revisions will not be tracked.
