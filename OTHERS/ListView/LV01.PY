import flet as ft

def main(page: ft.Page):
    page.add(
        ft.ListView(
            controls=[
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C")
            ]
        )
    )

ft.app(main)