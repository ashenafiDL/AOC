import networkx as nx


def check_if_correctly_ordered(graph, pages):
    """Check if the give list of pages in correct order"""

    sub_graph = nx.subgraph(graph, pages)
    topo_sort = list(nx.topological_sort(sub_graph))

    return topo_sort == pages


def corrected_order(graph, pages):
    """Return the correct order of the pages"""

    sub_graph = nx.subgraph(graph, pages)
    correct_order = list(nx.topological_sort(sub_graph))

    return correct_order


def get_middle_page(pages) -> int:
    """Return the middle page of the given list of pages"""

    middle = len(pages) // 2
    return int(pages[middle])


def main(lines):
    separator_index = lines.index("\n")
    rules = lines[:separator_index]
    updates = lines[separator_index + 1 :]

    # Created a directed graph for rules
    G = nx.DiGraph()
    for rule in rules:
        rule = rule.strip().split("|")
        G.add_node(rule[0])
        G.add_node(rule[1])
        G.add_edge(rule[0], rule[1])

    middle_sum = 0
    middle_sum_for_incorrect_updates = 0
    for update in updates:
        pages = update.strip().split(",")
        if check_if_correctly_ordered(G, pages):
            middle_sum += get_middle_page(pages)
        else:
            correct_order = corrected_order(G, pages)
            middle_sum_for_incorrect_updates += get_middle_page(correct_order)

    print("Middle sum:", middle_sum)
    print("Middle sum for incorrect updates:", middle_sum_for_incorrect_updates)
