/*
    Generated from {{from_struct}} to {{to_struct}} migration
    {{from_struct}}: {{from_header}}
    {{to_struct}}: {{to_header}}
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "{{from_header}}"
#include "{{to_header}}"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION({{from_struct}}, {{to_struct}}, [](const {{from_struct}}& old) {
    {{to_struct}} s;


    // Conversion ------- can be modified
{% for field in to_fields %}
    s.{{field.name}} = {% if field.name in from_field_names %}old.{{field.name}}{% else %}{{default_value(field.type)}}{% endif %};
{% endfor %}
    // ------------------


    return s;
});
