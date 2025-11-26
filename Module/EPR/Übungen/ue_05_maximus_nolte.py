"""
    Dieses Modul verwaltet ein Inventarsystem mit verschiedenen Lagerorten
    und Gegenständen. Es bietet Funktionen zum Hinzufügen von Gegenständen,
    Auflisten aller Gegenstände, Suchen nach Gegenständen, Anzeigen einer
    Übersicht der Lagerorte, Aktualisieren von Gegenstandseigenschaften
    und Erstellen von Backups des Inventars.
"""
__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

from datetime import datetime
from copy import deepcopy
from pprint import pprint

def add_item_to_storage(inventory, storage, item):
    """Fügt einen Gegenstand zu einem Lagerort im Inventar hinzu.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.
        storage (str): Der Lagerort, zu dem der Gegenstand hinzugefügt werden soll.
        item (str): Der hinzuzufügende Gegenstand.

    Returns:
        dict: Das aktualisierte Inventar.
    """
    if storage in inventory:
        inventory[storage].update({item: {}})
    else:
        inventory.update({storage: {item : {}}})
    return inventory

def list_all_items(inventory):
    """Gibt eine sortierte Liste aller Gegenstände im Inventar zurück.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.

    Returns:
        list: Eine sortierte Liste aller Gegenstände im Inventar.
    """
    all_items = []
    for items in inventory.values():
        all_items.extend(items)
    return sorted(all_items)

def search_item(inventory, item):
    """Sucht nach einem Gegenstand im Inventar und gibt den Lagerort zurück.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.
        item (str): Der zu suchende Gegenstand.

    Returns:
        str or None: Der Lagerort des Gegenstands oder None, wenn nicht gefunden.
    """
    storage_places = []
    for storage, items in inventory.items():
        if item in items:
            storage_places.append(storage)

    if storage_places:
        return storage_places
    return None

def overview_storage(inventory, storages):
    """Gibt eine Übersicht der Lagerorte und deren Gegenstände zurück.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.
        storages (list): Eine Liste von Lagerorten, für die die Übersicht erstellt werden soll.

    Returns:
        dict: Ein Dictionary mit Lagerorten als Schlüssel und
        sortierten Listen von Gegenständen als Werten.
    """
    overview = {}
    for storage in storages:
        if storage in inventory:
            for item in inventory[storage]:
                overview = add_item_to_storage(overview, storage, item)
        else:
            overview.update({storage : {"Location not found in Inventory"}})

    return overview

def update_item_property(inventory, storage, item, property_key, property_value):
    """Aktualisiert eine Eigenschaft eines Gegenstands im Inventar.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.
        storage (str): Der Lagerort des Gegenstands.
        item (str): Der Gegenstand, dessen Eigenschaft aktualisiert werden soll.
        property_key (str): Der Schlüssel der zu aktualisierenden Eigenschaft.
        property_value: Der neue Wert der Eigenschaft.

    Returns:
        dict: Das aktualisierte Inventar.
    """
    if storage in inventory and item in inventory[storage]:
        inventory[storage][item][property_key] = property_value
    return inventory

def demonstrate_shallow_copy_effect():
    """
        Demonstriert die Auswirkungen einer flachen Kopie auf verschachtelte Strukturen.
    """
    original = {
        "keller": {
            "box": {"color": "brown"},
            "lamp": {"watt": 60}
        }
    }

    print("\nOriginal:")
    pprint(original)

    # flache Kopie erzeugen
    shallow = original.copy()

    print("\nShallow Copy:")
    pprint(shallow)

    # Jetzt eine verschachtelte Eigenschaft ändern
    print("\nÄndere 'box.color' in der shallow copy...")
    shallow["keller"]["box"]["color"] = "red"

    print("\nOriginal NACH Änderung:")
    pprint(original)

    print("\nShallow Copy NACH Änderung:")
    pprint(shallow)


def create_backup(inventory):
    """Erstellt ein Backup des Inventars.

    Args:
        inventory (dict): Das Inventar mit Lagerorten als Schlüssel
        und Listen von Gegenständen als Werten.

    Returns:
        dict: Eine Kopie des Inventars.
    """
    return deepcopy(inventory), datetime.now()

def test_all_methods():
    """
        Testet alle Methoden des Inventarsystems.
    """
    test_inventory = {
        "keller": {
            "box": {},
            "lamp": {}
        },
        "garage": {
            "car": {},
            "bike": {}
        }
    }
    print("-----Test all methods-----")
    print("Initial Inventory:")
    pprint(test_inventory)
    updated_inventory = add_item_to_storage(test_inventory, "wohnzimmer", "chair")
    updated_inventory = add_item_to_storage(updated_inventory, "garage", "chair")
    print("\nUpdated Inventory:")
    pprint(updated_inventory)
    print("\nList all items:")
    pprint(list_all_items(updated_inventory))
    print("\nSearch for 'chair")
    pprint(search_item(updated_inventory, "chair"))
    print("\nOverview of 'keller' and 'wohnzimmer':")
    pprint(overview_storage(updated_inventory, ["keller", "wohnzimmer"]))
    updated_inventory = update_item_property(updated_inventory, "wohnzimmer", "chair", "color", "red")
    print("\nUpdated Inventory after property update:")
    pprint(updated_inventory)
    print("----- Finished -----")

if __name__ == '__main__':
    #test_all_methods()
    demonstrate_shallow_copy_effect()
