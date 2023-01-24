searched_book = input()
current_book = input()
is_found = False
checked_books_counter = 0
while current_book != "No More Books":
    if current_book == searched_book:
        is_found = True
        break
    current_book = input()
    checked_books_counter +=1
if is_found:
    print(f"You checked {checked_books_counter} books and found it.")
else:
    print("The book you search is not here!")
    print (f"You checked {checked_books_counter} books.")
