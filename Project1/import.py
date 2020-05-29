import os, csv

#importing the packages from the sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#To maintain a connecction through heroku url from the database
engine=create_engine(os.getenv("DATABASE_URL"))

#scopped session that confirms different user interact with db are kept seprate.
db=scoped_session(sessionmaker(bind=engine))

#data in which books are kept
file=open("books.csv")

#Python have direcct function to read from the file
reader=csv.reader(file)

for isbn, title, author, year in reader:
    db.execute("INSERT into books(isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
              {"isbn": isbn, "title": title, "author": author, "year": year})
    print(f"Added book {title} to database.")

    db.commit()

if __name__== "__main__":
    main()
