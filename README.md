# WindowsMEODecrypt
A python script that can be used to obtain the MD5 hash value from encrypted .meo containers for bruteforcing.

Original Blog Post: https://theincidentalchewtoy.wordpress.com/2021/11/09/meo-file-encryption-software/

*“MEO is easy file encryption software for Mac or Windows”.*

MEO is made by NCH software and enables a user to encrypt files, folders or emails, including 
making self-extracting versions, making them more portable.

The software makes use of two different encryption algorithms, ‘blowfish’ and ‘DES’. This script and the data below 
relates to data being encrypted using the blowfish algorithm.

## Data Structure

Not to delve too deeply into the entire files structure, the below screen shot shows the first ‘chunk’ 
of hex of a ‘.meo’ file.
<p align="center">
<img src="https://user-images.githubusercontent.com/97304946/151439379-bd01e5de-c10d-4f27-8c3c-b425eab82829.png" width="600" height="150">
<img src="https://user-images.githubusercontent.com/97304946/151439464-59c35ec6-93ef-4e4d-9290-c5c1fff1fd65.png" width="400" height="150">
</p>

The key length for blowfish encryption can be longer, however, the 32 byte length version has only 
been seen during testing.

In order for the key to be generated, the following process occurs:
<p align="center">
<img src="https://user-images.githubusercontent.com/97304946/151439671-eca10fa0-d99a-49ee-b0bf-5803ca6d82cd.png" width="400" height="300">
</p>
In order to revered this process, a script has been written which takes the ‘.meo’ file as an input, 
checks that it has the correct header, pulls the key and carries out the reverse of the above process 
to provide the user with the MD5 hash.

Using hashcat, it is then possible to bruteforce the password using the following:
<p align="center">
hashcat64.exe -a 0 -m 0 a58d4efd860b63bfcaa73474916a4567 "C:\pw list.txt
  </p>
