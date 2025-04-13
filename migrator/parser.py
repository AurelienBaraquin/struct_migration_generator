import re

def extract_structs(content):
    structs = []

    # Match 'typedef struct {...} Name;' or 'struct Name { ... };'
    pattern = re.compile(
        r"(typedef\s+)?struct\s*(\w*)\s*{([^}]*)}\s*(\w+)?\s*;",
        re.DOTALL
    )

    for match in pattern.finditer(content):
        _, name1, body, name2 = match.groups()
        name = name2 or name1
        if not name:
            continue
        fields = extract_fields(body)
        structs.append({'name': name.strip(), 'fields': fields})

    return structs

def extract_fields(body):
    lines = body.strip().split(";")
    fields = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        match = re.match(r"(.+?)\s+(\w+)$", line)
        if match:
            field_type, field_name = match.groups()
            fields.append({'type': field_type.strip(), 'name': field_name.strip()})
    return fields

