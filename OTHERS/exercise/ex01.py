import flet as ft

def main(page: ft.Page):

    input = ft.TextField(label="메시지 입력")
    result = ft.Text()

    def show(e):
        result.value = input.value
        page.update()

    page.add(
        input,
        ft.ElevatedButton("출력", on_click=show),
        result
    )

ft.app(main)