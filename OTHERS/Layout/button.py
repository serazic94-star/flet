import flet as ft

def main(page: ft.Page):

    text = ft.Text("Hello")

    def click(e):
        text.value = "Clicked"
        page.update()

    page.add(
        text,
        ft.ElevatedButton("Click", on_click=click)
    )

ft.app(main)