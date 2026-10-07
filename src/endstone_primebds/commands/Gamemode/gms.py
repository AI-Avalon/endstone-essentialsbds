from endstone import Player, GameMode
from endstone.command import CommandSender
from endstone_primebds.utils.command_util import create_command
from endstone_primebds.utils.target_selector_util import get_matching_actors

from typing import TYPE_CHECKING
from endstone_primebds.utils.locale_util import tr
if TYPE_CHECKING:
    from endstone_primebds.primebds import OnistoneEssentials

# Register command
command, permission = create_command(
    "gms",
    tr("gma.msg_1", "Sets your game mode to adventure!"),
    ["/gms [player: player]"],
    ["onistone.command.gms"]
)

# GMA COMMAND FUNCTIONALITY
def handler(self: "OnistoneEssentials", sender: CommandSender, args: list[str]) -> bool:
    if len(args) == 0:
        if not isinstance(sender, Player):
            sender.send_message(tr("heal.not_player", "This command can only be executed by a player"))
            return False
        sender.game_mode = GameMode.SURVIVAL
        sender.send_message(tr("gms.msg_1", "Set own game mode to Survival"))
        return True

    targets = get_matching_actors(self, args[0], sender)
    for target in targets:
        target.game_mode = GameMode.SURVIVAL
        target.send_message(tr("gms.msg_2", "Your game mode has been updated to Survival"))
    sender.send_message(f"§e{len(targets)} §rplayers were set to Survival")

    return True
