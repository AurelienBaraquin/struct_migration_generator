/*
    Generated from PlayerV1 to PlayerV2 migration
    PlayerV1: PlayerV1.hpp
    PlayerV2: PlayerV2.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV1.hpp"
#include "PlayerV2.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV1, PlayerV2, [](const PlayerV1& old) {
    PlayerV2 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    // ------------------


    return s;
});