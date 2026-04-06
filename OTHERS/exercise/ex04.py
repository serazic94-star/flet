import flet as ft

def main(page: ft.Page):

    name = ft.TextField(label="이름")
    result = ft.Text("")

    def click(e):
        result.value = name.value
        page.update()

    page.add(
        name,
        ft.ElevatedButton("확인", on_click=click),
        result
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)