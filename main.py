import unittest
from unittest import TestCase
import csv
import requests

plik_csv = 'https://raw.githubusercontent.com/khashishin/repozytorium_z_plikiem_polaczenia/main/phoneCalls.csv'
r = requests.get(plik_csv, allow_redirects=True)
open('phoneCalls.csv').write(r.content)

class MenadzerPolaczen:
  def __init__(self, filename):
    self.filenaCme = filename
    self.data_dict = self.read_data()

  def read_data(self):
    calls_dict_sum = dict()
    with open(self.filename, 'r') as fin:
      reader = csv.reader(fin, delimiter= ",")
      headers = next(reader)

      for row in reader:
        from_subsr = int(row[0])
        if from_subsr not in calls_dict_sum:
          calls_dict_sum[from_subsr] = 0
        calls_dict_sum[from_subsr] += 1
    return calls_dict_sum

  def pobierz_najczesciej_dzwoniacego(self):
    return max(self.data_dict.items(), key= lambda x: x[1])


class SprawdzDzwoniacegoTest(TestCase):
  def test_czy_abonent_najczesciej_dzwonioncy_rozpoznany_poprawnie(self):
      if __name__ == "__main__":
        mp = MenadzerPolaczen("phoneCalls.csv")
      wynik = mp.pobierz_najczesciej_dzwoniacego()
      self.assertEqual((226,5), wynik)

if __name__ == '__main__':
    print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())
