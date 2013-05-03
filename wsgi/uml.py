import subprocess, os, sys
siteroot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
htdocs = os.path.join(siteroot, 'htdocs')
imageDirectory = os.path.join(htdocs, 'images')
platumlPath = '/opt/plantuml/plantuml.jar'
plantuml = ['java', '-jar', platumlPath]
fileExtension = 'svg'

def application(environ, start_response):
    sourceUrl = environ['REDIRECT_URL'].lstrip('/\\')
    source = os.path.abspath(os.path.join(htdocs, sourceUrl))
    if source.startswith(htdocs):
        image = os.path.join(imageDirectory, sourceUrl[:-3]+fileExtension)
        imageUrl = '/'+os.path.relpath(image, htdocs)
        if (not os.path.exists(image)) or (os.path.getmtime(source) > os.path.getmtime(image)):
            cmd = plantuml + ['-t'+fileExtension, '-o', os.path.dirname(image), source]
            subprocess.call(cmd)
    # send first header and status
    if start_response is not None:
        status = '302 Found'
        headers = [('Location', imageUrl)]
        start_response(status, headers)

    yield ''




if __name__ == '__main__':
    #~ for r in application({'REDIRECT_URL': '/000-start.md'}, None):
    for r in application({'REDIRECT_URL': '/test.uml'}, None):
        print(r)
