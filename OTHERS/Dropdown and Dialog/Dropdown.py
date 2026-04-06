import flet as ft

def main(page: ft.Page):

    dropdown = ft.Dropdown(
        label="과일선택",
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도")
        ]
    )

    page.add(dropdown)

ft.run(main, view=ft.AppView.WEB_BROWSER)