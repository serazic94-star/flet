import flet as ft

def main(page: ft.Page):

    def like_click(e):
        print("좋아요 클릭")

    def star_click(e):
        print("즐겨찾기 클릭")

    def settings_click(e):
        print("설정 클릭")

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                  ft.IconButton(
                    icon=ft.Icons.FAVORITE, on_click=like_click),
                    ft.Text("좋아요")
                    ]
                ),
                ft.Row(
                    controls=[
                  ft.IconButton(
                    icon=ft.Icons.STAR, on_click=star_click),
                    ft.Text("즐겨찾기")
                    ]
                ),
                ft.Row(
                    controls=[
                  ft.IconButton(
                    icon=ft.Icons.SETTINGS, on_click=settings_click),
                    ft.Text("설정")
                    ]
                ),
            ]
        )
    )

ft.app(main)