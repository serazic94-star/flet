import flet as ft

def main(page: ft.Page):
  page.appbar = ft.AppBar(
    title=ft.Text("홈"),
    center_title=True
)
  
  page.add(ft.Text("본문 내용"))

ft.app(main)