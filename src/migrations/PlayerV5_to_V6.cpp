/*
    Generated from PlayerV5 to PlayerV6 migration
    PlayerV5: PlayerV5.hpp
    PlayerV6: PlayerV6.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV5.hpp"
#include "PlayerV6.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV5, PlayerV6, [](const PlayerV5& old) {
    PlayerV6 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    s.name = old.name;

    s.email = old.email;

    s.height = 0.0;

    // ------------------


    return s;
});