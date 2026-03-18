import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            bgcolor="ivory",
            padding=200,
            content=ft.Column(
                controls=[
                    ft.Text("로그인"),
                    ft.TextField(label="아이디"),
                    ft.TextField(label="비밀번호"),
                    ft.ElevatedButton("확인")
                ]
            )
        )
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)