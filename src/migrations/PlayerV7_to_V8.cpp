/*
    Generated from PlayerV7 to PlayerV8 migration
    PlayerV7: PlayerV7.hpp
    PlayerV8: PlayerV8.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV7.hpp"
#include "PlayerV8.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV7, PlayerV8, [](const PlayerV7& old) {
    PlayerV8 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    s.email = old.email;

    s.height = old.height;

    s.name = "";

    s.address = "";

    s.latitude = 0.0;

    // ------------------


    return s;
});