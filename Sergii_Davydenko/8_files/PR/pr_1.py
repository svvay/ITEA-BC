
# Write a version of a palindrome recogniser that accepts a file name from
# the sys.argv, reads each line, and prints the line to the screen if it is a
# palindrome and write results to file like {source_name } /{result}.

print([word for word in (line.strip() for line in ((open('palindrom.txt', 'r'))
      .read().lower().split())) if word == word[::-1]])
