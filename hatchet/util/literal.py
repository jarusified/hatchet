##############################################################################
# Copyright (c) 2017-2019, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Hatchet.
# Created by Abhinav Bhatele <bhatele@llnl.gov>.
# LLNL-CODE-741008. All rights reserved.
#
# For details, see: https://github.com/LLNL/hatchet
# Please also read the LICENSE file for the MIT License notice.
##############################################################################

import numpy as np
import json

def trees_to_literal(graph, dataframe):
    """ Calls to_json in turn for each tree in the graph/forest
    """
    literal = []
    nodes = dataframe['name'].unique()
    adj_idx_map = {}
    for idx, node in enumerate(nodes):
        adj_idx_map[node] = idx

    num_of_nodes = len(nodes)
    adj_matrix = np.zeros(shape=(num_of_nodes, num_of_nodes))

    mapper = {}

    def add_nodes_and_children(hnode):
        node_df = dataframe.loc[dataframe['name'] == hnode.callpath[-1]]
        node_name = node_df['name'].unique()[0]
        children = []
        
        for child in hnode.children:
            print(type(child), child.callpath[-1])
            child_df = dataframe.loc[dataframe['name'] == child.callpath[-1]]
            print(child_df['name'].unique())
            child_name = child_df['name'].unique()[0]
            if child_name in adj_idx_map and node_name in adj_idx_map:
                source_idx = adj_idx_map[node_name]
                target_idx = adj_idx_map[child_name]
                if(adj_matrix[source_idx][target_idx] == 0.0):
                    adj_matrix[source_idx, target_idx] = 1.0                
            # if(mapper[node_name] == 1):
            children.append(add_nodes_and_children(child))

        return {
            "name": node_name,
            "children": children,
            "metrics": {
                "nid": node_df['nid'].tolist(),
                "time (inc)": node_df['time (inc)'].mean(),
                "time": node_df['time'].mean(),
                "rank": node_df['rank'].tolist(),
            }
        }

    for root in graph.roots:
        literal.append(add_nodes_and_children(root))

    return literal
