import flet as ft

def main(page: ft.Page):
    page.title = "Step 3"
    page.window.width = 400
    page.window.height = 320
    page.window.resizable = False
    # page.window.center()  # ❌ 제거

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def label(text):
        return ft.Container(
            content=ft.Text(text),
            width=90,
            alignment=ft.Alignment(1, 0),  # ✅ 오른쪽 정렬
        )

    def field(password=False):
        return ft.TextField(
            width=160,
            height=40,
            password=password,
            can_reveal_password=password,
        )

    form = ft.Column(
        controls=[
            ft.Row([label("Database"), field()]),
            ft.Row([label("Host"), field()]),
            ft.Row([label("Port"), field()]),
            ft.Row([label("Username"), field()]),
            ft.Row([label("Password"), field(password=True)]),
            ft.Row(
                [ft.ElevatedButton("Connect", width=260)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=12,
    )

    page.add(form)

ft.run(main)  # ✅ 변경