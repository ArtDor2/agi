class Node:
    links_in = {}  # link to another agent, and weight
    links_out = {}

    functions = []  # agent functions to execute when activated?

    patterns = []  # ? agent patterns from data???

    # def link_add(linked_node, weight):
    #     Node.links[linked_node] = weight

    # def link_delete(linked_node, weight):  # wont be used yet
    #     del Node.links[linked_node]


# test nodes
node_a = Node()
node_b = Node()
node_c = Node()

mind = {'1': node_a, '2': node_b, '3': node_c}

# generator:
file = open("text_nano.txt", "r")
env_text = file.read()  # text env for now
file.close()

