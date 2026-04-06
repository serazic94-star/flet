import flet as ft

def main(page: ft.Page):

    listview = ft.ListView()

    for i in range(20):
        listview.controls.append(
            ft.Text(f"Item {i}")
        )

    page.add(listview)

ft.app(main)