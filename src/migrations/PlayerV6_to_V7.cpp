/*
    Generated from PlayerV6 to PlayerV7 migration
    PlayerV6: PlayerV6.hpp
    PlayerV7: PlayerV7.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV6.hpp"
#include "PlayerV7.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV6, PlayerV7, [](const PlayerV6& old) {
    PlayerV7 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    s.email = old.email;

    s.height = old.height;

    // ------------------


    return s;
});