#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os, sys, re
import logging
import argparse
import collections
import numpy
import time

from Node import *

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)


class Node_path:

    def __init__(self, transcript_name, path_string, sequence):
        self.transcript_name = transcript_name
        self.node_obj_list = list()

        node_descr_list = re.findall("\d+:\d+\-\d+", path_string)

        obj_node_list = list()
        for node_descr in node_descr_list:
            (loc_node_id, node_coord_range) = node_descr.split(":")
            (lend,rend) = node_coord_range.split("-")
            lend = int(lend)
            rend = int(rend)
            
            node_obj = Node.get_node(transcript_name, loc_node_id, sequence[lend:rend+1]) # coords in path were already zero-based
            
            self.node_obj_list.append(node_obj)


    def get_transcript_name(self):
        return self.transcript_name

    def get_path(self):
        return self.node_obj_list
    

    def __repr__(self):
        node_str_list = list()
        for node in self.node_obj_list:
            node_str_list.append(str(node))

        path_str = "--".join(node_str_list)

        return path_str
        