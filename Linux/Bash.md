# Commandes Principales :
## Shell :
- df : to see the current amount of free space on your disk drives
- free : to display the amount of free memory
- exit : to exit the terminal
- echo : Display a line of text
- echo This is a Line : print This is a Line
- echo * : print all the names inside the current folder
- echo \\$((\\$((5**2)) * 3)) : allow to use the shell as a calculator
- echo Description {1..15} : print Description 1 ... Description 15
- clear : Clear the screen
- history : Display the contents of the history list
- id : Display user identity
- chmod : Change a file's mode
- umask : Set the default file permissions
- su : Run a shell as another user
- sudo : Execute a command as another user
- chown : Change a file's owner
- chgrp : Change a file's group ownership
- passwd : Change a user's password

## Navigation
- pwd : name the current directory
- cd Name : go to the directory Name
- cd .. : to go to the parent directory
- cd ~ : to go to the root directory
- ls : list the contents of the current directory. option -l for long format

## Exploring System
- file filename : print a brief description of the file's contents
- less filename : to view the content of a text file

## Manipulating Files
### cp command :
- cp : Copy files and directories
- cp file1 file2 : Copy file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created.
- cp -i file1 file2 Same as above, except that if file2 exists, the user is prompted before it is overwritten.
- cp file1 file2 dir1 : Copy file1 and file2 into directory dir1. dir1 must already exist.
- cp dir1/* dir2 : Using a wildcard, all the files in dir1 are copied into dir2. dir2 must already exist.
- cp -r dir1 dir2 : Copy the contents of directory dir1 to directory dir2. If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1. If directory dir2 does exist, then directory dir1 (and its contents) will be copied into dir2.

### mv command : 
- mv : Move/rename files and directories
- mv file1 file2 Move file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created. In either case, file1 ceases to exist.
- mv -i file1 file2 Same as above, except that if file2 exists, the user is prompted before it is overwritten.
- mv file1 file2 dir1 Move file1 and file2 into directory dir1. dir1 must already exist.
- mv dir1 dir2 If directory dir2 does not exist, create directory dir2 and move the contents of directory dir1 into dir2 and delete directory dir1. If directory dir2 does exist, move directory dir1 (and its contents) into directory dir2.

### create directory : 
- mkdir : Create directories

### remove directory : 
- rm : Remove files and directories
- rm file1 Delete file1 silently.
- rm -i file1 Same as above, except that the user is prompted for confirmation before the deletion is performed.
- rm -r file1 dir1 Delete file1 and dir1 and its contents.
- rm -rf file1 dir1 Same as above, except that if either file1 or dir1 do not exist, rm will continue silently.

### create link
- ln : Create hard and symbolic links
- ln -s ../fun dir1/fun-sym : Create a shortcut of the file fun named fun-sym in dir1 

## Working with commands :
- type command : Display A Command's Type
- which command : Display An Executable's Location
- help command : Get help for shell builtins
- command \\-\\-help : Display Usage Information 
- apropos : Display a list of appropriate commands
- info : Display a command's info entry
- whatis : Display a very brief description of a command

### man method : 
- man program : Display a command's manual page
- man section search_term

#### Section Contents
- 1 User commands
- 2 Programming interfaces kernel system calls
- 3 Programming interfaces to the C library
- 4 Special files such as device nodes and drivers
- 5 File formats
- 6 Games and amusements such as screen savers
- 7 Miscellaneous
- 8 System administration commands

## Redirection :
### cat command :
- cat : Concatenate files
- cat file.txt : shows the content of file.txt
- cat movie.mpeg.0* > movie.mpeg : join the split files named movie.mpeg.0* into movie.mpeg

### sort & uniq
- sort : Sort lines of text
- uniq : Report or omit repeated lines
- ls /bin /usr/bin | sort | uniq | less : show a brief description of non repeated and sorted files taken from the list in /bin and /usr/bin.

### print commands :
- grep : Print lines matching a pattern
- wc file.txt : Print nb of lines, words, and bytes for file.txt 
- head -n 5 : Output the 5 first part of a file
- tail -n 5 : Output the 5 last part of a file
- tee : Read from standard input stdin and write to standard output stdout

# WildCards : 
- \\* : Matches any characters
- ? : Matches any single character
- [characters] : Matches any character that is a member of the set characters
- [!characters] : Matches any character that is not a member of the set characters
- [[:class:]] : Matches any character that is a member of the specified class

# Commonly Used Character Classes :
- [:alnum:] : Matches any alphanumeric character
- [:alpha:] : Matches any alphabetic character
- [:digit:] : Matches any numeral
- [:lower:] : Matches any lowercase letter
- [:upper:] : Matches any uppercase letter

## Examples : 
- \\* : All files
- g* : Any file beginning with “g”
- b*.txt : Any file beginning with “b” followed by any characters and ending with “.txt”
- Data??? : Any file beginning with “Data” followed by exactly three characters
- [abc]* : Any file beginning with either an “a”, a “b”, or a “c”
- BACKUP.[0-9][0-9][0-9] : Any file beginning with “BACKUP.” followed by exactly three numerals
- [[:upper:]]* : Any file beginning with an uppercase letter
- [![:digit:]]* : Any file not beginning with a numeral
- *[[:lower:]123] : Any file ending with a lowercase letter or the numerals “1”, “2”, or “3”
