c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.password = ''
c.NotebookApp.token = ''
c.InteractiveShellApp.exec_lines = [
    'import sys; sys.path.append("/home/user/.local")',
    'import os; os.environ["HTTP_PROXY"] = "http://figgis-s.hpc.virginia.edu:8080"',
    'import os; os.environ["HTTPS_PROXY"] = "http://figgis-s.hpc.virginia.edu:8080"',
    'import os; os.environ["http_proxy"] = "http://figgis-s.hpc.virginia.edu:8080"',
    'import os; os.environ["https_proxy"] = "http://figgis-s.hpc.virginia.edu:8080"',
]
