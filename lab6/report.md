# Overview

Lab 8 applies the understanding of entropy and information theory by challenging us to create a program to first generate a random file filled with random characters from the entire 256 ASCII character set and then calculate the entropy of the file based on the definition of the Shannon Entropy by traversing the file, tallying the frequecy of characters in the array, creating the probability distribution, andthen aggregating the distributions to find the entropy value. 


# Sources

- Arman (because hes awesome)
- Cisco Blog: On Information Entropy
- Python Software Foundation: Entropy

# Methodology for generating random file

My test file generator program receives an input file from the given parameter and begins writing "{}" "into the file 1 byte at a time for as many bytes as the user wants inputted. It then replaces each "{}" with a random character from the ASCII character set to generate the random file with the designated byte size.


# Questions

What sort of file will have higher entropy a normal text file or an encrypted text file?
An encrypted text file will likely have a higher entropy than a normal text file. The encrypted file likely will be converting the original document to random encryption code causing the randomness of the file to increase. With more randomness, naturally entropy will be higher.

UTF-8 another character encoding scheme takes 8 bits per character. What is the maximum achievable entropy for a file using all characters in UTF-8? How about for UTF-16?
The maximum achievable entropy for UTF-8 is 8 because UTF-designates at least 8 bits to represent a character. UTF-16 can achieve an entropy of 16 because it requires at least 2 bytes, or 16 bits to represent a character.  


Did you enjoy this lab? Was it helpful overall in your understanding of networks? 
It's nice knowing the practicality of the lab and understanding why we need to understand entropy. Entropy definitely sounds like a useful practice for compression and network security; however, I may not necessarily see myself applying these sort of practices. Nevertheless, it was helpful for my overall understanding of networks. 



# Extra Credit Completion


[] Implement generate_file in less than 8 lines, always achieving perfect entropy (of 8). 



# Comments and Feedback

As always, a cool lab that is challenging yet fun.
