Writeup 7 - Forensics I
======

Name: *Hamid Aina*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Hamid Aina*

## Assignment 7 writeup

### Part 1 (40 pts)
Answer the following questions regarding [this](image) file:

1. What kind of file is it?

It is a JPEG image file.

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.

The photo was taken in Chicago, Illinois at the John Hancock Center.

3. When was this photo taken? Provide a timestamp in your answer.

It was on August 22, 2018 at 11:33 A.M. The timestamp is: 2018:08:22 11:33:24

4. What kind of camera took this photo?

The camera was an Apple iPhone 8 back camera.

5. How high up was this photo taken? Provide an answer in meters.

The photo was taken at 539.5 meters above sea level.

6. Provide any found flags in this file in standard flag format.

You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng} and CMSC389R-{abr@cadabra}


### Part 2 (60 pts)
Reverse engineer [this](binary) binary and find the flag!

Submit a writeup with at least 250 words. Feel free to include screenshots and of course, the flag.

I began by trying to directly run the binary file, but I had no luck and was greeted with the message, “where is your flag?”. From there, I knew I had to use an external file to view the binary. After opening the file in cutter, I tried to run the code a few times but didn’t know how to use the application. So, I scrolled through the source code and found a multi-line comment that said, “tmp/.stego”.

I used binwalk on the file and found that the file was JPEG image data in JFIF standard format. Binwalk also showed that the JPEG was hidden within after one null byte. After removing that byte, I made a copy of the file and was able to open it as a JPEG. I saw the stegosaurus and was initially confused on where to proceed from there. After looking through the slides, I decided to use steghide to view any potentially hidden image data. I looked for documentation on steghide and saw that I could use: steghide extract which then asked me for a password. I thought back to when we were hacking kreuger and began trying passwords along the lines of that. I tried cmsc, password, etc, nothing worked. Finally, I tried stegosaurus and it worked. The password allowed the flag to be extracted into my current directory, and it was there that I saw it: CMSC389R-{dropping_files_is_fun}.


### Scoring

Part 1 is worth 40 points and part 2 is worth 60 points.

### Tips
Revisit the slides on Binaries 1 & 2 and Forensics 1.

Good luck!
