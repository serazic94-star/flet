import flet as ft

def main(page: ft.Page):

    text = ft.Text("즐겨찾기")

    def star_click(e):
        text.value = "클릭됨"
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.STAR,
                    on_click=star_click
                ),
                text
            ]
        )
    )

ft.app(main)