from invoke import task

@task
def test(c):
    with c.cd('tests/'):
        c.run("pytest")


