#!/home/drew/virtualEnv/FlaskWebApp/bin/ python2.7

"""
    run
    ~~~

    This module is used to start the web app
    Change host IP address to host on local area network eg( '192.168.1.*') if desired
    Change Flask config file to run in Development mode or Production mode,
    choose either debug_config or production_config
"""
import app

app.create_app("config.debug_config").run(host='192.168.1.114', port=5000)
