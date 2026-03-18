import flet as ft

def main(page: ft.Page):

    text = ft.Text("Hello")

    def click(e):
        text.value = "Clicked"
        page.update()

    page.add(
        ft.Column(
            controls=[
                text,
                ft.ElevatedButton("눌러봐", on_click=click)
            ]
        )
    )

ft.app(main)