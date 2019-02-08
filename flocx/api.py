



class Base(object):
    """ Contains basic operations of FLOCX."""


    def __init__(self, no_of_nodes, free_nodes):
        """ This is a temporary method, to test other 
        operations."""

        self._all_nodes = no_of_nodes
        self._free_nodes = free_nodes


    def get_nodes(self, arg):
        """ Reports the number of nodes available in the marketplace."""

        if(arg == "free"):
            return self._free_nodes
        elif(arg == "all"):
            return self._all_nodes



