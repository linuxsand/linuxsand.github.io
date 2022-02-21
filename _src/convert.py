#coding=utf-8
'''Qucik and dirty script to generate my blog site.'''
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
    <meta name="description" content="Notes about Industrial Automation, also some thoughts recorded here.">
    <link rel="stylesheet" href="static/style.css" />
    <title>Notes | Huang Jie</title>
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
<a href="http://www.linuxsand.info" target="_blank">about</a>
|
<a href="http://www.linuxsand.info/work_tools.html" target="_blank">tools</a>
]
</div>
<ul>'''
    footer = '''</ul>

<script type="text/javascript">
let blacklist = [
    "fcc83_tutorial.html",
    "my-2016.html",
    "my-2015.html",
    "my-2014.html",
    "xinjing-and-seal-cutting.html",
    "merida-warrior-500.html",
    "hangout-2.html",
    "fengtang-poems.html",
    "hangout-1.html",
    "insensitive-people.html",
    "hometown-1.html",
    "best-xxx-in-2012.html",
    "offer.html",
    "manual-focus.html",
    "root-your-android-device.html",
    "trifles-2.html",
    "get-animal-farm.html",
    "trifles-1.html",
    "went-to-nanjing-again.html",
    "xinjing.html",
    "long-message-and-short-message.html",
    "using-bat-file-to-save-time-for-edit-apk-file.html",
    "root-huawei-android-phones.html",
    "the-life-of-others.html",
    "time-to-have-a-haircut-again.html"
];

let liArray = document.getElementsByClassName("blog_title");
let len = liArray.length;
let postsCount = len;
for (let index = 0; index < len; index++) {
    let parts = liArray[index].firstChild.href.split('/');
    let link = parts[parts.length-1];
    if (blacklist.includes(link)) {
        liArray[index].style.display = 'none';
        //console.log('hit one');
        postsCount--;
    }
}

document.write( 
"<div style='text-align: right;'>" + postsCount.toString() + 
" posts hosted on Github Pages</div>");

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
    import time
    time.sleep(3)
    
    
