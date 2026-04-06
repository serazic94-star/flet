import flet as ft

def main(page: ft.Page):

    number = ft.Text("0")

    def plus_click(e):
        number.value = str(int(number.value) + 1)
        page.update()

    def minus_click(e):
        number.value = str(int(number.value) - 1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.REMOVE,
                    on_click=minus_click
                ),
                number,
                ft.IconButton(
                    icon=ft.Icons.ADD,
                    on_click=plus_click
                )
            ]
        )
    )

ft.app(main)