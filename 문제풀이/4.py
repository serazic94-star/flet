import flet as ft

def main(page: ft.Page):

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.FAVORITE),
                        ft.Text("좋아요")
                    ]
                ),

                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.SETTINGS),
                        ft.Text("설정")
                    ]
                ),

                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.PERSON),
                        ft.Text("프로필")
                    ]
                )
            ]
        )
    )

ft.app(main)