from behave.log_capture import capture
import ctypes


def _load_library(context, library_name):
    if context.tested_library is None:
        context.tested_library = ctypes.CDLL(library_name)


def before_all(context):
    """Perform setup before the first event."""
    context.tested_library = None
    context.load_library = _load_library
