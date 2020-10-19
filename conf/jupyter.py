# import os
# c = get_config()
import os
c = get_config()
# Kernel config
c.IPKernelApp.pylab = 'inline'
# Notebook config
c.NotebookApp.notebook_dir = 'sankalp-notebooks'
c.NotebookApp.allow_origin = u'secure-wildwood-01276.herokuapp.com'
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
# ipython -c "from notebook.auth import passwd; passwd()"
c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$Z/aJC0EIffKvkOyJEn/N1Q$Fo9Z7962Gg7gRhvXn0/3UA'
c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']