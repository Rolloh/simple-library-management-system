# This programme is a simple library management system
# By: Sonia Rolloh

def inventory():
    
    # This program presents the list of books to the user

    #I have stored the books and their respective details in a dictionary as follows:
    #{<'serial number'>:[<title>, <author>, <no. of said books present>]}    
       
    books = {1: ["Alice in Wonderland", "Lewis Carrol", 14], 2: ["The Wind in the Willows", "Kenneth Graham", 25],
             3: ["The Merchant of Venice", "Shakespeare", 9], 4: ["Utopia", "Sir Thomas Moore", 16],
             5: ["A Tale of Two Cities", "Charles Dickens", 12], 6: ["Divine Comedy", "Dante", 5],
             7: ["The Wild Iris", "Louis Gluck", 10], 8: ["Pilgrim's Progress", "John Bunyan", 23],
             9: ["Ben Hur", "Lewis Wallace", 18], 10: ["Pride and Prejudice", "Jane Austen", 14],
             11: ["Canterbury Tales", "Chaucer", 3], 12: ["The Christmas Pig", "JK Rowling", 7],
             13: ["Diary of a Wimpy Kid", "Jeff Kinney", 28], 14: ["Crime and Punishment", "Dostoevsky", 11],
             15: ["The Great Gatsby", "F. Scott Fitzgerald", 19], 16: ["To Kill a Mockingbird", "Harper Lee", 23]}

    opt = input("\nTo view list of books, press 1.\nTo add new book, press 2.\n\n>->-> ")

    if opt == "1":
        total = 0
        # used a loop to get the values of each key 
        for key in books:
            values = books[key]
            print("There are", values[2], "copies of", values[0], "by", values[1], ".")
            total = total + values[2]
        print("And there are a total of", total, "books in the library.")
        
        main_menu_opt = input("\nWould you like to go back to the main menu(yes / no)? ")
        if main_menu_opt.lower()[0] == "y":
            main()
        else:
            print("\nHave a great day.")

    elif opt == "2":

        new_book = input("\nTitle? ")
        new_book_count = int(input("How many? "))
        new_author = input("Written by? ")
        new_key = int(input("Enter serial number: "))
        new_book = new_book.capitalize()
        new_author = new_author.capitalize()

        books[new_key] = [new_book, new_author, new_book_count]

        inv = input("\nWould you like to view the updated list?(yes / no) ")
        
        if inv.lower()[0] == "y":
            total2 = 0
            for key in books:
                values = books[key]
                print("There are", values[2], "copies of", values[0], "by", values[1], ".")
                total2 = total2 + values[2]
            print("And there are a total of", total2, "books in the library.")
            
        else:
            print("\nHave a great day.")

    else:
        print("\nYou did not enter a valid value!")
        inventory()


def borrow():
    # This program updates the inventory of books to reflect books borrowed

    books = {1: ["Alice in wonderland", "Lewis Carrol", 14], 2: ["The wind in the willows", "Kenneth Graham", 25],
             3: ["The merchant of venice", "Shakespeare", 9], 4: ["Utopia", "Sir Thomas Moore", 16],
             5: ["A tale of two cities", "Charles Dickens", 12], 6: ["Divine comedy", "Dante", 5],
             7: ["The wild iris", "Louis Gluck", 10], 8: ["Pilgrim's progress", "John Bunyan", 23],
             9: ["Ben hur", "Lewis Wallace", 18], 10: ["Pride and prejudice", "Jane Austen", 14],
             11: ["Canterbury tales", "Chaucer", 3], 12: ["The christmas pig", "JK Rowling", 7],
             13: ["Diary of a wimpy kid", "Jeff Kinney", 28], 14: ["Crime and punishment", "Dostoevsky", 11],
             15: ["The great gatsby", "F. Scott Fitzgerald", 19], 16: ["To kill a mockingbird", "Harper Lee", 23]}

    
    book_borrowed = input("\nWhat is the title of the book being borrowed? ")
    num = int(input("How many? "))
    #writer = input("Who wrote the book? ")
    #title = book_borrowed.capitalize()

    new_list = []
    for key in books:        
        values = books[key]
        new_list.append(values[0])
           
    #print(new_list)
    if book_borrowed.capitalize() in new_list:
        for key in books:
            #if book_borrowed.capitalize() == values[0]:
            print(key,values)
    else:
        print("Sorry, this book is not available.")

    #updated_inv =
      

    inv = input("\nWould you like to view the updated list of books(yes\no)? ")
    if inv.lower()[0] == "y":
        print(updated_inv)
    else:
        print("Have a great day!")

