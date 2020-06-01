##############################################################################
# Copyright 2017 SoundHound, Incorporated.  All rights reserved.
##############################################################################
from distutils.core import setup, Extension

module1 = Extension("okhound",
                    sources = ["pyOkHound.cpp"],
                    libraries = ["PhraseSpotter"],
                    library_dirs = ["."])

setup(name = "OkHound",
      version = "1.0",
      description = "'Ok Hound' phrase spotter.",
      ext_modules = [module1])