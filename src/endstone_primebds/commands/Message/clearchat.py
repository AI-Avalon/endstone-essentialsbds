from endstone.command import CommandSender
try:
    from endstone.command import BlockCommandSender
except ImportError:
    BlockCommandSender = None 
from endstone_primebds.utils.command_util import create_command

from typing import TYPE_CHECKING
from endstone_primebds.utils.locale_util import tr

if TYPE_CHECKING:
    from endstone_primebds.primebds import OnistoneEssentials

# Register command
command, permission = create_command(
    "clearchat",
    tr("clearchat.msg_1", "Adds 100 empty lines to chat!"),
    ["/clearchat"],
    ["onistone.command.clearchat"]
)

def handler(self: "OnistoneEssentials", sender: CommandSender, args: list[str]) -> bool:
    if BlockCommandSender is not None and isinstance(sender, BlockCommandSender):
       sender.send_message(tr("clearchat.msg_2", "§cThis command cannot be automated"))
       return False



    empty_lines = 100
    for player in self.server.online_players:
        player.send_message("\n" * empty_lines)
        player.send_message(tr("clearchat.msg_3", "§cGlobal chat was cleared"))
