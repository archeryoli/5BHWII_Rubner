class Firma():
  def __init__(self) -> None:
    self.abteilungen = []
  
  def amount_of_employees(self):
    return sum(list(map(lambda x: len(x.mitarbeiter), self.abteilungen)))
  
  def amount_of_abteilungsleiter(self):
    return len(list(filter(lambda mitarbeiter: isinstance(mitarbeiter, AbteilungsVorstand), [y for x in  map(lambda x: x.mitarbeiter, self.abteilungen) for y in x])))
  
  def amount_of_abteilungen(self):
    return len(self.abteilungen)
  
  def max_mitarbeiter(self):
    return list(filter(lambda x: len(x.mitarbeiter) == max(list(map(lambda x: len(x.mitarbeiter), self.abteilungen))), self.abteilungen))[0]

  def percent_woman(self):
    return len(list(filter(lambda mitarbeiter: mitarbeiter.gender, [item for sublist in list(map(lambda x: x.mitarbeiter, self.abteilungen)) for item in sublist]))) * 100/ self.amount_of_employees()

class Abteilung():
  def __init__(self, name) -> None:
    self.name = name
    self.mitarbeiter = []
  
  def amount_of_mitarbeiter(self):
    return len(self.mitarbeiter)
  
  def add_mitarbeiter(self, mitarbeiter):
    if isinstance(mitarbeiter, AbteilungsVorstand):
      for mitarbeiter in self.mitarbeiter:
        if isinstance(mitarbeiter, AbteilungsVorstand):
          raise Exception("Es darf nur einen Abteilungsleiter geben")
        
      self.mitarbeiter.append(mitarbeiter)
      return
    self.mitarbeiter.append(mitarbeiter)

class Person():
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender

class Mitarbeiter(Person):
  def __init__(self,name,  gender: bool) -> None:
    super().__init__(name, gender)

class AbteilungsVorstand(Mitarbeiter):
  def __init__(self, name, gender: bool) -> None:
    super().__init__(name, gender)



if __name__ == '__main__':
  firma = Firma()
  abteilung = Abteilung("Vertrieb")
  abteilung.add_mitarbeiter(AbteilungsVorstand("Max Mustermann",  True))
  abteilung.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  abteilung.add_mitarbeiter(Mitarbeiter("Max Mustermann", False))
  abteilung.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  abteilung.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  abteilung.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  firma.abteilungen.append(abteilung)

  abteilung2 = Abteilung("IT")
  abteilung2.add_mitarbeiter(AbteilungsVorstand("Max Mustermann", True))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", False))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", False))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", False))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  abteilung2.add_mitarbeiter(Mitarbeiter("Max Mustermann", True))
  firma.abteilungen.append(abteilung2)
  print("Anzahl Mitarbeiter:",firma.amount_of_employees())
  print("Anzahl Abteilungsleiter:",firma.amount_of_abteilungsleiter())
  print("Anzahl Abteilungen:", firma.amount_of_abteilungen())
  print("Maximale Mitarbeiteranzahl in einer Abteilung:", len(firma.max_mitarbeiter().mitarbeiter))
  # v1, v2 = firma.percent_woman()
  # print("Prozent der Frauen in der Firma:", v1, "%", v2)
  print("Prozent der Frauen in der Firma:", firma.percent_woman(), "%")