import flet as ft

def main(page: ft.Page):
    page.title = "Step 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    line = ft.Row(
        controls=[
            ft.Text("Host"),
            ft.TextField(width=150),
        ]
    )

    page.add(line)

ft.app(target=main)

if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )