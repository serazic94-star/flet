import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text("사용자1")
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text("사용자2")
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text("사용자3")
                )
            ]
        )
    )

ft.app(main)