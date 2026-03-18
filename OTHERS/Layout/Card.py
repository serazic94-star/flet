import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Icon(ft.Icons.PETS),
                    width=120,
                    height=120,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=60,
                    left=20,
                    top=20,
                ),

                ft.Container(
                    content=ft.Icon(ft.Icons.PETS),
                    width=120,
                    height=120,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=60,
                    left=160,
                    top=20,
                ),

                ft.Container(
                    content=ft.Icon(ft.Icons.PETS),
                    width=60,
                    height=60,
                    bgcolor=ft.Colors.GREY,
                    left=160,
                    top=160,
                ),

                ft.Container(
                    content=ft.Icon(ft.Icons.PETS),
                    width=60,
                    height=60,
                    bgcolor=ft.Colors.GREY,
                    left=230,
                    top=160,
                ),
            ]
        )
    )

ft.app(main)