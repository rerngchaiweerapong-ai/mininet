from mininet.topo import Topo

class SDNTopo(Topo):
    def build(self):

        # Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        mgmt = self.addHost('mgmt')
        server = self.addHost('server')

        # Switches
        sw1 = self.addSwitch('sw1')
        sw2 = self.addSwitch('sw2')
        sw3 = self.addSwitch('sw3')
        sw4 = self.addSwitch('sw4')
        sw5 = self.addSwitch('sw5')

        # Host connections
        self.addLink(h1, sw1, delay='2ms', bw=10)
        self.addLink(h2, sw2, delay='2ms', bw=10)
        self.addLink(mgmt, sw5, delay='2ms', bw=10)
        self.addLink(server, sw5, delay='2ms', bw=1000)

        # Inter-switch links (example bandwidths)
        self.addLink(sw1, sw3, delay='2ms', bw=100)
        self.addLink(sw1, sw4, delay='2ms', bw=100)
        self.addLink(sw2, sw4, delay='2ms', bw=100)
        self.addLink(sw2, sw3, delay='2ms', bw=100)
        self.addLink(sw3, sw5, delay='2ms', bw=1000)
        self.addLink(sw4, sw5, delay='2ms', bw=1000)

topos = {'sdn': SDNTopo}
