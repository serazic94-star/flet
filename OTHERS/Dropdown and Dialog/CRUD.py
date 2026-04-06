import flet as ft

def main(page: ft.Page):

    name_input = ft.TextField(label="이름 입력")
    listview = ft.ListView(expand=True)

    def add_user(e):
        listview.controls.append(
            ft.ListTile(title=ft.Text(name_input.value))
        )
        name_input.value = ""
        page.update()

    page.add(
        name_input,
        ft.ElevatedButton("추가", on_click=add_user),
        listview
    )

ft.app(main)