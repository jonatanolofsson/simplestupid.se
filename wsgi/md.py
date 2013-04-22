#-*- coding: utf-8 -*-
import os, imp, re
siteroot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
htdocs = os.path.join(siteroot, 'htdocs')
tplname = 'template.tpl.py'
markdownVersion = 1

if markdownVersion == 1:
    import markdown
    markdownExtensions = []
else:
    import markdown2
    markdownExtensions = ['extra', 'codehilite', 'headerid', 'meta', 'sane_lists']

def getLink(to):
    return "/" + os.path.relpath(to, htdocs)

def validLink(lnk):
    return isMarkdown(lnk) or (os.path.isdir(lnk) and any(map(validLink, os.listdir(x))))

def isMarkdown(filename):
    return (not os.path.isdir(filename) and filename.endswith('.md'))

def readStructure(directory):
    mdfiles = []
    directories = []
    for root, dirnames, filenames in os.walk(directory):
      for filename in filter(isMarkdown, filenames):
          mdfiles.append(os.path.join(root, filename))
    mdfiles.sort()
    return mdfiles

def getLinks(directory):
    mdfiles = list(readStructure(directory))
    links = []
    for f in map(lambda x: os.path.join(directory, x), filter(lambda x: (os.path.isdir(os.path.join(directory, x)) or isMarkdown(x)), sorted(os.listdir(directory)))):
        for m in mdfiles:
            if m.startswith(f):
                links.append((getName(f), getLink(m), m))
                break
    return links

def getName(filename):
    return re.match('^([0-9]*).?(.*?)(.md)?$', os.path.basename(filename)).group(2).capitalize()

def getMenu(mdfile, startDirectory, endDirectory, level = 0):
    output = ""
    maxlevel = level
    if endDirectory != startDirectory:
        (output, maxlevel) = getMenu(mdfile, startDirectory, os.path.dirname(endDirectory), level+1)

    output += '<ol class="menu menulevel{level}">\n'.format(level=maxlevel-level) \
    + "\n".join(['<li class="{cssclass}"><a href="{link}">{name}</a></li>'.format(
        link = link,
        name = name,
        cssclass = 'active' if mdfile.startswith(filename) else 'normal'
    ) for name,link,filename in getLinks(endDirectory)]) \
    + '\n</ol>'


    if level == 0:
        return output
    else:
        return (output, maxlevel)


def application(environ, start_response):
    output = ""
    mdfile = os.path.join(htdocs, environ['REDIRECT_URL'].lstrip('/'))
    tpldir = os.path.dirname(mdfile)
    while not os.path.exists(os.path.join(tpldir, tplname)) and not tpldir == siteroot:
        tpldir = os.path.dirname(tpldir)

    tpl = os.path.join(tpldir, tplname)
    template = {}
    if os.path.exists(tpl):
        template = imp.load_source('template', tpl)

    if "header" in dir(template):
        output += template.header(environ, {
            'title': " / ".join(map(getName, os.path.relpath(mdfile, htdocs)[0:-3].split('/'))),
            'menu': getMenu(mdfile, htdocs, os.path.dirname(mdfile))
        })

    with open(mdfile) as f:
        if markdownVersion == 1:
            output +=  markdown.markdown(f.read(), extensions=markdownExtensions)
        else:
            output +=  markdown2.markdown(f.read(), extra=markdownExtensions)


    if "footer" in dir(template):
        output += template.footer(environ)

    # send first header and status
    if start_response is not None:
        status = '200 OK'
        headers = [('Content-type', 'text/html'),
            ('Content-Length', str(len(output)))]
        start_response(status, headers)

    # wsgi apps should return and iterable, the following is acceptable too :
    # return [output]
    yield output

if __name__ == '__main__':
    #~ for r in application({'REDIRECT_URL': '/000-start.md'}, None):
    for r in application({'REDIRECT_URL': '/01.helicopter/00.helicopter.md'}, None):
        print(r)
