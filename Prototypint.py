from abc import ABC, abstractmethod
import copy

class Address:
    def __init__(self):
        self.building=""
        self.street_name=""
        self.city=""
#############################################################
# abstracte Klasse. 
class EmployeePrototype(ABC):
    def __init__(self, id, name):
        self.id=id
        self.name=name
        self.emp_address= Address() # Komposition

    @abstractmethod
    def shallow_copy(self):
        pass

    @abstractmethod
    def deep_copy(self):
        pass
    # ToString Methode
    def __str__(self):
        return (
            f"\nID: {self.id},\n"
            f"Name: {self.name}\n"
            f"{self.emp_address.building}\n"
            f"{self.emp_address.city}\n"
            f"{self.emp_address.street_name}\n"
        )
################################################################
class RegEmployee(EmployeePrototype):
    def shallow_copy(self):
        # Falche Kopie des RegEmployee-objects erstellen.
        new_employee = RegEmployee(self.id,self.name)
        new_employee.emp_address = self.emp_address
        return new_employee

    def  deep_copy(self):
        # Tiefe Kopie des RegEmployee-Objekts erstellen.
        new_employee = RegEmployee(self.id,self.name)
        new_employee.emp_address = copy.deepcopy(self.emp_address) # Neue Kopie der Addresse
        return new_employee
################################################################
class TempEmployee(EmployeePrototype):
    def shallow_copy(self):
        # Flache Kopie des RegEmployee-objects erstellen.
        new_employee = TempEmployee(self.id,self.name)
        new_employee.emp_address = self.emp_address
        return new_employee
    def deep_copy(self):
        # Tief Kopie des RegEmployee-Objekts erstellen.
        new_employee = TempEmployee(self.id,self.name)
        new_employee.emp_address = copy.deepcopy(self.emp_address)
        return new_employee

# Ein Object mitarbeiter erstellen
mitarbeiter = TempEmployee(1, "Anwar")
mitarbeiter.emp_address.building = "Mein Building"
mitarbeiter.emp_address.city = "Gelsenkirchen"
mitarbeiter.emp_address.street_name = "Rudolf\n####################"

print("\nerstellteMitarbeiter: ", mitarbeiter)

# Flache oder Tieffe Kopie von der object mitarbeiter
#mitarbeiter_2 = mitarbeiter.shallow_copy()
mitarbeiter_2 = mitarbeiter.deep_copy()
print("Erstellte Mitarbeiter wurde Kopiert:\nKopierte Mitarbeiter:")
print(mitarbeiter_2)

# Wert(building) in der Kopierte object ändern
mitarbeiter_2.emp_address.building ="Zweite Bilding"
mitarbeiter_2.id=10
print("Mitarbeiter 1 nach dem Anderung eines wertes")
print(mitarbeiter)
print("Mitarbeiter 2 nach dem Anderung eines wertes")
print(mitarbeiter_2)
