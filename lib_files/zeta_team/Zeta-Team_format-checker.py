# Zeta-Team_format-checker.py

LIBRARY_NAME = "zeta_fc"

SUPPORTED_FORMATS = {
    "vbr",
    "zta",
}


def check_format(format_name):
    format_name = format_name.lower().strip().lstrip(".")

    if format_name in SUPPORTED_FORMATS:
        return "success"

    return "invalid"
