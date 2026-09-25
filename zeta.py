import re
import sys


variables = {}
imported = set()
loaded = False


def expand(text):
    def replace(match):
        name = match.group(1)

        if name not in imported:
            raise Exception(f"Variable '{name}' was not imported")

        return variables[name]

    return re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", replace, text)


def run(filename):
    global loaded

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    terminated = False

    for line_number, line in enumerate(lines, 1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line == "$ load_zeta":
            loaded = True

        elif not loaded:
            raise Exception(f"Line {line_number}: Zeta is not loaded")

        elif line == "$ import_lib_zeta_variables":
            pass

        elif line.startswith("$ import_variable:"):
            name = line.split(":", 1)[1].strip()
            imported.add(name)
            variables[name] = ""

        elif line.startswith("$print <") and line.endswith(">"):
            text = line[8:-1]
            print(expand(text))

        elif line == "$ terminate_code":
            terminated = True
            break

        else:
            match = re.fullmatch(
                r"\{([A-Za-z_][A-Za-z0-9_]*)\}\s*=\s*(.*)",
                line
            )

            if match:
                name, value = match.groups()

                if name not in imported:
                    raise Exception(
                        f"Line {line_number}: Variable '{name}' was not imported"
                    )

                variables[name] = expand(value)
            else:
                raise Exception(
                    f"Line {line_number}: Unknown syntax"
                )

    if not terminated:
        raise Exception("$ terminate_code is required")


if len(sys.argv) != 2:
    print("Usage: python zeta.py <file.zta>")
    sys.exit(1)

try:
    run(sys.argv[1])
except Exception as error:
    print(f"Zeta error: {error}")
