Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Hamid Aina*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Hamid Aina*

## Assignment 2 writeup

### Part 1 (45 pts)

1. His real name is Fred Krueger.

2. Twitter: @kruegster1990. I discovered his twitter through a Google search of his username. Email: kruegster@tutanota.com, this was found from his about page on the cornerstoneairlines.co website. Reddit: u/kruegster1990, I found this from searching his name followed by Reddit. He runs his own business called Cornerstone Airlines, the website is cornerstoneairlines.co. Additionally, he is located in Silver Spring, Maryland and was born in 1990.

3. The IP address of the web server is 142.93.118.186. I found this by using nslookup on the domain name: cornerstoneairlines.co from the command line. Equivalently, I could have used dnsdumpster on the domain name cornerstoneairlines.co and I would have achieved the same result.

4. I found a hidden /secret directory by typing in: 142.93.118.186/robots.txt. From there, I typed: 142.93.118.186/secret/ and did "inspect" to find the flag: Congrats! Your first flag is: CMSC389R-{fly_th3_sk1es_w1th_u5}.

5. I also found: 142.93.117.193 from the website that was under construction. A simple nslookup allowed me to find the main ip, after which I found 142.93.117.193.

6. The associated server (Digital Ocean) is located in New York. I found this by doing: whois 142.93.118.186 on the command line.

7. The server is running Apache 2.4.18 on Ubuntu. I discovered this by doing whois on the ip.

8. Yes, I found the flag: CMSC389R-{h1dden_fl4g_in_s0urce} by using "inspect" on the main page of cornerstoneairlines.co. I also found the flag: CMSC389R-{dns-txt-rec0rd-ftw} from dnsdumpster.com after searching cornerstoneairlines.co. Finally I found the flag: CMSC389R-{y0u_found_th3_g1t_repo} by attempting to bruteforce all subdirectories on the ip: 142.93.117.193 and accessing the .git repo.

### Part 2 (55 pts)

I began by using the utility npm to find all available ports. After doing so, I realized that the port I found was of no use. From there I proceeded to use Inteltechniques to find all accounts associated with Fred. Once I found the IP address I needed, I used nmap to find all of the relevant ports, 1337 being one of them.

After a call to nc, I determined that 1337 allowed me to access the airlines admin portal. I easily found his username, kruegster, on the website. So I just needed to find the password by using rockyou.txt along with a python program to iterate through the possible combinations to find the password, pokemon.

The flag inside the flight records directory was: CMSC389R -{c0rn3rstone-air-27670}. The instagram page took the longest for me to find. Eventually, I used the picture of the plane ticket on his instagram to identify the pertinent txt file.
