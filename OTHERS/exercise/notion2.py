import flet as ft

def main(page: ft.Page):
    page.title = "Step 2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    form = ft.Column(
        controls=[
            ft.Row([ft.Text("Database"), ft.TextField(width=150)]),
            ft.Row([ft.Text("Host"), ft.TextField(width=150)]),
            ft.Row([ft.Text("Port"), ft.TextField(width=150)]),
        ]
    )

    page.add(form)

ft.app(target=main)