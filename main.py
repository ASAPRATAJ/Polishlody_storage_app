from kivy.core.window import Window

from helpers import DemoApp
from helpers import ProductName
from helpers import MenuScreen
from helpers import ProductValue
from helpers import ShowRecords

Window.size = (1200, 800)

if __name__ == '__main__':
    DemoApp().run()

    menu_screen = MenuScreen()

    product_name = ProductName()

    product_value = ProductValue()

    show_records = ShowRecords()


