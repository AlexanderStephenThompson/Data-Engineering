import os

# Absolute path: 'C:\\Folder_Name\\File_Name.mp3'

"""
Relative Paths
. - This directory (Starting point)
.. - Parent folder (Go up one)

\Folder_Name (Going into a folder.)
\File_Name.extension (Selecting a file)
"""

File_Path = os.path.dirname('C:\\Folder_Name\\File_Name.mp3')
File_Selection = os.path.basename('C:\\Folder_Name\\File_Name.mp3')
