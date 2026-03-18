import flet as ft

def main(page: ft.Page):

    dropdown = ft.Dropdown(
        label="과일",
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도")
        ]
    )

    dlg = ft.AlertDialog(title=ft.Text("선택 결과"))

    def show(e):
        dlg.content = ft.Text(f"{dropdown.value} 선택됨")
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        dropdown,
        ft.ElevatedButton("확인", on_click=show)
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)