from invoke import task

@task
def test(c):
    c.run("cd tests && pytest --mocha")
