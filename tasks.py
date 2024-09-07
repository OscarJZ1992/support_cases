from invoke import task

@task
def run(c):
    c.run('uvicorn api.main:app --reload')