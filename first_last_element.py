"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some Content', '</h1>]

remove_first_and_last(html)

html_2 = ['<h1>', 'Some content', 'more', '</h1>']

remove_first_and_last(html2)
=> ['some content', 'more']
"""

def remove_first_and_last(list_to_clean):
    _ , *content, _ = list_to_clean
    return content

html = ['<h1>', 'Some content', '</h1>']
html_two = ['<h1>', 'Some content', 'more content', '</h1>']

# def remove_first_and_last(list_to_clean):
#     return list_to_clean[1:-1]

print(remove_first_and_last(html))
print(remove_first_and_last(html_two))
