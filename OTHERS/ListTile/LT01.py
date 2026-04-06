import flet as ft

def main(page: ft.Page):
    page.add(
        ft.ListTile(
            title=ft.Text("사용자"),
            subtitle=ft.Text("사용자 정보입니다")
        )
    )

ft.app(main)