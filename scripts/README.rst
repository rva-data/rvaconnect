========
Scripts!
========

The scripts here are a collection of development and build related scripts for
running tests and linting code.

They are divided up into two sections, 'automatic' and 'manual' based on how
they are intended to be used. Note that they can be used in either way
depending on the circumstance.

Automated
=========

curly-spacing.sh
----------------

Lints Django templates (*not* pre-compiled Jade) for weirdly formatted Django
template tag delimitters.

django-url.sh
-------------

Lints Django templates for new style `url` tags.

pre-commit
----------

This is a Git hook used to run `flake8` to check for badly formatted Python
code and to perform basic static analysis on Python code, subject to the
constraints specified in the tox.ini file.

To install it, you must edit the script first to include the path to the flake8
executable::

    /Users/me/.virtualenvs/myenv/bin/flake8

Using the path to the installed executable in your virtualenv is a good idea
for two reasons:

1. It ensures that you're using the version of flake8 (and components)
   specified for the project in case of multiple installs
2. It ensures that the Git hook is executed properly whether you have your
   virtualenv activated or not

The second reason is especially important if you or any teammates use a
separate Git GUI.

After you've edited the file, copy this file so its path is
`.git/hooks/pre-commit` with respect to the root of the project repository.

Manual
======

check-links.sh
--------------

This is a convenience wrapper around `pylinkvalidate.py` and is used to crawl
different environments in search of broken links. Usage::

    ./check-links staging
    ./check-links production

It configures the domains for the script, additional options, and the HTTP
basic auth credentials for staging.