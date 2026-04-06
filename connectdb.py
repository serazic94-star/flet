import flet as ft

def main(page: ft.Page):
    # 창 설정
    page.title = "DB Connect"
    page.window.width = 400
    page.window.height = 310
    page.window.resizable = False
    page.window.center()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Label ---
    db_name = ft.Text("Database")
    db_host = ft.Text("Host")
    db_port = ft.Text("Port")
    db_username = ft.Text("Username")
    db_password = ft.Text("Password")

    # --- Input ---
    db = ft.TextField(width=150, height=30, max_length=10, autofocus=True)
    host = ft.TextField(width=150, height=30, max_length=40)
    port = ft.TextField(width=150, height=30, max_length=6)
    username = ft.TextField(width=150, height=30, max_length=10)
    password = ft.TextField(width=150, height=30, max_length=20)

    # 비밀번호 옵션
    password.password = True
    password.can_reveal_password = True

    # --- Button ---
    connect = ft.ElevatedButton("Connect", width=230)

    # --- Layout ---
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Row([db_name, db]),
                        ft.Row([db_host, host]),
                        ft.Row([db_port, port]),
                        ft.Row([db_username, username]),
                        ft.Row([db_password, password]),
                        ft.Row([connect]),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)