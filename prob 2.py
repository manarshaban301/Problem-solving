#manar shaban moubarak

records = input("Enter borrowed books in the format 'Book Title - Days Borrowed', separated by commas:")

borrow_data = {}
for record in records.split(","):
    book, days = record.split(" - ")
    days = int(days)
    if book in borrow_data:
        borrow_data[book] += days  
    else:
        borrow_data[book] = days

most_borrowed_book = max(borrow_data, key=borrow_data.get)
least_borrowed_book = min(borrow_data, key=borrow_data.get)

average_days = sum(borrow_data.values()) / len(borrow_data)

unique_books = set(borrow_data.keys())

sorted_books = sorted(borrow_data.items(), key=lambda x: x[1], reverse=True)

print(f"Most borrowed book: '{most_borrowed_book}' with {borrow_data[most_borrowed_book]} days.")
print(f"Least borrowed book: '{least_borrowed_book}' with {borrow_data[least_borrowed_book]} days.")
print(f"Average borrowing days: {average_days:}")
print(f"Unique book titles: {unique_books}")
print("Books sorted by borrowing duration (descending):")
for book, days in sorted_books:
    print(f" {book} : {days} days")




