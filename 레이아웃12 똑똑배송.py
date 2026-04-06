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
def invisible_middle_box(image_src):
    return ft.Container(
        width=200,   # 👉 크게 키움 (원하는 값으로 조절)
        height=200,
        bgcolor=ft.Colors.TRANSPARENT,  # 👉 완전 투명
        border=None,  # 👉 테두리 없음
        border_radius=20,  # 👉 둥글게 (선택)
        alignment=ft.Alignment(0, 0),
        content=ft.Image(
            src=image_src,
            fit=ft.BoxFit.COVER,  # 👉 꽉 채우기
        ),
    )

def invisible_large_box(image_src):
    return ft.Container(
        width=400,   # 👉 가로 기준만 잡는다 (이미지 크기의 기준)
        # height 제거 ❗ → 비율 유지하려면 고정 높이 쓰면 안됨
        
        bgcolor=ft.Colors.TRANSPARENT,  # 👉 완전 투명 배경
        border=None,  # 👉 테두리 없음
        border_radius=20,  # 👉 둥글게 (필요 없으면 삭제 가능)

        # clip_behavior 추가해야 border_radius 적용됨
        clip_behavior=ft.ClipBehavior.HARD_EDGE,

        alignment=ft.Alignment(0, 0),

        content=ft.Image(
            src=image_src,

            # 👉 가로 기준으로 맞추고 세로는 자동으로 늘어남 (핵심)
            width=400,

            # 👉 비율 유지하면서 꽉 채움 (세로 잘릴 수 있음)
            fit=ft.BoxFit.FIT_WIDTH,
        ),
    )
def mid_box(text):
    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),  # 👉 더 큼
        bgcolor=ft.Colors.YELLOW_600,  
        border_radius=8,
        content=ft.Text(
            text,
            size=12,  # 👉 글자도 조금 키움
            weight=ft.FontWeight.W_500,
            color=ft.Colors.BLACK,
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


    pagelet.floating_action_button = ft.FloatingActionButton(
        content=ft.Container(
            width=60,   # 👉 버튼 안 영역 키움
            height=60,
            alignment=ft.Alignment(0, 0),
            content=ft.Image(
                src="bowlradius.png",
                fit=ft.BoxFit.CONTAIN,  # 👉 비율 유지
            ),
        ),
        bgcolor=ft.Colors.WHITE,
        shape=ft.CircleBorder(),
        elevation=0,
        on_click=lambda e: print("가운데 버튼 클릭"),
    )


    # ✅ 추가: FAB 위치를 하단 중앙에 도킹
    pagelet.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    # ✅ 추가: 하단바를 BottomAppBar로 연결
    pagelet.bottom_appbar = custom_bottom_appbar(
        selected_index=0,
        on_tab_change=change_tab,
    )


    def menu_box(image_src):
        return ft.Container(
            width=95,
            height=95,
            padding=0,
            margin=0,
            content=ft.Image(
                src=image_src,
                fit=ft.BoxFit.COVER,  # 꽉 채우기
            ),
        )
    def super_long_box(controls=None):
            return ft.Container(
                width=350,
                height=100,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,  # 왼쪽 정렬
                    controls=controls or [],  # 👉 리스트로 받기
                ),
            )
        
    def mini_box(text):
        return ft.Container(
            width=70,
            height=60,
            bgcolor=ft.Colors.YELLOW,
            border_radius=10,
            alignment=ft.Alignment(0, 0),  # ✅ 여기 수정
            content=ft.Text(
                text,
                size=18,
                weight=ft.FontWeight.W_700,
                color=ft.Colors.BLACK,
            ),
        )
        
    def micro_iconbox(icon_name):
        return ft.Container(
            padding=ft.Padding.symmetric(horizontal=8, vertical=4),
            bgcolor=ft.Colors.YELLOW_600,
            border_radius=6,
            content=ft.Icon(
                icon_name,
                size=16,
                color=ft.Colors.BLACK,
            ),
        )
    
    def record_card(date_text, title_text, info_list):
        return ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                mini_box(date_text),

                ft.Column(
                    spacing=6,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.Text("🔥"),
                                ft.Text(
                                    title_text,
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.Colors.BLACK,
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=6,
                            controls=[micro_box(info) for info in info_list],
                        ),
                    ],
                ),
            ],
        )
    
        
    menu_grid1 = ft.Column(
      spacing=14,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      controls=[
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
      ],
  )
    
    menu_grid2 = ft.Column(
      spacing=14,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      controls=[
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
          ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              spacing=14,
              controls=[
                  menu_box("raw.png"),
                  menu_box("raw.png"),
                  menu_box("raw.png"),
              ],
          ),
      ],
  )
    
    dropdown = ft.Dropdown(
        label="sort",
        width=320,
        border=ft.InputBorder.NONE,
        content_padding=10,
        options=[
            ft.dropdown.Option("사과"),
            ft.dropdown.Option("바나나"),
            ft.dropdown.Option("포도"),
        ],
    )

    # 주소 팁 bottomsheet 정의하기
    harim_bottom_tip_sheet = ft.BottomSheet(
      # ✅ 뒤 배경 안 까맣게
        barrier_color=ft.Colors.TRANSPARENT,

        # ✅ 바텀시트 자체 배경색
        bgcolor=ft.Colors.BLUE_ACCENT,

        size_constraints=ft.BoxConstraints( # ✅ 높이를 크게
            max_width=350,   # 필요하면 450, 500으로 더 키워도 됨
            max_height=100,
        ),

        content=ft.Container(
            height=200,  # ✅ 높이 고정 (여기 숫자로 위치 조절)
            padding=20,
            alignment=ft.Alignment(0, -1),  # 👈 위쪽으로 살짝 (0,-1 ~ 0,1 조절)

            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,  # 👈 위쪽 정렬
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("똑똑배송으로 주문하기", size=25, weight='bold'),
                ],
            ),
        ),
    )

    # 앱이 시작될때 bottomSheet을 띄우기
    def show_inital_tip(e=None):
      harim_bottom_tip_sheet.open = True
      page.update()

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
        content=ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    custom_appbar("개밥개밥푸드"),
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Container(
                                    height=100,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),  # 👈 중앙 정렬
                                    content=invisible_middle_box("product.jpg"),
                                ),  
                                ft.Container(
                                    height=50,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10,
                                        controls=[
                                            mid_box("바로구매"),
                                            mid_box("장바구니"),
                                            micro_iconbox(ft.Icons.FAVORITE)
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    width=350,
                                    height=60,
                                    border=ft.border.all(1, ft.Colors.BLUE_600),
                                    bgcolor=ft.Colors.BLUE_600,
                                    border_radius=10,
                                    padding=ft.padding.symmetric(horizontal=10),
                                    alignment=ft.Alignment(0, 0),
                                    content= ft.Text("똑똑 배송"),
                                ),
                                ft.Container(
                                    width=350,
                                    bgcolor=ft.Colors.WHITE,
                                    alignment=ft.Alignment(0, 0),  # 👈 중앙 정렬
                                    content=invisible_large_box("productpic1.jpg"),
                                ),
                                
                            ],
                        ),
                    ),
                ],
            ),
        ),
    )

      ### 페이지에 BottomSheet를 등록하기
    page.overlay.append(harim_bottom_tip_sheet)
    show_inital_tip() 

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