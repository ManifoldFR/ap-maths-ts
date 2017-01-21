set /p fichier= Enter name of notebook you want to cook: 
jupyter nbconvert --to python %fichier%
jupyter nbconvert --to html %fichier%
jupyter nbconvert --to slides %fichier%
jupyter nbconvert --to pdf %fichier%