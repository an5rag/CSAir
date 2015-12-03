from unittest import TestCase
from csAir.Edge import Edge
import json


def parse_json(text_file_name):
    with open (text_file_name, "r") as myfile:
        data=myfile.read()
    return json.loads(data)

def prepare_test_data():
  json_data = parse_json("mockJsonText.txt")
  dict_of_edges = Edge.make_dict(json_data)
  return dict_of_edges


class TestEdge(TestCase):
  def test_make_dict(self):
    dict_of_edges = prepare_test_data()
    no_of_edges_made = len(dict_of_edges)
    self.assertEqual(4,no_of_edges_made)

  def test_get_longest_flight(self):
    dict_of_edges = prepare_test_data()
    answer = Edge.get_longest_flight(dict_of_edges)
    self.assertTrue("LON-NYC" in answer or "NYC-LON" in answer)

  def test_get_shortest_flight(self):
    dict_of_edges = prepare_test_data()
    answer = Edge.get_shortest_flight(dict_of_edges)
    self.assertTrue("LON-ESS" in answer or "ESS-LON" in answer)

  def test_remove_city_edges(self):
    dict_of_edges = prepare_test_data()
    print("\n\nREMOVE CITY EDGES\n----------------")
    print("\nBefore deletion:")
    print(dict_of_edges)
    Edge.remove_city_edges(dict_of_edges, 'ESS')
    print("\nAfter deletion:")
    print(dict_of_edges)

