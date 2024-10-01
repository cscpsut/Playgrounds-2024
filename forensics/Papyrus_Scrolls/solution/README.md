-First, as you explore the disk image, you will find a deleted 7zip file in the Recycle Bin. When you download the zipped file, you’ll notice it is password-protected. You will need to find the password for it somewhere on the disk.

-Second, the password you are looking for can be found in a database file named "scrolls.db" located in the Downloads folder. When you download this file, you’ll see that it is an SQLite file. Use an app or tool to read its contents. Under one of the tables, you will find two passwords. Try both, and you will discover that the second one is correct. This will allow you to access the files in the 7zip archive.
 
-Inside, you will find two tampered images and a PDF protected by a password. You can crack the PDF's password using pdfcrack or another tool. To use pdfcrack, the command is:

```
pdfcrack -w /usr/share/wordlists/rockyou.txt Papyrus_Scrolls.pdf
```

--The first image (scroll1) needs width and height adjustments:

06 -> 07 in width
04 -> 05 in height

A good reference for manipulating image dimensions: https://cyberhacktics.com/hiding-information-by-changing-an-images-height/

--The second image (scroll3) requires you to fix the header from scroll to JFIF. You can identify that it’s a JPEG by using ExifTool or a hex editor. The first 4 bytes resemble the first 4 bytes of a JPEG file header signature. You can find the JPEG file signature here: https://en.wikipedia.org/wiki/List_of_file_signatures
