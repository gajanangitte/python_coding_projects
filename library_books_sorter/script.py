import utils
import sorts

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']: 
    return True
  else:
    False
def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']: 
    return True
  else:
    False
def by_total_length(book_a, book_b):
  return len(book_a['title_lower'])+ len(book_a['author_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
sorts.quicksort(bookshelf_v2, 0 , len(bookshelf_v2)-1, by_total_length )
sorts.quicksort(long_bookshelf, 0 , len(long_bookshelf)-1, by_title_ascending )

# for book in sort_1:
#   print(book['title'])
# for book in sort_2:
#   print(book['title'])

for book in long_bookshelf:
  print(book['title'])

# print(ord("a"))
# print(ord(" "))
# print(ord("A"))