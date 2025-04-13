/*
    Generated from PlayerV3 to PlayerV4 migration
    PlayerV3: PlayerV3.hpp
    PlayerV4: PlayerV4.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV3.hpp"
#include "PlayerV4.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV3, PlayerV4, [](const PlayerV3& old) {
    PlayerV4 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    s.name = "coucou";

    // ------------------


    return s;
});