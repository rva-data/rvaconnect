from invoke import task, run


@task
def deploy():
    """
    Pushes to Heroku and runs any ancillary tasks necessary.
    """
    run("git push heroku master")
    run("heroku run python manage.py syncdb")
    run("heroku run python manage.py migrate")