# Zeta_Team_lib_zeta.py
# Library name: lib_zeta-team_zeta

LIB_NAME = "lib_zeta-team_zeta"
FORCED = True

LIBRARIES = {
    "lib_zeta_variables": "lib_files/zeta_team/Zeta-Team_variables.py"
}


def load():
    if not FORCED:
        raise RuntimeError("lib_zeta-team_zeta must be forced to load.")

    return True