def re_turn():

    # This program updates the inventory of books to reflect books returned
    books = {1: ["Alice in wonderland", "Lewis Carrol", 14], 2: ["The wind in the willows", "Kenneth Graham", 25],
             3: ["The merchant of venice", "Shakespeare", 9], 4: ["Utopia", "Sir Thomas Moore", 16],
             5: ["A tale of two cities", "Charles Dickens", 12], 6: ["Divine comedy", "Dante", 5],
             7: ["The wild iris", "Louis Gluck", 10], 8: ["Pilgrim's progress", "John Bunyan", 23],
             9: ["Ben hur", "Lewis Wallace", 18], 10: ["Pride and prejudice", "Jane Austen", 14],
             11: ["Canterbury tales", "Chaucer", 3], 12: ["The christmas pig", "JK Rowling", 7],
             13: ["Diary of a wimpy kid", "Jeff Kinney", 28], 14: ["Crime and punishment", "Dostoevsky", 11],
             15: ["The great gatsby", "F. Scott Fitzgerald", 19], 16: ["To kill a mockingbird", "Harper Lee", 23]}

    return_title = input("What is the title of the book you want to return? ")
    return_count = int(input("How many? "))
    #return_author =

    #return_opt

def return2():

    return_multiple = input("Do you have any more books to return(yes / no)? ")
    if return_multiple.lower()[0] == "y":
        re_turn()
    else:
        print("Have a great day.")    


def stat():
    # This program presents the current status of a particular book

    book_title = input("\nWhat is the title of the book? ")

    books = {1: ["Alice in wonderland", "Lewis Carrol", 14], 2: ["The wind in the willows", "Kenneth Graham", 25],
             3: ["The merchant of venice", "Shakespeare", 9], 4: ["Utopia", "Sir Thomas Moore", 16],
             5: ["A tale of two cities", "Charles Dickens", 12], 6: ["Divine comedy", "Dante", 5],
             7: ["The wild iris", "Louis Gluck", 10], 8: ["Pilgrim's progress", "John Bunyan", 23],
             9: ["Ben hur", "Lewis Wallace", 18], 10: ["Pride and prejudice", "Jane Austen", 14],
             11: ["Canterbury tales", "Chaucer", 3], 12: ["The christmas pig", "JK Rowling", 7],
             13: ["Diary of a wimpy kid", "Jeff Kinney", 28], 14: ["Crime and punishment", "Dostoevsky", 11],
             15: ["The great gatsby", "F. Scott Fitzgerald", 19], 16: ["To kill a mockingbird", "Harper Lee", 23]}

    list_of_books = []

    for key in books:
        values = books[key]
        list_of_books.append(values[0])

    if book_title.capitalize() in list_of_books:
        print("\nAvailable")
    else:
        print("\nUnavailable")

    stat_opt = input("\nWould you like to go back to the main menu(yes / no)? ")
    if stat_opt.lower()[0] == "y":
        main()
    else:
        print("\nHave a great day.")


def main():
    opt = input("\nTo borrow a book, press 1.\nTo return a book, press 2.\nTo check inventory, press 3.\nTo check status of a book, press 4.\n\n>->->-> ")

    if opt == "1":
        borrow()
    elif opt == "2":
        re_turn()
        return2()
    elif opt == "3":
        inventory()
    elif opt == "4":
        stat()
    else:
        print("Invalid input!")


main()
