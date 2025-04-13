#include "BinaryReaderRegistry.hpp"
#include "PlayerV3.hpp"

std::map<std::string, BinaryReader> binaryReaders = {
    { "PlayerV3", [](std::istream& in) -> std::any {
        PlayerV3 s;
        in.read(reinterpret_cast<char*>(&s), sizeof(PlayerV3));
        return s;
    } },
};
