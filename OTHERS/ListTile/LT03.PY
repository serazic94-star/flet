import flet as ft

def main(page: ft.Page):
  page.add(
    ft.ListTile(
      leading=ft.Icon(ft.Icons.PERSON),
      title=ft.Text("민서우"),
    trailing=ft.Icon(ft.Icons.ARROW_FORWARD)
  )
)
ft.run(main, view=ft.AppView.WEB_BROWSER)