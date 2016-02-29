# -*-coding: UTF-8-*-
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')  # 允许程序以双击运行

py2exe_options = {
    "dll_excludes": ["MSVCP90.dll","w9xpopen.exe"],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    "bundle_files": 1,
}
setup(
    name='boois-guid',
    version='1.0',
    console=[{'script': 'boois-guid.py',"icon_resources": [(1, "logo.ico")]}],
    zipfile=None,
    options={'py2exe': py2exe_options}
)
