import flet as ft

def main(page: ft.Page):

    number = ft.Text("0")

    def plus_click(e):
        number.value = str(int(number.value) + 1)
        page.update()

    def reset_click(e):
        number.value = "0"
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.STAR,
                            on_click=plus_click
                        ),
                        number
                    ]
                ),
                ft.ElevatedButton(
                    "RESET",
                    on_click=reset_click
                )
            ]
        )
    )

ft.app(main)