from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'animalsounds',         # How you named your package folder (TSIClient)
  packages = ['animalsounds'],   # Chose the same as "name"
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  long_description=long_description,
  long_description_content_type='text/markdown',  # This is important!
  author = 'Vivek Raja P S',                   # Type in your name
  author_email = 'vivekraja98@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Vivek0712/azure-devops-pypackage',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/RaaLabs/TSIClient/archive/v_0.7.tar.gz',    # If you create releases through Github, then this is important
  keywords = ['Azure', 'DevOps', 'Python'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
)
