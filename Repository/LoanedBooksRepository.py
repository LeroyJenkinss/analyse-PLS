# LoanedBooksRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllLoanedBooks.json
# Zie BooksRepository.py voor verdere toelichting
from shutil import copyfile
import datetime as dt
from pathlib import Path

def createBackup():
    backUpPath = "../Data/Backup/{}/AllLoanedBooks.json".format(dt.date.today())
    if not Path(backUpPath).exists():
        Path().mkdir(parents=True, exist_ok=True)
        copyfile('../Data/AllLoanedBooks.json', backUpPath)

def recoverBackup(date):
    backUpPath ='../Data/Backup/{}/AllLoanedBooks.json'.format(date)
    copyfile(backUpPath, '../Data/AllLoanedBooks.json')
