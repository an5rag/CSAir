import json
from unittest import TestCase
from csAir.City import City


def parse_json(text_file_name):
  with open(text_file_name, "r") as myfile:
    data = myfile.read()
  return json.loads(data)


__author__ = 'an5ra'

def prepare_test_data():
  json_data = parse_json("mockJsonText.txt")
  dict_of_cities = City.make_city_dict(json_data)
  return dict_of_cities



class TestCity(TestCase):
  def test_make_city_dict(self):
    dict_of_cities = prepare_test_data()
    no_of_cities_made = len(dict_of_cities)
    self.assertEqual(3, no_of_cities_made)

  def test_get_city_code(self):
    dict_of_cities = prepare_test_data()
    code = City.get_city_code("london", dict_of_cities)
    self.assertEqual("LON", code)

  def test_get_biggest_city(self):
    dict_of_cities = prepare_test_data()
    answer = City.get_biggest_city(dict_of_cities)
    self.assertTrue("New York" in answer)

  def test_get_smallest_city(self):
    dict_of_cities = prepare_test_data()
    answer = City.get_smallest_city(dict_of_cities)
    self.assertTrue("Essen" in answer)

  def test_get_average_population(self):
    dict_of_cities = prepare_test_data()
    answer = City.get_average_population(dict_of_cities)
    self.assertTrue(int(answer) == 11729966)

  def test_add_city(self):
    dict_of_cities = prepare_test_data()
    City.add_city(dict_of_cities,"ABC", "Alphabet", "Google", "North America", "EST", "sdfsfd", 123, "qwe")
    if not 'ABC' in dict_of_cities:
      self.fail()

  def test_remove_city(self):
    dict_of_cities = prepare_test_data()
    to_remove_city_code = 'LON'
    City.remove_city(dict_of_cities, to_remove_city_code)
    if 'LON' in dict_of_cities:
      self.fail()
