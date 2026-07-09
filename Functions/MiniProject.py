#Sort the Colors
'''Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence 
after sorting them alphabetically.'''
def sort_colors(color):
  colors=color.split("-")
  colors.sort()
  result='-'.join(colors)  
  return result
  
color = input("Enter the colors separated by hyphen: ")
print(sort_colors(color))