from unittest import TestCase

from csAir.jsonUtilities import jsonUtility
from csAir.jsonUtilities.jsonUtility import parse_json

__author__ = 'an5ra'


class TestJson_Utility(TestCase):
  def test_delete_route_from_json_data(self):
    json_data = parse_json("mockJsonText.txt")
    print("\n\nROUTE DELETION\n----------------")
    print("Before deletion:")
    print(json_data["routes"])
    result = jsonUtility.delete_route_from_json_data(json_data, 'LON-NYC')
    print("After deletion:")
    print(json_data["routes"])
    if not result:
      self.fail()

  def test_delete_city_from_json_data(self):
    json_data = parse_json("mockJsonText.txt")
    print("\n\nCITY DELETION\n----------------")
    print("Before deletion:")
    print(json_data["metros"])
    result = jsonUtility.delete_city_from_json_data(json_data, 'LON')
    print("After deletion:")
    print(json_data["metros"])
    if not result:
      self.fail()

  def test_add_city_to_json(self):
    json_data = parse_json("mockJsonText.txt")
    print("\n\nCITY ADDITION\n----------------")
    print("Before addition:")
    print(json_data["metros"])
    old_length = len(json_data["metros"])
    jsonUtility.add_city_to_json_data(json_data,"SCL","Santiago","CL","South America",-4,{"S" : 33, "W" : 71}, 6000000, 1)
    print("After addition:")
    print(json_data["metros"])
    new_length = len(json_data["metros"])
    if(old_length==new_length):
      self.fail()

  def test_add_route_to_json(self):
    json_data = parse_json("mockJsonText.txt")
    print("\n\nROUTE ADDITION\n----------------")
    print("Before addition:")
    print(json_data["routes"])
    old_length = len(json_data["routes"])
    jsonUtility.add_route_to_json_data(json_data,'SCL','LON',2345)
    print("After addition:")
    print(json_data["routes"])
    new_length = len(json_data["routes"])
    if(old_length==new_length):
      self.fail()