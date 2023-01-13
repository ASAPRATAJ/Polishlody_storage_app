from kivy.core.window import Window

from helpers import DemoApp
from helpers import AddName
from helpers import MenuScreen
from helpers import AddValue
from helpers import SubtractValue
from helpers import ShowRecords
from helpers import DeleteName

Window.size = (300, 500)

if __name__ == '__main__':
    DemoApp().run()

    menu_screen = MenuScreen()

    add_name = AddName()
    add_name.add_product_name()

    add_value = AddValue()
    add_value.add_product_value()

    subtract_value = SubtractValue()
    subtract_value.subtract_product_value()

    show_records = ShowRecords()
    show_records.on_enter()
    show_records.on_leave()

    delete_name = DeleteName()
    delete_name.delete_product_name()
