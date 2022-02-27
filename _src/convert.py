#coding=utf-8
'''A quick and dirty script to generate my blog site.'''
import os, sys
import shutil
import markdown

def join_post_content(title, date, content):
    CHARSET = "utf-8"
    header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="static/style.css" />
    <title>{title} | 黄杰的记事本</title>
</head>
<body>
<h1>{title}</h1>
<p style="text-align: right;">黄杰, {date}<br />root[a]linuxsand.info</p>"""
    body_end = """</body>\r\n</html>"""
    
    return header.format(title=title, date=date) + \
           markdown.markdown(
               content,
                extensions=[
                    "markdown.extensions.tables",
                    "markdown.extensions.toc"
                    ]
               ) + \
           body_end

           
           
def get_meta_from_src(filename):
    thisfile = open(filename, "r", encoding="utf-8")
    line1 = thisfile.readline().rstrip()
    line2 = thisfile.readline().rstrip()
    content = thisfile.read().strip()
    return line1, line2, content


    
def get_title_from_post(html_name):
    if html_name.endswith('2013-06-18-robotics.html'):
        #return '机器人学导论阅读笔记'
        return None
    with open(html_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        title = lines[9][4:-6]#.decode('utf8').encode('gbk', 'ignore') # test in cmd.exe
        return title
        
        
        
def gen_index():
    header = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Weblog for software development and industrial automation applications.">
    <link rel="stylesheet" href="static/style.css" />
    <script type="text/javascript" src="static/index.js"></script>
    <title>Weblog | Huang Jie</title>
    <style type="text/css">
    .left {text-align: left;}
    .right {text-align: right;}
    .center {text-align: center;}
    </style>
</head>
<body>
<h1>索引 | 黄杰的记事本</h1>
<div class="right">
[
<a href="http://linuxsand.info" target="_blank">about</a>
]
</div>
<ul>'''
    footer = '''</ul>
<script type="text/javascript">
    var postsCount = main();
    document.write( 
        "<div style='text-align: right;'>" + postsCount.toString() + 
        " posts hosted on Github Pages</div>"
    );
</script>
</body>
</html>'''
    line_tpl = '''<li class="blog_title"><a href="{0}">{1}</a></li>'''
    
    posts = []
    PATH_PREFIX = '../_posts'
    for post in os.listdir(PATH_PREFIX):
        if not post.endswith('.html'): continue
        date = post[:10]
        url = post[11:]
        title = get_title_from_post(os.path.join(PATH_PREFIX, post))
        if title is None: continue
        posts.append( (url, title, date) )
    posts.sort(key=lambda x: x[2], reverse=True) # newest date on the top
    
    lines = []
    for info in posts:
        lines.append( line_tpl.format( info[0], info[1]) )
        
    with open ('../index.html', 'w', encoding='utf-8') as index:
        index.write(header + '\n'.join(lines) + footer)
    print('index generated.\n')
    
    
    
def gen_new_posts():
    md_files = []
    for _file in os.listdir("."):
        if not _file.endswith(".txt"): continue
        print("...converting " + _file)
        title, date, content = get_meta_from_src(_file)
        html_content = join_post_content(title, date, content)
        with open("../_posts/" + date + "-" + _file.replace(".txt", ".html"), "w", encoding='utf-8') as f:
            f.write(html_content)
        md_files.append(_file)
    print("\nnew posts generated.\n")
        
        
        
def gen_sitemap():            
    pass
    
    
    
if __name__ == "__main__":
    print('---Start---\n')
    gen_new_posts()
    gen_sitemap()
    gen_index()
    print("\n\n--End--")
    # import time
    # time.sleep(3)
    
    
