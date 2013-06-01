===========
xctemplateutils
===========

xctemplateutils provides a list of useful command line programs that
helps ease the pain of manually dealing with messy .xctemplate files.

How to use it
=========

* Install
```
    pip install xctemplateutils
```

* Generate <key> and <dict> for <Definitions> element
```
        generate_xctemplate.py -d <folder_name>
```
  For example, suppose you have MagicalRecord copied into
  a subfolder MagicalRecord/ of your .xctemplate folder @
  MyXCTemplate/MagicalRecord. You can:
```
        cd MyXCTemplate; generate_xctemplate.py -d MagicalRecord
```

* Generate <string> for <Nodes> element
```
        generate_xctemplate.py -n <folder_name>
```

Once you verify the output, you can simply copy-and-paste the output
into the respective <Definitions> and <Nodes> elements in your
.xctemplate file to customize them.
