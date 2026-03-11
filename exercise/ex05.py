import flet as ft

def main(page: ft.Page):

    page.add(
        ft.Card(
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    controls=[
                        ft.Text("사용자 정보", size=20),
                        ft.Text("이름: 민서우"),
                        ft.Text("나이: 25"),
                        ft.ElevatedButton("상세보기")
                    ]
                )
            )
        )
    )

ft.app(main)