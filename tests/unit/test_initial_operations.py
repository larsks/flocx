import sys
import unittest


sys.path.insert(0, '/home/jack/git/flocx')
import flocx
from flocx.api import Base

f = Base(10, 5)

print ("Hello world")

#TODO: Still working on what to put for assertEqual

class Test_initial_operations(unittest.TestCase):
    """ Tests the operations that are needed for 
    FLOCX to operate.
    """

    def test_get_free_nodes(self):
        """tests if the flocx reports correct values of all nodes it
        has in its inventory.
        """
        result = f.get_nodes("free")
        self.assertEqual(result, 5)


    def test_buy(self):
        """Tests for buyer bids to flocx."""
        result = f.buy(who, how_many_nodes, duration, rate)


    def test_sell(self):
        """Tests a selling offer to flocx."""
        result = f.sell(who, how_many_nodes. duration, rate)

    def test_account_bal(self):
        """Tests reports credits a user is holding currently."""
        result = user.account_balance()


    def test_node_occupant(self):
        """ Tests attributes of nodes that are managed by FLOCX.
        It will have extra attributes of "owner" and "occupant"
        
        """
        result = node.get_occupant()

    def test_node_owner(self):
        """ Tests that reports owner of the node.
        """
        result = node.get_owner()


    def test_node_rental_expiry(self):
        """ Test to check for duration after which 
        FLOCX will take the node away from the occupant.
        Note occupant rents node from owner.
        """
        result = node.rental_expiry()

    def test_node_lease_expiry(self):
        """ Test to check for duration after which the nodes
        will be returned to the owner. FLOCX will not offer it 
        on the marketplace after that timestamp.
        Nor will it accept bids that exceed beyond that timestamp.
        """
        result = node.lease_expiry()

    def test_node_rate(self):
        """Tests rate at which node is rented."""
        result = node.rental_rate()








