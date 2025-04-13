import re

def normalize_struct_name(name):
    """Supprime un éventuel suffixe Vx du nom de struct (ex: UserV3 → User)"""
    return re.sub(r'V[0-9]+$', '', name)

def compare_structs(s1, s2):
    """
    Compare deux structures (dicts au format parser.py).
    Retourne True si elles sont différentes, False sinon.
    """
    if normalize_struct_name(s1['name']) != normalize_struct_name(s2['name']):
        return True

    f1 = s1['fields']
    f2 = s2['fields']

    if len(f1) != len(f2):
        return True

    for field1, field2 in zip(f1, f2):
        if field1['type'] != field2['type'] or field1['name'] != field2['name']:
            return True

    return False
