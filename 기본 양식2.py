import datetime
import calendar
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
                    width=56,
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


def custom_bottom_appbar(selected_index=0, on_tab_change=None):
    items = [
        (ft.Icons.HOME, "Home"),
        (ft.Icons.EDIT_NOTE, "Log"),
        (ft.Icons.MENU_BOOK, "Contents"),
        (ft.Icons.PERSON, "MyPage"),
    ]

    return ft.BottomAppBar(
        bgcolor=ft.Colors.YELLOW,
        shape=ft.CircularRectangleNotchShape(),
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
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.TRANSPARENT
    page.appbar = None

    def change_tab(index):
        print("선택된 탭:", index)

    pagelet = ft.Pagelet(
        expand=True,
        content=ft.Container(),
        bgcolor=ft.Colors.YELLOW,
    )

    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.PETS, color=ft.Colors.YELLOW_700, size=34),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )

    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )

    dropdown = ft.Dropdown(
        label="문대추",
        width=320,
        border=ft.InputBorder.NONE,
        content_padding=10,
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ],
    )

    # -------------------------
    # 인라인 달력 상태
    # -------------------------
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    selected_date = today

    calendar_container = ft.Container()

    def month_title(year, month):
        return datetime.date(year, month, 1).strftime("%B %Y")

    def select_day(day):
        nonlocal selected_date
        selected_date = datetime.date(current_year, current_month, day)
        build_calendar()

    def prev_month(e):
        nonlocal current_year, current_month
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        build_calendar()

    def next_month(e):
        nonlocal current_year, current_month
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        build_calendar()

    def day_cell(day):
        if day == 0:
            return ft.Container(
                width=40,
                height=40,
            )

        is_selected = (
            selected_date.year == current_year
            and selected_date.month == current_month
            and selected_date.day == day
        )

        return ft.Container(
            width=40,
            height=40,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, d=day: select_day(d),
            content=ft.Container(
                width=28,   # 선택된 날짜 원 크기
                height=28,
                border_radius=14,
                bgcolor=ft.Colors.YELLOW if is_selected else None,
                alignment=ft.Alignment(0, 0),
                content=ft.Text(
                    str(day),
                    size=14,
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500,
                ),
            ),
        )

    def build_calendar():
        cal = calendar.Calendar(firstweekday=6)  # 일요일 시작
        month_days = cal.monthdayscalendar(current_year, current_month)

        cell_width = 40
        calendar_width = cell_width * 7
        weekday_names = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        weekday_row = ft.Row(
            width=calendar_width,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    width=cell_width,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Text(
                        name,
                        size=11,
                        color=ft.Colors.GREY_500,
                    ),
                )
                for name in weekday_names
            ],
        )

        week_rows = [
            ft.Row(
                width=calendar_width,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[day_cell(day) for day in week],
            )
            for week in month_days
        ]

        calendar_container.content = ft.Container(
            width=350,
            bgcolor=ft.Colors.WHITE,
            border_radius=30,
            padding=ft.padding.only(left=20, right=20, top=18, bottom=18),
            content=ft.Column(
                tight=True,
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                month_title(current_year, current_month),
                                size=17,
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_LEFT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=prev_month,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_RIGHT,
                                        icon_size=18,
                                        icon_color=ft.Colors.GREY_700,
                                        style=ft.ButtonStyle(
                                            padding=4,
                                        ),
                                        on_click=next_month,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    weekday_row,
                    ft.Column(
                        tight=True,
                        spacing=8,
                        controls=week_rows,
                    ),
                ],
            ),
        )

        page.update()

    # 처음 화면에 달력 1회 생성
    build_calendar()

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
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    custom_appbar("LOG"),
                    ft.Container(height=12),  # 드롭다운 위 여백
                    ft.Container(
                        width=350,
                        height=60,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.border.all(1, ft.Colors.GREY_300),
                        border_radius=10,
                        padding=ft.padding.symmetric(horizontal=10),
                        alignment=ft.Alignment(0, 0),
                        content=dropdown,
                    ),
                    ft.Container(height=2),  # 드롭다운과 달력 사이 간격
                    calendar_container,
                ],
            ),
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