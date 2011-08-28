from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-inboxinfluence",
      version="0.1.0",
      py_modules=["inboxinfluence"],
      description="Libraries for interacting with the Influence Explorer Text API",
      author="Dan Drinkard <dan.drinkard@gmail.com>",
      author_email = "dan.drinkard@gmail.com",
      license="BSD",
      url="http://github.com/dandrinkard/python-inboxinfluence",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )

