def read_and_sum_numbers(filename):
  total_sum = 0
  try:
    # Open the file in read mode
    with open(filename, 'r') as file:
      # Read the file line by line
      for line in file:
        # Remove leading/trailing whitespaces
        line = line.strip()
        # Try converting the line to a number
        try:
          # Add the number to the sum if conversion is successful
          total_sum += float(line)
          # Display the number
          print(line)
        except ValueError:
          # Handle lines that are not numbers
          print(f"Line '{line}' is not a valid number and will be skipped.")
  except FileNotFoundError:
    # Handle the case where the file is not found
    print(f"Error: File '{filename}' not found.")
    return None

  # Return the total sum after processing all lines
  return total_sum

# Example usage
filename = "numbers.txt"
total_sum = read_and_sum_numbers(filename)

if total_sum is not None:
  print(f"The sum of the numbers in '{filename}' is: {total_sum}")
