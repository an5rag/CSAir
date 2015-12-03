import json
from unittest import TestCase
from csAir.Edge import Edge
from csAir.Graph import make_graph

__author__ = 'an5ra'
def parse_json(text_file_name):
    with open (text_file_name, "r") as myfile:
        data=myfile.read()
    return json.loads(data)
#parse the json
json_data = parse_json("mockJsonText.txt")

#construct dictionary of edges
dict_of_edges = Edge.make_dict(json_data)

#construct graph
graph = make_graph(dict_of_edges)

class TestMake_graph(TestCase):
  def test_make_graph(self):
    no_of_cities_made = len(graph)
    self.assertEqual(3,no_of_cities_made)
