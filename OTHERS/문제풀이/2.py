import flet as ft

def main(page: ft.Page):
  page.add(
      ft.Row(
    controls=[
      ft.Text("Hello"),
      ft.Text("World")
    ]
  )
)
ft.app(main)