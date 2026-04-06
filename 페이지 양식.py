import flet as ft

def custom_appbar(title="중앙 텍스트"):
    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=48),  # 왼쪽 빈자리
                ft.Text(title, size=20, weight=ft.FontWeight.W_500,color=ft.Colors.BLACK),
                ft.Row(
                    spacing=8,
                    controls=[
                        ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
                        ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK,),
                    ],
                ),
            ],
        ),
    )

      
def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=70,
        border_radius=16,
        bgcolor=ft.Colors.YELLOW_700 if selected else ft.Colors.YELLOW_600,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),  # ✅ 수정
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Icon(
                    icon,
                    color=ft.Colors.BLACK,
                    size=24,
                ),
                ft.Text(
                    label,
                    color=ft.Colors.BLACK,
                    size=12,
                    weight=ft.FontWeight.W_500,
                ),
            ],
        ),
    )


def custom_navbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.Container(
        bgcolor=ft.Colors.YELLOW_600,
        padding=ft.Padding.symmetric(horizontal=12, vertical=8),  # ✅ 수정
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                nav_item(
                    icon,
                    label,
                    selected=(i == selected_index),
                    on_click=(lambda e, idx=i: on_tab_change(idx) if on_tab_change else None),
                )
                for i, (icon, label) in enumerate(items)
            ],
        ),
    )

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT

    # AppBar
    page.appbar = None
  
    
    def change_tab(index):
        print("선택된 탭:", index)

    page.add(
        ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, 1),
                end=ft.Alignment(0, -1),
                colors=[
                    ft.Colors.WHITE,
                    ft.Colors.WHITE,
                    ft.Colors.YELLOW,
                ],
            ),
            content=ft.SafeArea(
                expand=True,
                content=ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        custom_appbar("홈"),
                        ft.Container(
                            expand=True,
                            padding=20,
                            content=ft.Column(
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Container(height=100, bgcolor=ft.Colors.WHITE),
                                    ft.Container(height=100, bgcolor=ft.Colors.WHITE),
                                    ft.Container(height=100, bgcolor=ft.Colors.WHITE),
                                ],
                            ),
                        ),
                        custom_navbar(
                            selected_index=0,
                            on_tab_change=change_tab,
                        ),
                    ],
                ),
            ),
        )
    )
       
  


if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )