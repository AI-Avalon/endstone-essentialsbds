from endstone import Player
from endstone.command import CommandSender
from endstone_primebds.utils.command_util import create_command
from endstone_primebds.utils.target_selector_util import get_matching_actors

from typing import TYPE_CHECKING
from endstone_primebds.utils.locale_util import tr
if TYPE_CHECKING:
    from endstone_primebds.primebds import OnistoneEssentials

# Register command
command, permission = create_command(
    "heal",
    tr("heal.msg_1", "Sets player health to full!"),
    ["/heal [player: player]"],
    ["onistone.command.heal", "onistone.command.heal.other"]
)

# HEAL COMMAND FUNCTIONALITY
def handler(self: "OnistoneEssentials", sender: CommandSender, args: list[str]) -> bool:
    from endstone_primebds.utils.locale_util import tr

    if len(args) == 0:
        if not isinstance(sender, Player):
            sender.send_message(tr("heal.not_player", "This command can only be executed by a player"))
            return False
        sender.health = sender.max_health
        sender.send_message(tr("heal.healed", "§aYou were healed"))
        return True
    
    if not sender.has_permission("onistone.command.heal.other"):
        sender.send_message(tr("heal.no_perm_other", "§cYou do not have permission to heal others"))
        return True
    
    targets = get_matching_actors(self, args[0], sender)
    for target in targets:
        target.health = target.max_health
        target.send_message(tr("heal.healed", "§aYou were healed"))
        
    if len(targets) == 1:
        sender.send_message(tr("heal.healed_one", f"§e{targets[0].name} §rwas healed", target=targets[0].name))
    else:
        sender.send_message(tr("heal.healed_multiple", f"§e{len(targets)} §rplayers were healed", count=len(targets)))

    return True
