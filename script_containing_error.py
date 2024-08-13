from hera.workflows import Steps, script, Workflow, Step


@script()
def hello():
    print("hello")

with Workflow(name="hello-world-workflow") as wt:
    with Steps(name="main"):
        h = hello()
        Step(name="hello-world", template=h)

print(wt.to_yaml())
