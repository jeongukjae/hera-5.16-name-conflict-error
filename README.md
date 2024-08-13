to reproduce error, run following:

```
$ pip install -r requirements.txt
$ python script_containing_error.py
```

will be raised following error

```
Traceback (most recent call last):
  File "{SOME_PATH}/hera-5.16-name-conflict-error/script_containing_error.py", line 10, in <module>
    Step(name="hello-world", template=hello())
  File "{SOME_PATH}/hera-5.16-name-conflict-error/.venv/lib/python3.12/site-packages/pydantic/v1/main.py", line 349, in __init__
    __pydantic_self__._init_private_attributes()
  File "{SOME_PATH}/hera-5.16-name-conflict-error/.venv/lib/python3.12/site-packages/hera/shared/_global_config.py", line 181, in _init_private_attributes
    self.__hera_init__()
  File "{SOME_PATH}/hera-5.16-name-conflict-error/.venv/lib/python3.12/site-packages/hera/workflows/_context.py", line 30, in __hera_init__
    _context.add_sub_node(self)
  File "{SOME_PATH}/hera-5.16-name-conflict-error/.venv/lib/python3.12/site-packages/hera/workflows/_context.py", line 106, in add_sub_node
    raise TemplateNameConflict(f"Found multiple templates with the same name: {t.name}")
hera.workflows.exceptions.TemplateNameConflict: Found multiple templates with the same name: hello
```

while with hera<5.16, I can get following result

```
$ python script_containing_error.py
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: hello-world-workflow
spec:
  templates:
  - name: main
    steps:
    - - name: hello
        template: hello
    - - name: hello-world
        template: hello
  - name: hello
    script:
      command:
      - python
      image: python:3.8
      source: |-
        import os
        import sys
        sys.path.append(os.getcwd())
        print('hello')
```
