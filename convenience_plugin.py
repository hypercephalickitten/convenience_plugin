from base_plugin import SimpleCommandPlugin
from core_plugins.player_manager import permissions, UserLevels
from packets import warp_command_write, Packets
from utility_functions import build_packet

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
    
    @permissions(UserLevels.GUEST)
    def ship(self, name):
        """Warps you to your ship. Syntax: /ship"""
        self.logger.debug("Ship command called by %s", self.protocol.player.name)
        name = self.protocol.player.name
        target_player = self.player_manager.get_logged_in_by_name(name)
        target_protocol = self.protocol.factory.protocols[target_player.protocol]
        warp_packet = build_packet(Packets.WARP_COMMAND,
                                   warp_command_write(t='WARP_UP'))
        self.protocol.client_protocol.transport.write(warp_packet)

    @permissions(UserLevels.GUEST)
    def home(self, name):
        """Warps you to your home planet. Syntax: /home"""
        self.logger.debug("Ship command called by %s", self.protocol.player.name)
        name = self.protocol.player.name
        target_player = self.player_manager.get_logged_in_by_name(name)
        target_protocol = self.protocol.factory.protocols[target_player.protocol]
        warp_packet = build_packet(Packets.WARP_COMMAND,
                                   warp_command_write(t='WARP_HOME'))
        self.protocol.client_protocol.transport.write(warp_packet)
