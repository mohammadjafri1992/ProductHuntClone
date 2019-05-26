# Product Hunt Clone

#### NOTE: This is only a project showcase website with no intended commercial use. If you decide to clone the project or use any part of this project/repository, USE IT AT YOUR OWN RISK. The owner of this project cannot be held liable for any damage/loss this code may cause to an already existing system / or any new system developed using this codebase. Thank you.

### Project Overview
This project website is a clone of a popular website www.ProductHunt.com . The project website (this repo) contains two Django apps. Accounts and Products. Although the original website contains many more apps and a lot more feature, I only recreated these two major apps because these are essential for the website to function properly.

All other apps can be created as clones/copies of the Products app as that is the most versatile app.

#### Database
The first thing I did before I started working on anything was to replace the original SQLite databse with PostgreSQL becasue in production environment, SQLite simply doesn't cut it. 

I created a databse called "producthuntdb" in pgAdmin4 and ran it in the background. This database was then added in the settings.py instead of sqlite3.

settings.py was also 
