def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()

    words = count_words(file_contents)
    characters = count_char(file_contents)
    sorted_chars = sorted(characters.items(), key=lambda item: item[1], reverse=True)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{words} words found in the document')
    print(' ')
    for tuple in sorted_chars:
      print(f"The '{tuple[0]}' character was found {tuple[1]} times")
    print('--- End report ---')


def count_words(text: str):
  return len(text.split())

def count_char(text: str):
  characters = {}
  book_text = text.lower()
  for char in book_text:
    if not char.isalpha():
      continue
    if char in characters:
      characters[char] = characters[char] + 1
    else:
      characters[char] = 1
  return characters

main()