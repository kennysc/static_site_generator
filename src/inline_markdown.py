from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    Takes a list of "old_nodes", a delimiter and a text type.
    Returns a new list of nodes where any "text" type nodes are
    split into multiple nodes based on the syntax
    '''
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_split = node.text.split(delimiter)
        if len(text_split) % 2 == 0:
            raise Exception(f'Invalid markdown syntax, unmatched "{delimiter}" delimiter in "{node.text}"')
        for i in range(len(text_split)):
            if text_split[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(
                    TextNode(text_split[i], TextType.TEXT)
                )
            else:
                new_nodes.append(
                    TextNode(text_split[i], text_type)
                )
    return new_nodes
