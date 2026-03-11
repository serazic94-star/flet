import flet as ft

def main(page: ft.Page):

    def click(e):
        print("클릭됨")

    page.add(
        ft.ListTile(
            title=ft.Text("사용자"),
            on_click=click
        )
    )

ft.app(main)