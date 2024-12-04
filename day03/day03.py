import re

def process_text(text):
    # Regular expression to find mul(x,y) where x and y are numbers
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches of the pattern
    matches = re.findall(pattern, text)
    
    # Initialize a sum accumulator
    total = 0
    
    # Iterate over matches and compute their products
    for match in matches:
        x, y = map(int, match)  # Convert extracted strings to integers
        total += x * y  # Add the product to the total
    
    return total
content = ""
with open('input.txt', 'r') as file:
    content = file.read()
# Example usage
input_text = "Here are some examples: mul(3,4), mul(2,5), and mul(10,2)."
result = process_text(content)
print(f"The sum of all products is: {result}")