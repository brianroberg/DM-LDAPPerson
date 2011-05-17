from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dm.ldapperson',
      version=version,
      description="Library for accessing data about people in LDAP",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Brian Roberg',
      author_email='robergb@dm.org',
      url='https://github.com/brianroberg/DM-LDAPPerson',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
