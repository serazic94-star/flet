import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            bgcolor="yellow",
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text("사과"),
                    ft.Text("바나나"),
                    ft.Text("포도")
                ]
            )
        )
    )
    

ft.app(main)