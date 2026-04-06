import flet as ft

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("홈"),
        bgcolor=ft.Colors.BLUE
    )

ft.app(main)