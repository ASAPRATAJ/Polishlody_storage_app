import sqlite3
from sqlite3 import IntegrityError

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, TwoLineListItem

sql_connect = 'app_polish_storage.db'

sql_create_table = """CREATE TABLE if not exists storage(
                        product_name text UNIQUE,
                        product_value integer DEFAULT(0))"""

sql_insert = """INSERT INTO storage(product_name)VALUES(?)"""

sql_update_add = """UPDATE storage
                SET product_value=product_value+?
                WHERE product_name=?"""

sql_update_subtract = """UPDATE storage
                        SET product_value=product_value-?
                        WHERE product_name=?"""

sql_show_records = """SELECT * FROM storage"""

sql_delete_name = """DELETE FROM storage WHERE product_name=?"""


class AddName(Screen):
    def add_product_name(self):
        connection = sqlite3.connect(sql_connect)

        # Create cursor to operate in database
        cur = connection.cursor()
        # Check if user entered input properly
        if self.ids.product_name.text.isalpha():
            try:
                # Add product_name into product_name column
                cur.execute(sql_insert, (self.ids.product_name.text.lower(),))
                check_string = 'Dodano ' + self.ids.product_name.text
            except IntegrityError:
                check_string = 'Ta nazwa została już dodana'
        else:
            check_string = 'Proszę podać prawidłową nazwę'

        # Apply changes and close connection
        connection.commit()
        connection.close()

        # Clearing textfield
        self.ids.product_name.text = ''

        # Create an object of MDDialog which pops up
        dialog = MDDialog(text=check_string)
        dialog.open()


class MenuScreen(Screen):
    pass


class AddValue(Screen):
    def add_product_value(self):
        # Create connection to the database
        connection = sqlite3.connect(sql_connect)
        # Create cursor to operate in database
        cur = connection.cursor()

        if self.ids.product_value.text.isalnum() and self.ids.product_name.text.isalpha():
            # Add a value to specified product_name
            cur.execute(sql_update_add, (int(self.ids.product_value.text), self.ids.product_name.text.lower()))
            check_string = 'Dodano ' + self.ids.product_name.text
        else:
            check_string = 'Proszę podać prawidłową nazwę'

        # Apply changes and close connection
        connection.commit()
        connection.close()

        # Clearing textfield
        self.ids.product_name.text = ''
        self.ids.product_value.text = ''

        # Create an object of MDDialog which pops up
        dialog = MDDialog(text=check_string)
        dialog.open()


class SubtractValue(Screen):
    def subtract_product_value(self):
        # Create connection to the database
        connection = sqlite3.connect(sql_connect)
        # Create cursor to operate in database
        cur = connection.cursor()

        if self.ids.product_value.text.isalnum() and self.ids.product_name.text.isalpha():
            # Add a value to specified product_name
            cur.execute(sql_update_subtract, (int(self.ids.product_value.text),
                                              self.ids.product_name.text.lower()))
            check_string = 'Odjęto ' + self.ids.product_name.text
        else:
            check_string = 'Proszę podać prawidłową nazwę'
        # Apply changes and close connection
        connection.commit()
        connection.close()

        # Clearing textfield
        self.ids.product_name.text = ''
        self.ids.product_value.text = ''

        # Create an object of MDDialog which pops up
        dialog = MDDialog(text=check_string)
        dialog.open()


class ShowRecords(Screen):
    screen = ObjectProperty()

    def on_enter(self):
        # Create connection to the database
        connection = sqlite3.connect(sql_connect)
        # Create cursor to operate in database
        cur = connection.cursor()

        # Grabbing all the records and fetching them into variable records
        cur.execute(sql_show_records)
        records = cur.fetchall()

        # Sort a list of tuples in alphabetical order
        records.sort()

        # Create an object of ScrollView()
        scroll = ScrollView()

        # Create and object of MDlist()
        list_view = MDList()

        # Add a list_view as a widget to scroll object
        scroll.add_widget(list_view)

        # Get product names from tuples in records list
        product_names = [x[0] for x in records]

        # Get product_values from tuples in records list
        product_values = [x[1] for x in records]

        # Adding product_name and product_value to TwoLineListItem
        for item_number in range(len(product_names)):
            item = TwoLineListItem(text=str(product_names[item_number]),
                                   secondary_text=str(product_values[item_number]))

            list_view.add_widget(item)

        # Add scroll object with items to the screen object to be able to display it on the screen
        self.screen.add_widget(scroll)

    def on_leave(self, *args):
        self.screen.clear_widgets()


class DeleteName(Screen):
    def delete_product_name(self):
        # Create connection to the database
        connection = sqlite3.connect(sql_connect)
        # Create cursor to operate in database
        cur = connection.cursor()

        # Check if user entered input properly
        if self.ids.delete_product_name.text.isalpha():
            # Delete product_name from storage tabel
            cur.execute(sql_delete_name, (self.ids.delete_product_name.text.lower(),))
            check_string = 'Usunięto nazwę ' + self.ids.delete_product_name.text
        else:
            check_string = 'Proszę podać prawidłową nazwę'

        connection.commit()
        connection.close()

        # Clearing textfield
        self.ids.delete_product_name.text = ''

        # Create an object of MDDialog which pops up
        dialog = MDDialog(text=check_string)
        dialog.open()


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Brown'
        screen = Builder.load_file("config.kv")

        return screen

    def on_start(self):
        connection = sqlite3.connect(sql_connect)
        cur = connection.cursor()

        cur.execute(sql_create_table)
