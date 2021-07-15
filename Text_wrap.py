import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    # Print each line.
    res = []
    for element in word_list:
        res.append(element)
    return '\n'.join(res)


string, max_width = input(), int(input())
print(wrap(string, max_width))

