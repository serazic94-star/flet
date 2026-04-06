import flet as ft

def main(page: ft.Page):
  page.navigation_bar = ft.NavigationBar(
      destinations=[
          ft.NavigationBarDestination(icon=ft.Icons.HOME, label="홈"),
          ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="검색"),
          ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="내정보"),
      ]
  )

  page.add(ft.Text("본문 내용"))
ft.app(main)