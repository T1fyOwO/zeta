# Zeta-Team_variables.py

LIBRARY_NAME = "lib_zeta_variables"

def is_variable(value):
    return value.startswith("{") and value.endswith("}")
