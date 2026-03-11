import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Text("Hello Card"),
                padding=20
            )
        )
    )

ft.app(main)