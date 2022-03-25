import re

def h_repl(m):
    text = m.group('text')
    if m.group('hash') == '#':
        return f'<h1>{text}</h1>'
    elif m.group('hash') == '##':
        return f'<h2>{text}</h2>'
    elif m.group('hash') == '###':
        return f'<h3>{text}</h3>'

def p_repl(m):
    text = m.group('text')
    return f'<p>{text}</p>'

def li_repl(m):
    text = m.group('text')
    if m.group(1) == '*':
        return f'<li>{text}</li>'

def ul_repl(m):
    text = m.group('text')
    return f'<ul>{text}</ul>'



h_pattern = re.compile(r'^(?P<hash>#{1,3})\s(?P<text>.*)', re.M)
p_pattern = re.compile(r'^(?P<text>[^*#\n-]+)', re.M)
li_pattern = re.compile(r'^(\*|-)\s(?P<text>.*)', re.M)
ul_pattern = re.compile(r'(?P<text><li>.*</li>)', re.DOTALL)

patterns = [h_pattern, p_pattern, ul_pattern, li_pattern]

def to_html(patterns, repl, content):
    content = content.group('text')
    for pattern in patterns:
        content = re.sub(pattern, repl, content)


content = '''
# HTML

HTML is a markup language that can be used to define the structure of a web page. HTML elements include

* headings
* paragraphs
* lists
* links
* and more!

The most recent major version of HTML is HTML5.
'''


# print(re.findall(h, content))
# print(re.sub(h, h_repl, content))
# content = re.sub(li, li_repl, content)
# print(re.sub(ul, ul_repl, content))
# print(re.findall(ul, content))

print(__name__)
