from packageA.logic import logic_fn
# import packageA.logic as logic # <-- this form also works! change the call in logic_from_util to: logic.logic_fn()

def util_fn():
    print(f"Hi from {__name__}!")

def logic_from_util():
    logic_fn()

