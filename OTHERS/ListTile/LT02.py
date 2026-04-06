import flet as ft

def main(page: ft.Page):
  page.add(
    ft.ListTile(
      leading=ft.Icon(ft.Icons.PERSON),
      title=ft.Text("민서우"),
      subtitle=ft.Text("사용자")
)
)  
ft.app(main)