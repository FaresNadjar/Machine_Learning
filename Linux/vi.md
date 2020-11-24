# vi CHEATSHEET
## Get into and out of vi 

- vi filename : If filename exists, then the first page will be displayed; if not, then an empty file and screen are created.
- vi -r filename : recover filename that was being edited when system crashed.

- :x<Return> #quit vi with saving 
- :q<Return> #quit vi
- :q!<Return> # qui vi even though latest changes have not been saved

## Moving the cursor : 

- 0 #move cursor to start of current line
- $ # ///////////// end   //////////////
- w # //////////// start of next word
- b # ///////////////////// previous word
- :0<Return> # move cursor to first line in file
- :n<Return> # move cursor to line n 
- :$<Return> # move cursor to last line in file

## Screen manipulation

- ^f #move forward one screen
- ^b #move backward one screen
- ^d #move down (forward) one half screen
- ^u #move up (back) one half screen
- ^l #redraws the screen
- ^r #redraws the screen, removing deleted lines

## Manipulating text

- u #Undo last change
- i #insert text before cursor, until <Esc> hit
- I #insert text at beginning of current line, until <Esc> hit
- a #append text after cursor, until <Esc> hit
- A #append text to end of current line, until <Esc> hit
- o #open and put text in a new line below current line, until <Esc> hit
- O #open and put text in a new line above current line, until <Esc> hit

- r #replace single character under cursor (no <Esc> needed)
- R #replace characters, starting with current cursor position, until <Esc> hit
- cw #change the current word with new text,
starting with the character under cursor, until <Esc> hit
- cNw #change N words beginning with character under cursor, until <Esc> hit;
  e.g., c5w changes 5 words
- C #change (replace) the characters in the current line, until <Esc> hit
- cc #change (replace) the entire current line, stopping when <Esc> is hit
- Ncc or cNc #change (replace) the next N lines, starting with the current line, stopping when <Esc> is hit

- x #delete single character under cursor
- Nx #delete N characters, starting with character under cursor
- dw #delete the single word beginning with character under cursor
- dNw #delete N words beginning with character under cursor;
  e.g., d5w deletes 5 words
- D #delete the remainder of the line, starting with current cursor position
- dd #delete entire current line
- Ndd or dNd #delete N lines, beginning with the current line;
  e.g., 5dd deletes 5 lines

- yy # copy (yank, cut) the current line into the buffer
- Nyy or yNy #copy (yank, cut) the next N lines, including the current line, into the buffer
- p #put (paste) the line(s) in the buffer into the text after the current line

## Searching commands : 
- /string #search forward for occurrence of string in text
- ?string #search backward for occurrence of string in text
- n #move to next occurrence of search string
- N #move to next occurrence of search string in opposite direction

## Determining line numbers : 
- :.= #returns line number of current line at bottom of screen
- := #returns the total number of lines at bottom of screen
- ^g #provides the current line number, along with the total number of lines,in the file at the bottom of the screen

## Saving and reading files : 
- :r filename<Return> #read file named filename and insert after current line (the line with cursor)
- :w<Return> #write current contents to file named in original vi call
- :w newfile<Return> #write current contents to a new file named newfile
- :12,35w smallfile<Return> #write the contents of the lines numbered 12 through 35 to a new file named smallfile
- :w! prevfile<Return> #write current contents over a pre-existing file named prevfile 
