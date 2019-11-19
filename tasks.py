
from invoke import task

@task
def test(c):
    c.run("pytest -q Cesta/tests/test_cesta.py")

