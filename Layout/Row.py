import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[
                ft.Container(width=50, height=50, bgcolor="red"),
                ft.Container(width=50, height=50, bgcolor="blue"),
                ft.Container(width=50, height=50, bgcolor="green")
            ]
        )
    )

ft.app(main)