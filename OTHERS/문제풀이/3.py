import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[
                ft.Icon(ft.Icons.FAVORITE),
                ft.Text("Hello")
            ]
        )
    )

ft.app(main)