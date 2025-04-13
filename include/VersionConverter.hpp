#pragma once

#include <functional>
#include <map>
#include <typeindex>
#include <type_traits>
#include <any>
#include <stdexcept>
#include <memory>

#include <iostream>

class VersionGraph {
public:
    using ConverterFn = std::function<std::any(const std::any&)>;

    static VersionGraph& instance() {
        static VersionGraph inst;
        return inst;
    }

    void registerConverter(std::type_index from, std::type_index to, ConverterFn fn) {
        converters[{from, to}] = std::move(fn);
    }

    std::any convertTo(std::any data, std::type_index from, std::type_index to) const {
        std::cout << "[VersionGraph] Converting from: " << from.name()
          << " to: " << to.name() << std::endl;
        if (from == to) return data;
        std::type_index current = from;

        while (current != to) {
            bool found = false;
            for (const auto& [key, fn] : converters) {
                std::cout << "Checking converter: " << key.first.name() << " → " << key.second.name() << std::endl;
                if (key.first == current) {
                    data = fn(data);
                    current = key.second;
                    found = true;
                    break;
                }
            }
            if (!found) throw std::runtime_error("No conversion path found.");
        }
        return data;
    }

private:
    std::map<std::pair<std::type_index, std::type_index>, ConverterFn> converters;
};

class VersionConverter {
    public:
        template<typename Target, typename Source>
        static Target toLatest(const Source& src) {
            std::cout << "Converting (typed)" << std::endl;
            std::any result = VersionGraph::instance().convertTo(src, typeid(Source), typeid(Target));
            return std::any_cast<Target>(result);
        }
    
        template<typename Target>
        static Target toLatest(std::any src) {
            std::cout << "Converting (any)" << std::endl;
            std::any result = VersionGraph::instance().convertTo(src, src.type(), typeid(Target));
            return std::any_cast<Target>(result);
        }
    };
    