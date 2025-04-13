// RegisterConversion.hpp
#pragma once
#include "VersionConverter.hpp"

#define REGISTER_CONVERSION(FROM, TO, FUNC)              \
    namespace {                                          \
        struct AutoRegister_##FROM##_to_##TO {           \
            AutoRegister_##FROM##_to_##TO() {            \
                VersionGraph::instance().registerConverter( \
                    typeid(FROM),                        \
                    typeid(TO),                          \
                    [](const std::any& a) -> std::any {  \
                        return std::any(FUNC(std::any_cast<const FROM&>(a))); \
                    });                                  \
            }                                            \
        };                                               \
        static AutoRegister_##FROM##_to_##TO reg_##FROM##_to_##TO; \
    }
