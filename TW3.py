# Write a Python program to read the book information from the user and store in a CSV file containing rows in the following format:
# 	bookNo, title, author, price
# Develop a menu-driven program (with functions for each) with the following options:
# 1: Search Book by author
# 2: Search Books below specified price (Raise an exception if price entered is <= 0)
# 3: Search Books where title contains the specified word
# 4: Exit



import csv

def read(n):
    books=[]
    for i in range(n) :
        no,title,author,price=input("Enter number title author and price: ").split(',')
        price=float(price)
        books.append([no,title,author,price])
    with open("Books.csv","w",newline='') as f:
        w=csv.writer(f)
        w.writerows(books)
    print( "Books are: ",books)

def AuthorSearch():
    A=input("Enter author to search: ")
    flag=0
    with open("Books.csv") as f:
        r=csv.reader(f)
        for book in r:
            if A== book[2]:
                flag=1
                print("Book Details are: ",book[0],book[1],book[2],book[3])
        if flag==0:
            print("Book not found ")

def TitleSearch():
    A=input("Enter title to search: ")
    flag=0
    with open("Books.csv") as f:
        r=csv.reader(f)
        for book in r:
            if A== book[1]:
                flag=1
                print("Book Details are: ",book[0],book[1],book[2],book[3])
        if flag==0:
            print("Book not found ")

def PriceSearch():
    try:
        price=float(input("Enter price to search: "))
        if price<=0:
            raise ValueError("Invalid Price")
        else:
            flag=0
            with open("Books.csv") as f:
                r=csv.reader(f)
                for book in r:
                    if price >= float(book[3]):
                        flag=1
                        print("Book Details are: ",book[0],book[1],book[2],book[3])
                if flag==0:
                    print("Book not found ")
    except ValueError as e:
        print("ValueError",e,type(e))




def main():
    n=int(input("Enter the no. of books: "))
    read(n)
    while True:
        opt=int(input("1: Author Search  2:Price Search 3:Title Search 4:Exit \n Enter the option"))
        if opt==1:
            AuthorSearch()
        elif opt==2:
            PriceSearch()
        elif opt==3:
            TitleSearch()
        else:
            break

if __name__=='__main__':
    main()