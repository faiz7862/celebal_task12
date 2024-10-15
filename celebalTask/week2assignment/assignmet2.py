def count_words_in_file(filename):

  try:
    # Open the file in read mode
    with open(filename, 'r') as file:
      # Read the entire content of the file
      content = file.read()
      # Split the content into words using whitespace as delimiters
      words = content.split()
      # Return the number of words (length of the list)
      return len(words)
  except FileNotFoundError:
    # Handle the case where the file is not found
    print(f"Error: File '{filename}' not found.")
    return 0

# Example usage
filename = "celebalTask\week2assignment\fileexample.txt"
word_count = count_words_in_file(filename)

if word_count > 0:
  print(f"The file '{filename}' contains {word_count} words.")
