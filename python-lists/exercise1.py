colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']
# print(colors)
# print(type(colors))

# sundry = ['John', 3.14, 7, False]
# print(sundry)
# print(type(sundry))

# print(f'0-based indexing into the list...second item: {colors[12]}')

# print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
# print(colors[2:5])
# print(type(colors[2:5]))

# print('\nPrint a slice, starting at index 0 to index 3:')
# print(colors[:3])

# print('\nPrint a slice, starting a index 4 to the end of the list:')
# print(colors[4:])

# print('\nPrint a slice, from the 4th from the end (but not the last item):')
# print(colors[-4:-1])

# colors.reverse()
# print(colors)

# colors.sort()
# print(colors)

# print(colors)
# color = colors.pop(0)
# print('popped', color)
# print(colors)

print(colors)

# colors.append('black')
# colors.append('white')

# colors.append('yellow')
# colors.append('orange')

# print(colors)

# colors.remove('whatever')

new_colors = ['lime', 'gray']
colors.extend(new_colors)
print(colors)