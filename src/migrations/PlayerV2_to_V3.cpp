/*
    Generated from PlayerV2 to PlayerV3 migration
    PlayerV2: PlayerV2.hpp
    PlayerV3: PlayerV3.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV2.hpp"
#include "PlayerV3.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV2, PlayerV3, [](const PlayerV2& old) {
    PlayerV3 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    // ------------------


    return s;
});