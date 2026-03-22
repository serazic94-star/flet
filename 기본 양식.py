import flet as ft

def custom_appbar(title="중앙 텍스트"):
    right_icons = ft.Row(
        spacing=8,
        controls=[
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.BLACK),
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.BLACK),
        ],
    )

    return ft.Container(
        height=60,
        padding=ft.padding.symmetric(horizontal=16),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=56),  # 왼쪽 빈자리
                ft.Text(
                    title,
                    size=20,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    width=56,   # 오른쪽 아이콘 자리와 비슷하게 맞춤
                    content=right_icons,
                    alignment=ft.Alignment(1, 0),
                ),
            ],
        ),
    )

def nav_item(icon, label, selected=False, on_click=None):
    return ft.Container(
        expand=True,
        height=70,
        on_click=on_click,
        alignment=ft.Alignment(0, 0),
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


# ✅ 수정: custom_navbar를 BottomAppBar용 내용으로 바꿈
def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),  # ✅ 가운데 홈(파인 부분) 생성
        content=ft.Row(
            spacing=8,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
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
    page.appbar = None

    def change_tab(index):
        print("선택된 탭:", index)

    # ✅ 추가: Pagelet 생성
    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),  # ✅ 필수
        bgcolor=ft.Colors.YELLOW,  # ✅ 이게 있으니까 검은 음영이 사라짐 
        )


    # ✅ 추가: 가운데 버튼
    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.PETS, color=ft.Colors.YELLOW_700, size=34),  # 개밥그릇 대신 우선 아이콘
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,  # ✅ 그림자 제거
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    # ✅ 추가: FAB 위치를 하단 중앙에 도킹
    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # ✅ 추가: 하단바를 BottomAppBar로 연결
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    # ✅ 기존 본문은 content로 유지
    pagelet.content = ft.Container(
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
    )

    page.add(pagelet)

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