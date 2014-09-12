from invoke import task, run


@task
def deploy():
    """
    Pushes to Heroku and runs any ancillary tasks necessary.
    """
    print("Pushing latest changes to Heroku...")
    run("git push heroku master")
    run("heroku run python manage.py syncdb")
    run("heroku run python manage.py migrate")


@task
def test():
    """
    Execute test suite
    """
    run("python manage.py test")
