import flet as ft

def main(page: ft.Page):

    table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Name")),
            ft.DataColumn(label=ft.Text("Age"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Tom")),
                    ft.DataCell(ft.Text("25"))
                ]
            )
        ]
    )

    page.add(table)

ft.run(main, view=ft.AppView.WEB_BROWSER)