from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'gui'

executables = [
    Executable('main.py', base=base)
]

setup(name='samoosa',
      version = '1',
      description = 'A tool that will help you to know the summary of the youtube video without watching the fullvideo. Just paste the link of the video you want to summarise in this tool, then you will see the magic.',
      options = {'build_exe': build_options},
      executables = executables)
