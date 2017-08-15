/////////////////////////////////////////////////////////////////////////////
// This file is part of the Journey MMORPG client                           //
// Copyright � 2015-2016 Daniel Allendorf                                   //
//                                                                          //
// This program is free software: you can redistribute it and/or modify     //
// it under the terms of the GNU Affero General Public License as           //
// published by the Free Software Foundation, either version 3 of the       //
// License, or (at your option) any later version.                          //
//                                                                          //
// This program is distributed in the hope that it will be useful,          //
// but WITHOUT ANY WARRANTY; without even the implied warranty of           //
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            //
// GNU Affero General Public License for more details.                      //
//                                                                          //
// You should have received a copy of the GNU Affero General Public License //
// along with this program.  If not, see <http://www.gnu.org/licenses/>.    //
//////////////////////////////////////////////////////////////////////////////
#pragma once
#include "../Error.h"

#include <cstdint>
#include <array>

namespace jrc
{
    namespace NxFiles
    {
        // Number of needed files.
        constexpr uint8_t NUM_FILES = 14;
        // Names of the needed game files.
        constexpr std::array<const char*, NUM_FILES> filenames =
        {
            "Character.nx", "Effect.nx", "Etc.nx",   "Item.nx",
            "Map.nx",       "Mob.nx",    "Npc.nx",   "Quest.nx",
            "Reactor.nx",   "Skill.nx",  "Sound.nx", "String.nx",
            "TamingMob.nx", "UI.nx"
        };

        // Initialize nlnx.
        // When successful, also tests if the UI file contains valid images.
        Error init();
    };
}
