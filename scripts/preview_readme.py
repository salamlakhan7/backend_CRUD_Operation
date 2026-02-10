"""
Generate an HTML preview from backend_CRUD_Operation/README.md and serve it at http://127.0.0.1:8000/
"""
import os
import sys
import subprocess

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# README.md lives inside the backend_CRUD_Operation folder (PROJECT_DIR)
README_MD = os.path.join(PROJECT_DIR, 'README.md')
OUTPUT_HTML = os.path.join(PROJECT_DIR, 'README_preview.html')
PORT = 8000

# Ensure markdown package
try:
    import markdown
except Exception:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown'])
    import importlib
    importlib.reload(sys.modules.get('markdown', None))
    import markdown

with open(README_MD, 'r', encoding='utf-8') as f:
    md = f.read()

html_body = markdown.markdown(md, extensions=['extra', 'toc'])
full_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>README Preview</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; padding: 24px; max-width: 980px; margin: auto; }}
img {{ max-width: 100%; height: auto; display: block; margin: 12px 0; }}
.preview-center {{ text-align: center; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(full_html)

# Serve project root so images and files are reachable
os.chdir(PROJECT_DIR)

from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ('127.0.0.1', PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serving at http://{server_address[0]}:{server_address[1]}/")
print(f"Open /backend_CRUD_Operation/README_preview.html to view the preview")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Shutting down server')
    httpd.server_close()
