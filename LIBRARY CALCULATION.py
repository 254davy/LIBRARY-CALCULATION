def calculate_fine(book_id, due_date, return_date):
  """Calculates the library fine based on the due date and return date of a book.

  Args:
      book_id: The ID of the book (string).
      due_date: The due date of the book in YYYY-MM-DD format (string).
      return_date: The return date of the book in YYYY-MM-DD format (string).

  Returns:
      The library fine amount (float) or 0 if the book is returned on time.
  """

  from datetime import datetime

  # Convert dates to datetime objects for comparison
  due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
  return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")

  # Calculate the difference in days between due date and return date
  days_overdue = (return_date_obj - due_date_obj).days

  # Check if the book is returned on time or overdue
  if days_overdue <= 0:
    return 0  # No fine if returned on time or before

  # Apply the fine rates based on the number of days overdue
  fine = 0
  if days_overdue <= 7:
    fine = days_overdue * 20  # Ksh 20 per day up to 7 days
  elif days_overdue <= 14:
    fine = 140 + (days_overdue - 7) * 50  # Ksh 140 fixed + Ksh 50 per day for days 8-14
  else:
    fine = 340 + (days_overdue - 14) * 100  # Ksh 340 fixed + Ksh 100 per day for 15 days or more

  return fine

# Example usage
book_id = "LIB-1234"
due_date = "2023-12-15"
return_date = "2024-01-10"  # Example overdue return

fine_amount = calculate_fine(book_id, due_date, return_date)

if fine_amount > 0:
  print(f"Book ID: {book_id}")
  print(f"Fine amount: Ksh {fine_amount:.2f}")
else:
  print(f"Book ID: {book_id}")
  print("Book returned on time. No fine.")
