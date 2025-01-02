start_symbol = 'S'
productions = {
    'S': [('NP', 'VP')],
    'NP': [('John',), ('Mary',)],
    'VP': [('eats',), ('sleeps',)]
}
input_str = "John eats"
tokens = input_str.split()
stack = [start_symbol]
while stack:
    current_symbol = stack.pop()
    if current_symbol in productions:
        current_productions = productions[current_symbol]
        for production in current_productions:
            if production[0] == tokens[0]:
                stack.extend(reversed(production[1:]))
                tokens.pop(0)
                break
    elif current_symbol == tokens[0]:
        tokens.pop(0)
    else:
        print("Invalid input string")
        break
else:
    if not tokens:
        print("Input string parsed successfully")
    else:
        print("Invalid input string")
