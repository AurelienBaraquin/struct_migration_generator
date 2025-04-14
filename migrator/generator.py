# generator.py
import os
from jinja2 import Template
from pathlib import Path
import re

def default_value(type_str):
    if "int" in type_str:
        return "0"
    elif "float" in type_str or "double" in type_str:
        return "0.0"
    elif "string" in type_str:
        return '""'
    elif "*" in type_str:
        return "nullptr"
    return "{}"

def extract_includes_before_struct(filepath):
    includes = []
    with open(filepath) as f:
        for line in f:
            if "struct" in line:
                break
            if line.strip().startswith("#include"):
                includes.append(line.strip())
    return includes

def generate_versioned_header(struct, version, output_dir, original_path):
    struct_name = struct_with_version(struct['name'], version)
    file_path = os.path.join(output_dir, f"{struct_name}.hpp")

    with open(file_path, "w") as f:
        f.write("#pragma once\n")
        f.write(f"#include \"{original_path}\"\n")
        f.write(f"struct {struct_name} {{\n")
        for field in struct['fields']:
            f.write(f"    {field['type']} {field['name']};\n")
        f.write("};\n")

def normalize_struct_name(name):
    return re.sub(r'V[0-9]+$', '', name)

def struct_with_version(base_name, version):
    """Ajoute Vx au nom seulement s'il n'existe pas déjà."""
    if re.search(r'V[0-9]+$', base_name):
        return base_name  # déjà suffixé
    return f"{base_name}V{version}"

def generate_migration(from_struct, to_struct, from_version, to_version, output_dir, template_path):
    from_name = struct_with_version(from_struct['name'], from_version)
    to_name = struct_with_version(to_struct['name'], to_version)

    with open(template_path) as f:
        template = Template(f.read())

    cpp_code = template.render(
        from_header=f"{from_name}.hpp",
        to_header=f"{to_name}.hpp",
        from_struct=from_name,
        to_struct=to_name,
        to_fields=to_struct['fields'],
        from_field_names={field['name'] for field in from_struct['fields']},
        default_value=default_value
    )

    filename = f"{to_struct['name']}V{from_version}_to_V{to_version}.cpp"
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(cpp_code)
