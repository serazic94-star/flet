import flet as ft

def main(page: ft.Page):

    page.add(
        ft.ListView(
            controls=[
                ft.ListTile(title=ft.Text("사용자1")),
                ft.ListTile(title=ft.Text("사용자2")),
                ft.ListTile(title=ft.Text("사용자3")),
                ft.ListTile(title=ft.Text("사용자4")),
                ft.ListTile(title=ft.Text("사용자5"))
            ]
        )
    )

ft.app(main)