import sys
from stats import txt_from_book
from stats import num_of_char
from stats import sorted_list

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  text = get_book_text(book_path)
  num_words = txt_from_book(text)
  dictionary = num_of_char(text)
  list_sorted = sorted_list(dictionary)
  return print_report(book_path, num_words, list_sorted)


def print_report(book_path, num_words, list_sorted):
  print(
    "============ BOOKBOT ============"
  )
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in list_sorted:
    if not item["char"].isalpha():
      continue
    print(f"{item['char']}: {item["num"]}")
  print("============= END ===============")

main()
