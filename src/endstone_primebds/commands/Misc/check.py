from datetime import datetime

from endstone import GameMode
from endstone_primebds.utils.time_util import TimezoneUtils
from endstone_primebds.utils.mod_util import format_time_remaining
from endstone.command import CommandSender
from endstone_primebds.utils.command_util import create_command

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from endstone_primebds.primebds import OnistoneEssentials

# Register command
command, permission = create_command(
    "check",
    "Checks a player's client info!",
    ["/check <player: player> (info|mod|jail|network|world)[info: info]"],
    ["onistone.command.check"],
    "op",
    ["seen"]
)

# CHECK COMMAND FUNCTIONALITY
def handler(self: "OnistoneEssentials", sender: CommandSender, args: list[str]) -> bool:
    from endstone_primebds.utils.locale_util import tr

    if any("@" in arg for arg in args):
        sender.send_message(tr("common.target_selector_invalid", f"§cTarget selectors are invalid for this command"))
        return False

    player_name = args[0].strip('"')
    filter_type = args[1].lower() if len(args) > 1 else "info"  # default to info if not provided
    target = sender.server.get_player(player_name)

    if target is None:
        # Check Offline DB
        user = self.db.get_offline_user(player_name)
        user_mod = self.db.get_offline_mod_log(player_name)
        if user is None:
            sender.send_message(
                tr("common.player_not_found", f"Player §e{player_name}§c not found in database.", player_name=player_name)
            )
            return False

        xuid = user.xuid
        uuid = user.uuid
        unique_id = user.unique_id
        name = user.name
        ping = f"{user.ping}ms §7[Last Recorded§7]"
        device_os = user.device_os
        device_id = user.device_id
        version = user.client_ver
        rank = user.internal_rank
        last_join = user.last_join
        last_leave = user.last_leave
        status = tr("check.status_offline", f"§cOffline")
        is_jailed = bool(user_mod.is_jailed)
        jail_reason = user_mod.jail_reason
        jail_time = user_mod.jail_time
        jail = user_mod.jail
        jail_return_loc = user_mod.return_jail_pos
        jail_return_dim = user_mod.return_jail_dim
        is_ip_muted = bool(user_mod.is_ip_muted)
        is_ip_banned = bool(user_mod.is_ip_banned)
        is_banned = bool(user_mod.is_banned)
        ban_reason = user_mod.ban_reason
        ban_time = user_mod.banned_time
        is_muted = bool(user_mod.is_muted)
        mute_reason = user_mod.mute_reason
        mute_time = user_mod.mute_time
        ip = user_mod.ip_address

    else:
        # Fetch Online Data
        user = self.db.get_online_user(target.xuid)
        user_mod = self.db.get_mod_log(target.xuid)
        xuid = target.xuid
        uuid = target.unique_id
        unique_id = user.unique_id
        name = target.name
        ping = f"{target.ping}ms"
        device_os = user.device_os
        device_id = user.device_id
        version = target.game_version
        rank = user.internal_rank
        last_join = user.last_join
        last_leave = user.last_leave
        status = tr("check.status_online", f"§aOnline")
        is_jailed = bool(user_mod.is_jailed)
        jail_reason = user_mod.jail_reason
        jail_time = user_mod.jail_time
        jail = user_mod.jail
        jail_return_loc = user_mod.return_jail_pos
        jail_return_dim = user_mod.return_jail_dim
        is_ip_muted = bool(user_mod.is_ip_muted)
        is_ip_banned = bool(user_mod.is_ip_banned)
        is_banned = bool(user_mod.is_banned)
        ban_reason = user_mod.ban_reason
        ban_time = user_mod.banned_time
        is_muted = bool(user_mod.is_muted)
        mute_reason = user_mod.mute_reason
        mute_time = user_mod.mute_time
        ip = str(target.address)

    join_time = TimezoneUtils.convert_to_timezone(last_join, "EST")

    dt = datetime.fromtimestamp(last_leave)
    year = dt.year

    leave_time_str = (
        tr("check.not_applicable", "N/A")
        if year < 2000
        else TimezoneUtils.convert_to_timezone(last_leave, "EST")
    )

    if filter_type == "info":
        sender.send_message(tr("check.player_database_info", f"§bPlayer Database Information:\n§7- §eName: §f{name} §8[{status}§8]\n§7- §eXUID: §f{xuid}\n§7- §eUUID: §f{uuid}\n§7- §eUnique ID: §f{unique_id}\n§7- §eInternal Rank: §f{rank}\n§7- §eDevice OS: §f{device_os}\n§7- §eDevice ID: §f{device_id}\n§7- §eClient Version: §f{version}\n§7- §ePing: §f{ping}\n§7- §eLast Join: §f{join_time}\n§7- §eLast Leave: §f{leave_time_str}\n", name=name, status=status, xuid=xuid, uuid=uuid, unique_id=unique_id, rank=rank, device_os=device_os, device_id=device_id, version=version, ping=ping, join_time=join_time, leave_time_str=leave_time_str))

    elif filter_type == "mod":

        warning = self.db.get_latest_active_warning(None, player_name)

        ban_info = ""
        name_ban_info = ""
        mute_info = ""
        warn_info = ""

        if is_banned:
            ban_info = tr("check.ban_reason", f"\n§7  - §eBan Reason: §f{ban_reason}\n§7  - §eBan Expires: §f{format_time_remaining(ban_time)}", reason=ban_reason, expires=format_time_remaining(ban_time))
        
        if self.serverdb.check_nameban(player_name):
            name_ban = self.serverdb.get_ban_info(player_name)
            name_ban_info = f"""
§7  - §eBan Reason: §f{name_ban.ban_reason}
§7  - §eBan Expires: §f{format_time_remaining(name_ban.banned_time)}
"""

        if is_muted:
            mute_info = tr("check.mute_reason", f"\n§7  - §eMute Reason: §f{mute_reason}\n§7  - §eMute Expires: §f{format_time_remaining(mute_time, is_mute=True)}", reason=mute_reason, expires=format_time_remaining(mute_time, is_mute=True))
            
        if warning:
            warn_info = f"""
§7  - §eWarn Reason: §f{warning["warn_reason"]}
§7  - §eWarn Expires: §f{format_time_remaining(warning["warn_time"], True)}
"""

        sender.send_message(f"""§6Player Mod Information:
§7- §eName: §f{name} §8[{status}§8]
§7- §eRank: §f{rank}
§7- §eBanned: §f{is_banned} §8[§7IP: {is_ip_banned}§8]{ban_info}
§7- §eName Banned: §f{self.serverdb.check_nameban(player_name)}{name_ban_info}
§7- §eMuted: §f{is_muted} §8[§7IP: {is_ip_muted}§8]{mute_info}
§7- §eWarned: §f{bool(warning)}{warn_info}
""")

    elif filter_type == "jail":

        jail_info = ""
        
        if is_jailed:
            jail = self.serverdb.get_jail(jail, self.server)
            if jail:
                parts = jail_return_loc.split(",")
                x = float(parts[0])
                y = float(parts[1])
                z = float(parts[2])
                loc = jail["pos"]
                jail_info = tr("check.jail_details", f"\n§7  - §eJail: §f{jail['name']}\n§7  - §eJail Location: §f{round(loc.x)} {round(loc.y)} {round(loc.z)} §8[§e{loc.dimension.name}§8]\n§7  - §eJail Reason: §f{jail_reason}\n§7  - §eJail Time: §f{format_time_remaining(jail_time)}\n§7  - §eJail Return Location: §f{round(x)} {round(y)} {round(z)} §8[§e{jail_return_dim}§8]", jail_name=jail['name'], loc_x=round(loc.x), loc_y=round(loc.y), loc_z=round(loc.z), loc_dim=loc.dimension.name, reason=jail_reason, time=format_time_remaining(jail_time), ret_x=round(x), ret_y=round(y), ret_z=round(z), ret_dim=jail_return_dim)

        sender.send_message(tr("check.player_jail_info", f"§6Player Jail Information:\n§7- §eName: §f{name} §8[{status}§8]\n§7- §eRank: §f{rank}\n§7- §eJail Status: §f{is_jailed}{jail_info}\n", name=name, status=status, rank=rank, is_jailed=is_jailed, jail_info=jail_info))

    elif filter_type == "network":
        sender.send_message(tr("check.player_network_info", f"§dPlayer Network Information:\n§7- §eName: §f{name} §8[{status}§8]\n§7- §eIP: §f{ip}\n", name=name, status=status, ip=ip))

    elif filter_type == "world":
        if target:
            sender.send_message(tr("check.player_world_info", f"§aPlayer World Information:\n§7- §eName: §f{name} §8[{status}§8]\n§7- §eUnique ID: §f{target.id}\n§7- §eGamemode: §f{target.game_mode.name}\n§7- §eLocation: §fx: {target.location.block_x} §7/ §fy: {target.location.block_y} §7/ §fz: {target.location.block_z}\n§7- §eRotation: §fyaw: {round(target.location.yaw, 2)} §7/ §fpitch: {round(target.location.pitch, 2)}\n§7- §eDimension: §f{target.dimension.name}\n§7- §eHealth: §f{target.health}/{target.max_health}\n§7- §eTotal XP: §f{target.total_exp}\n§7- §eGrounded: §f{target.is_on_ground}\n§7- §eIn Lava: §f{target.is_in_lava}\n§7- §eIn Water: §f{target.is_in_water}\n§7- §eIs OP: §f{target.is_op}\n§7- §eCan Fly: §f{target.allow_flight}\n§7- §eTags: §f{target.scoreboard_tags}\n", name=name, status=status, unique_id=target.id, gamemode=target.game_mode.name, x=target.location.block_x, y=target.location.block_y, z=target.location.block_z, yaw=round(target.location.yaw, 2), pitch=round(target.location.pitch, 2), dimension=target.dimension.name, health=target.health, max_health=target.max_health, xp=target.total_exp, grounded=target.is_on_ground, in_lava=target.is_in_lava, in_water=target.is_in_water, is_op=target.is_op, can_fly=target.allow_flight, tags=target.scoreboard_tags))
        else:
            sender.send_message(tr("common.player_not_online", f"§cPlayer must be online to check world data"))

    else:
        sender.send_message(tr("check.invalid_filter", f"§cInvalid filter type '{filter_type}'", filter_type=filter_type))
        return False

    return True
