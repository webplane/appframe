from appframe import verbose

AFTER_FEATURE = "test2"


def activate(*args, **kwargs):
    print("F1")
    verbose(1, "Verbose running F1")
