# Define the rows with emojis
row1 = ["😀", "😂", "😎"]
row2 = ["🍎", "🍌", "🍉"]
row3 = ["🥕", "🥦", "🍅"]

# Create a map consisting of the three rows
map = [row1, row2, row3]

# Print the rows
print(f"{row1}\n{row2}\n{row3}")


# Print a specific emoji by specifying its row and column index
# For example, to print the second emoji in the first row:
print(map[0][1])  # Output: 😂

# To print the third emoji in the second row:
print(map[1][2])  # Output: 🍉

# To print the first emoji in the third row:
print(map[2][0])  # Output: 🥕
