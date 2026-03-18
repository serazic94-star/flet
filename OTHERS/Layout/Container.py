import flet as ft

def main(page: ft.Page):
  ft.Container(
    content=ft.Text("hello"),
    bgcolor="blue",
    padding=10
)
  page.add(ft.Text("Hello, world!"))
  
ft.app(main)