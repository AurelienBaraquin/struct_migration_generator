#pragma once
#include <map>
#include <functional>
#include <any>
#include <istream>

using BinaryReader = std::function<std::any(std::istream&)>;
extern std::map<std::string, BinaryReader> binaryReaders;
