import flet as ft

def main(page: ft.Page):

    number = ft.Text("0")

    def add_click(e):
        number.value = str(int(number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    on_click=add_click
                ),
                number
            ]
        )
    )

ft.app(main)