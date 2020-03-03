from Menu import Menu


if __name__ == "__main__":
    print(f'Menu is a class object: {Menu}.')

    new_menu = Menu()

    print(f'After assigning new_menu to a Menu class, new_menu becomes an \
object of a Menu class: {new_menu}.')

    print(f'Command "dir" returns a list if all methods and attributes \
of the class: {dir(Menu)}.')

    print(f'__init__ is a class method: {new_menu.__init__}.')
    print(f'__init__() returns: {new_menu.__init__()}.')

    print(f'__str__ is a class method: {new_menu.__str__}.')
    print('__str__() returns text if given.')

    print(f'show_notes is a class method: {new_menu.show_notes}.')
