from base_plugin import SimpleCommandPlugin
from plugins.core.player_manager import permissions, UserLevels
from packets import warp_command_write, Packets, warp_command
from utility_functions import build_packet, extract_name


class Convenience(SimpleCommandPlugin):
    """
    Plugin that allows players to warp to their ship and home planet.
    """
    name = "convenience_plugin"
    depends = ['command_dispatcher', 'player_manager']
    commands = ["ship", "home"]
    auto_activate = True

    def activate(self):
        super(Convenience, self).activate()
        self.player_manager = self.plugins['player_manager'].player_manager

    @permissions(UserLevels.REGISTERED)
    def ship(self, arg):
        """Warps you to your ship.\nSyntax: /ship"""
        player = self.player_manager.get_logged_in_by_name(self.protocol.player.name)
        from_protocol = self.factory.protocols[player.protocol]
        warp_packet = build_packet(Packets.WARP_COMMAND, warp_command_write(t='WARP_UP'))
        from_protocol.client_protocol.transport.write(warp_packet)
        self.protocol.send_chat_message("^yellow;%s^green; warped to their ship." % self.protocol.player.name)

    @permissions(UserLevels.REGISTERED)
    def home(self, arg):
        """Warps you to your home planet.\nSyntax: /home"""
        player = self.player_manager.get_logged_in_by_name(self.protocol.player.name)
        from_protocol = self.factory.protocols[player.protocol]
        warp_packet = build_packet(Packets.WARP_COMMAND, warp_command_write(t='WARP_HOME'))
        from_protocol.client_protocol.transport.write(warp_packet)
        self.protocol.send_chat_message("^yellow;%s^green; warped to their home planet." % self.protocol.player.name)

