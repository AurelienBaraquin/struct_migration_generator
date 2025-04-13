import json
import os

VERSIONS_JSON = "versions.json"
OUTPUT_CPP = "src/BinaryReaderRegistry.cpp"
OUTPUT_HPP = "include/BinaryReaderRegistry.hpp"

def generate_registry():
    with open(VERSIONS_JSON) as f:
        versions = json.load(f)

    # On fusionne tous les types de toutes les versions
    type_versions = {}
    for version_map in versions.values():
        for logical_name, real_type in version_map.items():
            type_versions[real_type] = logical_name  # on garde l'info logique si besoin plus tard

    # Génération du .hpp
    os.makedirs("include", exist_ok=True)
    with open(OUTPUT_HPP, "w") as hpp:
        hpp.write("""#pragma once
#include <map>
#include <functional>
#include <any>
#include <istream>

using BinaryReader = std::function<std::any(std::istream&)>;
extern std::map<std::string, BinaryReader> binaryReaders;
""")

    # Génération du .cpp
    os.makedirs("src", exist_ok=True)
    with open(OUTPUT_CPP, "w") as cpp:
        cpp.write('#include "BinaryReaderRegistry.hpp"\n')
        for struct_name in sorted(type_versions.keys()):
            cpp.write(f'#include "{struct_name}.hpp"\n')
        cpp.write("\nstd::map<std::string, BinaryReader> binaryReaders = {\n")
        for struct_name in sorted(type_versions.keys()):
            cpp.write(f'    {{ "{struct_name}", [](std::istream& in) -> std::any {{\n')
            cpp.write(f'        {struct_name} s;\n')
            cpp.write(f'        in.read(reinterpret_cast<char*>(&s), sizeof({struct_name}));\n')
            cpp.write(f'        return s;\n')
            cpp.write(f'    }} }},\n')
        cpp.write("};\n")

    print("✅ BinaryReaderRegistry generated.")

if __name__ == "__main__":
    generate_registry()
