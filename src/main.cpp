#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include "BinaryReaderRegistry.hpp"
#include "VersionConverter.hpp"
#include "aliases/Player.hpp"

using json = nlohmann::json;

int main() {
    std::ifstream versionFile("../versions.json");
    json versionMap;
    versionFile >> versionMap;

    int binaryVersion = 3;
    auto versionSet = versionMap[std::to_string(binaryVersion)];

    std::cout << "Version: " << versionSet.dump(4) << std::endl;

    std::ifstream bin("data.bin", std::ios::binary);

    // Lire un Player dans la bonne version
    std::string userVersionType = versionSet["Player"];
    std::cout << "userVersionType: " << userVersionType << std::endl;
    std::any userStruct = binaryReaders[userVersionType](bin);
    std::cout << "userStruct: " << userStruct.type().name() << std::endl;
    Player player = VersionConverter::toLatest<Player>(std::move(userStruct));

    std::cout << "Player.id = " << player.id << std::endl;
    std::cout << "Player.score = " << player.score << std::endl;
    std::cout << "Player.email = " << player.email << std::endl;
    std::cout << "Player.height = " << player.height << std::endl;
}

// int main() {
//     // Create a Player object
//     PlayerV3 player;
//     player.id = 42; // Example ID
//     player.score = 100; // Example score

//     // Open a binary file for writing
//     std::ofstream bin("data.bin", std::ios::binary);

//     if (!bin) {
//         std::cerr << "Failed to open data.bin for writing." << std::endl;
//         return 1;
//     }

//     // Write the Player object to the binary file
//     bin.write(reinterpret_cast<const char*>(&player), sizeof(PlayerV3));
//     if (!bin) {
//         std::cerr << "Failed to write Player object to data.bin." << std::endl;
//         return 1;
//     }

//     bin.close();
//     std::cout << "Player object written to data.bin successfully." << std::endl;

//     return 0;
// }