# migrator.py
import os
import sys
from parser import extract_structs
from comparer import compare_structs
from generator import generate_versioned_header, generate_migration
from pathlib import Path
import re

VERSIONS_DIR = "include/versions"
MIGRATIONS_DIR = "src/migrations"
HEADERS_DIR = "include/test"
ALIASES_DIR = "include/aliases"
TEMPLATE_PATH = "migrator/templates/migration.cpp.tpl"

def get_latest_version(struct_name):
    version = 0
    for file in os.listdir(VERSIONS_DIR):
        if file.startswith(struct_name + "V") and file.endswith(".hpp"):
            try:
                v = int(file[len(struct_name)+1:-4])  # Extract number from NameV1.hpp
                if v > version:
                    version = v
            except:
                continue
    return version

def normalize_struct_name(name):
    """Supprime un éventuel suffixe Vx du nom de struct (ex: UserV3 → User)"""
    return re.sub(r'V[0-9]+$', '', name)

def load_struct_version(struct_name, version):
    path = os.path.join(VERSIONS_DIR, f"{struct_name}V{version}.hpp")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        content = f.read()
        structs = extract_structs(content)
        for s in structs:
            if normalize_struct_name(s['name']) == normalize_struct_name(struct_name):
                return s
    return None

def struct_with_version(base_name, version):
    """Ajoute Vx au nom seulement s'il n'existe pas déjà."""
    if re.search(r'V[0-9]+$', base_name):
        return base_name
    return f"{base_name}V{version}"

import re
import os

def generate_alias_header(struct_name, output_dir, versions_dir):
    versioned_files = []
    for file in os.listdir(versions_dir):
        if file.startswith(struct_name + "V") and file.endswith(".hpp"):
            match = re.match(rf"{re.escape(struct_name)}V(\d+)\.hpp", file)
            if match:
                versioned_files.append((int(match.group(1)), file))

    if not versioned_files:
        return

    versioned_files.sort()  # par ordre croissant
    latest_version, latest_file = versioned_files[-1]
    latest_struct = f"{struct_name}V{latest_version}"

    file_path = os.path.join(output_dir, f"{struct_name}.hpp")

    with open(file_path, "w") as f:
        f.write("#pragma once\n")
        for _, file in versioned_files:
            f.write(f'#include "{file}"\n')
        f.write(f"\nusing {struct_name} = {latest_struct};\n")

def main():
    Path(VERSIONS_DIR).mkdir(exist_ok=True)
    Path(MIGRATIONS_DIR).mkdir(exist_ok=True)
    Path(ALIASES_DIR).mkdir(parents=True, exist_ok=True)

    for file in os.listdir(HEADERS_DIR):
        if not file.endswith(".hpp"):
            continue

        header_path = os.path.join(HEADERS_DIR, file)
        with open(header_path) as f:
            current_structs = extract_structs(f.read())

        for struct in current_structs:
            struct_name = struct['name']
            latest_version = get_latest_version(struct_name)

            if latest_version == 0:
                # Première version détectée
                print(f"[NEW] {struct_name} → V1")
                generate_versioned_header(struct, 1, VERSIONS_DIR, header_path)
                generate_alias_header(struct_name, ALIASES_DIR, VERSIONS_DIR)
            else:
                # Charger la dernière version enregistrée
                previous = load_struct_version(struct_name, latest_version)
                if not previous:
                    print(f"[WARN] Impossible de charger {struct_name}V{latest_version}")
                    continue

                if compare_structs(previous, struct):
                    new_version = latest_version + 1
                    print(f"[UPDATE] {struct_name} V{latest_version} → V{new_version}")
                    generate_versioned_header(struct, new_version, VERSIONS_DIR, header_path)
                    generate_migration(previous, struct, latest_version, new_version, MIGRATIONS_DIR, TEMPLATE_PATH)
                    generate_alias_header(struct_name, ALIASES_DIR, VERSIONS_DIR)
                else:
                    print(f"[UNCHANGED] {struct_name} V{latest_version} (pas de modification)")

if __name__ == "__main__":
    main()
