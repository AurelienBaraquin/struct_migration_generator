/*
    Generated from PlayerV4 to PlayerV5 migration
    PlayerV4: PlayerV4.hpp
    PlayerV5: PlayerV5.hpp
    This file is auto-generated. Do not edit it manually except for conversions fields.
*/

#include "PlayerV4.hpp"
#include "PlayerV5.hpp"
#include "RegisterConversion.hpp"

REGISTER_CONVERSION(PlayerV4, PlayerV5, [](const PlayerV4& old) {
    PlayerV5 s;


    // Conversion ------- can be modified

    s.id = old.id;

    s.score = old.score;

    s.name = old.name;

    s.email = "coucou";

    // ------------------


    return s;
});