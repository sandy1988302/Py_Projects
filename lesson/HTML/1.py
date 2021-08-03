from pyh import *
f = "D:\\Py_Projects\\lesson\\HTML\\a.html"
page = PyH('My wonderful PyH page')
page << h1('My big title', cl='center')
page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
mydiv2 = page << div(id='myDiv2')
mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
page << div(id='myDiv3')
page.myDiv3.attributes['cl'] = 'myCSSclass3'
page.myDiv3 << p('Another paragraph')
html = page.render()
with open(f, "w", encoding="utf-8") as hotwords:
    hotwords.write(html)
