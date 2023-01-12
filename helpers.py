navigation_helper = """
ScreenManager:
    MenuScreen:
    AddName:
    AddValue:
    SubtractValue:
    ShowRecords:
    DeleteName:

<MenuScreen>
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Dodaj nazwę'
        pos_hint: {'center_x':0.5, 'center_y':0.9}
        on_press: root.manager.current = 'add_name'
    MDRectangleFlatButton:
        text: 'Dodaj wartość'
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        on_press: root.manager.current = 'add_value'
    MDRectangleFlatButton:
        text: 'Odejmij wartość'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'subtract_value'
    MDRectangleFlatButton:
        text: 'Wyświetl produkty'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.manager.current = 'show_records'
        on_release: root.show_records()
    MDRectangleFlatButton:
        text: 'Usuń nazwę produktu'
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        on_release: root.manager.current = 'delete_product_name'

<AddName>
    name: 'add_name'
    MDTextField:
        id: product_name
        hint_text: "Podaj nazwę produktu"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        size_hint_x: None
        width: 300
    MDRectangleFlatButton:
        text: 'Dodaj'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.add_product_name()
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<AddValue>
    name: 'add_value'
    MDTextField:
        id: product_name
        hint_text: 'Podaj nazwę produktu'
        pos_hint: {'center_x': 0.4, 'center_y': 0.9}
        size_hint_x: None
        width: 300
    MDTextField:
        id: product_value
        hint_text: 'Podaj wartość produktu'
        pos_hint: {'center_x': 0.4, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDRectangleFlatButton:
        text: 'Dodaj'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.add_product_value()
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<SubtractValue>
    name: 'subtract_value'
    MDTextField:
        id: product_name
        hint_text: 'Podaj nazwę produktu'
        pos_hint: {'center_x': 0.4, 'center_y': 0.9}
        size_hint_x: None
        width: 300
    MDTextField:
        id: product_value
        hint_text: 'Podaj wartość produktu'
        pos_hint: {'center_x': 0.4, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDRectangleFlatButton:
        text: 'Odejmij'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.subtract_product_value()
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

<ShowRecords>
    name: 'show_records'
    screen: screen
    Screen:
        id: screen

    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.85, 'center_y':0.95}
        on_release: root.manager.current = 'menu'

<DeleteName>
    name: 'delete_product_name'
    MDTextField:
        id: delete_product_name
        hint_text: "Podaj nazwę produktu"
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        size_hint_x: None
        width: 300
    MDRectangleFlatButton:
        text: 'Usuń'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.delete_product_name()
    MDRectangleFlatButton:
        text: 'back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

"""