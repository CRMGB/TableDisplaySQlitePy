TABLE DISPLAY sqlite3 AND PyQt5

Python GUI application to display the data stored in a sqlite file.

Install sqlite3 for Ubuntu
    - sudo apt update
    - sudo apt-cache search sqlite
    - sudo apt install sqlite3
    - sqlite3 --version

Install python3-pyqt5 for Ubuntu
    - sudo apt update
    - sudo apt install python3-pyqt5

TODO:
    Allow the user to page through the `safe_hashes` table of the hashes.sqlite database. Pagination should be done using the LIMIT OFFSET SQL syntax and display 10 records at a time. Bonus if you can allow the user to type
    in the page number to view.

    Text input for a hash and have an option to search the `safe_hashes` table for any matching hash. A confirmation should be shown if that hash
    exists. Bonus if you can allow the user to enter multiple hashes to search at once.
