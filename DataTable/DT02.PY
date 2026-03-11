import flet as ft

def main(page: ft.Page):
  page.add(
            ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("이름")),
                ft.DataColumn(ft.Text("나이")),
            ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Tom")),
                    ft.DataCell(ft.Text("25"))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Jane")),
                    ft.DataCell(ft.Text("30"))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Mike")),
                    ft.DataCell(ft.Text("28"))
                ]
            )
        ]
    )
  )
ft.app(main)