# Photo Backup Software

It is possible that we want to show our friends photos from social networks, but social networks may not be available for some reason. Let's protect ourselves from this.
This program allows you to back up photos from the VK user's profile (avatars) to the Yandex. Disk cloud storage.

## Functions:

•	Receiving photos from the VK user's profile (avatars);

•	Conservation the specified number of photos (5 by default) of the maximum size (width/height in pixels) on Yandex. Disk in the folder created during the process;

•	For the name of photos usage number of likes. If the number of likes is the same, then the upload date is added to the file name;

•	Track the program's progress using the progress bar;

•	Conservation information about photos in a json file with results.

All dependencies are specified in the file requiremеnts.txt.

Pay attention! To work with the program, you need to get:

•	VK token;

•	Token with Yandex.Disk Polygon.

## Input data

The user enters:

•	VK user id;

•	Token with Yandex.Disk Polygon.

## Output data:

1.	Json file with information about the file:

1
2
3
4
    [{
    "file_name": "34.jpg",
    "size": "z"
    }]
2.	Modified Yandex.Disk where photos were added.
