from setuptools import setup

setup(
    name="SteampyTest",
    options = {
        'build_apps': {
            #'include_patterns': [
                #'**/*.png',
                #'**/*.jpg',
                #'**/*.egg',
                #'**/*.obj',
                #'**/*.txt',
                #'**/*.gltf',
                #'**/*.xml',
                #'Resources/Textures/testgrid.png',
                #'../Resources/Textures/testgrid.png',
                #'../Resources/Textures/*.png',
                #'../Resources/Models/*.egg',
            #],
            'gui_apps': {
                'SteampyTest': './panda.py',
            },
            'platforms': ['manylinux2014_x86_64', # this is most recent
            #'manylinux1_x86_64' # this is older than 2010?
            #'manylinux2010_x86_64', 'macosx_10_9_x86_64', 'win_amd64'],
            ],
            
            #'log_filename': '$USER_APPDATA/Demogame/output.log',
            'log_filename': '~/Demogameoutput.log',
            'log_append': False,
            'use_optimized_wheels': False, # this was advised in the troubleshooting section.
            
            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],

        },
    }
)
