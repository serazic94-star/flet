import flet as ft

def main(page: ft.Page):
  page.add(
      ft.Card(
          content=ft.ListTile(
              leading=ft.Icon(ft.Icons.PERSON),
              title=ft.Text("민서우"),
              subtitle=ft.Text("관리자")
          )
      )
  )
ft.app(main)