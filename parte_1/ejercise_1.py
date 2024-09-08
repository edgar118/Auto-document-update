import re
import math

class Test1():

    """
        The function ListAverage(numbers: list) calculates the average of a list of integers,
        alternating the inclusion of numbers when a 10 is encountered. Each time a 10 appears,
        it toggles whether the following numbers are included in the calculation. It sums only the included numbers and,
        if any are included, returns the truncated average; otherwise, it returns 0.
    """
    def ListAverage(numbers: list):
        total = 0
        count = 0
        include = True
        
        for number in numbers:
            if number == 10:
                include = not include
                continue
            
            if include:
                total += number
                count += 1
        
        
        return int(total / count) if count > 0 else 0


    """
    The function multipliesNumbers(text: str) extracts all numbers from a given text,
    multiplies them, and returns the product. It first uses a regular expression to find all digit sequences in the text,
    converts them to integers, and then calculates their product using math.prod(). If no numbers are found, it returns the message "Numbers not Found".
    """                
    def multipliesNumbers(text: str):
        
        numbers = re.findall(r'\d+', text)

        numbers = list(map(int, numbers))
        return math.prod(numbers) if numbers else 'Numbers not Found'
            
    """
    The function christmas_tree(n: int) generates and prints a Christmas tree pattern.
    It first checks if n is an odd number; if not, it prints an error message.
    Then, it calculates the middle index to determine the tree's top and trunk. For the tree's top,
    it prints lines with an increasing number of stars centered with spaces. For the trunk, it prints a series of lines with a single centered star.
    The height and width of the trunk are based on the middle index.
    """
    def christmas_tree(n: int):
        if n % 2 == 0:
            print("n debe ser un número impar.")
            return
        
        middle = n // 2
        
        # treetop
        for i in range(middle + 1):
            stars = 2 * i + 1
            spaces = (n - stars) // 2 
            print(' ' * spaces + '*' * stars + ' ' * spaces)
        
        # trunk
        trunk_height = middle + 1
        trunk_width = 1
        trunk_spaces = (n - trunk_width) // 2
        
        for _ in range(trunk_height):
            print(' ' * trunk_spaces + '*' * trunk_width + ' ' * trunk_spaces)


