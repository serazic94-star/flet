import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C")
            ]
        )
    )

ft.app(main)