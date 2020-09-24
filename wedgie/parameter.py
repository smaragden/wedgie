from arnold import *


class Parameter(object):
    def __init__(self, node_name, parameter_name):
        self._node = AiNodeLookUpByName(node_name)
        self._node_entry = AiNodeGetNodeEntry(self._node)
        self._param_entry = AiNodeEntryLookUpParameter(self._node_entry, parameter_name)

    @property
    def node(self):
        return self._node

    @property
    def name(self):
        return AiParamGetName(self._param_entry)

    @property
    def type(self):
        return AiParamGetType(self._param_entry)

    def __repr__(self):
        return "<Parameter node={} name={}>".format(
            AiNodeGetName(self._node), self.name
        )
