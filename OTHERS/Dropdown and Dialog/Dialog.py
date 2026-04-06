import flet as ft

def main(page: ft.Page):

    dlg = ft.AlertDialog(
        title=ft.Text("알림"),
        content=ft.Text("저장되었습니다")
    )

    def open_dialog(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton("저장", on_click=open_dialog)
    )

ft.run(main, view=ft.AppView.WEB_BROWSER)