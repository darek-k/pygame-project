import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name='Untitled Pygame Project',
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ['audio', 'clock', 'create', 'display', 'end_windows', 'images',
                                             'inventory', 'items', 'player', 'search', 'sleep', 'file.py'
                                             ]}},
    executables=executables

)
