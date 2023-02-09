import re

class Node:
    def __init__(self, func, inputs, outputs, name):
        self.func = func
        self.inputs = inputs
        self.outputs = outputs if outputs is not None else []
        self.name = name

class Pipeline:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, node):
        node.inputs = [n.outputs for n in self.nodes]
        self.nodes.append(node)
    
    def node_dependencies(self):
        nodes_deps = []
        for node in self.nodes:
            deps = []
            for n in self.nodes:
                if node.name == n.name:
                    break
                deps.append(n.name)
            nodes_deps.append({'node': node, 'name': node.name, 'deps': deps})
        return nodes_deps
    
def create_pipeline(nodes):
    pipeline = Pipeline()
    for node in nodes:
        pipeline.add_node(node)
    return pipeline

def clean_name(name):
    return re.sub(r"[\W_]+", "-", name).strip("-")

def get_dependencies(dependencies):
    deps_dict = [
        {
            "node": node,
            "name": clean_name(node),
            "deps": [clean_name(val) for val in parent_nodes],
        }
        for node, parent_nodes in dependencies.items()
    ]
    return deps_dict
