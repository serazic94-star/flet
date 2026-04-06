import flet as ft

def main(page: ft.Page):

    def like_click(e):
        print("좋아요 클릭")

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.FAVORITE,
                    on_click=like_click
                ),
                ft.Text("좋아요")
            ]
        )
    )
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.STAR,
                    on_click=like_click
                ),
                ft.Text("즐겨찾기")
            ]
        )
    )
ft.app(main)