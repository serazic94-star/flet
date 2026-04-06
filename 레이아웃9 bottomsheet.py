import flet as ft

def arrow_back(on_click=None):
      return ft.Container(
        width=float("inf"),  # 👉 전체 너비 차지
        alignment=ft.Alignment(-1, 0),  # 👉 왼쪽 정렬  # 👈 왼쪽 이동
        on_click=on_click,
        content=ft.Icon(ft.Icons.ARROW_BACK),
        )

def about_dog():
    return ft.Column(
        spacing=0,
        controls=[
            ft.Text("About your Dog", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=30),
            ft.Text("반려동물의 기본 정보를 입력하세요", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK, size=15),
        ],
    )

def long_box(text, bgcolor = ft.Colors.WHITE, text_color=ft.Colors.BLACK, on_click=None):
    return ft.Container(
        width=350,
        height=50,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
        padding=10,
        bgcolor=bgcolor,
        on_click=on_click,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, size=14, weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
            ],
        ),
    )

def input_box(label=None, hint_text=None):
    return ft.TextField(
        width=350,
        height=50,
        border_radius=10,
        border_color=ft.Colors.GREY_300,
        focused_border_color=ft.Colors.GREY_400,
        hint_text = hint_text,
        label=label,  # 선택적으로 라벨도 넣을 수 있음
    )

def bottom_continue_button(on_click=None):
    return ft.Container(
        alignment=ft.Alignment(0, 1),
        padding=ft.padding.only(bottom=20),
        content=long_box(
            "Continue",
            bgcolor=ft.Colors.YELLOW,
            text_color=ft.Colors.BLACK,
            on_click=on_click,
        ),
    )

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.title = "For Dog5"

       #주소 팁 닫기
    def close_tip(e=None):
      harim_bottom_tip_sheet.open = False
      page.update()

# 주소 팁 bottomsheet 정의하기
    harim_bottom_tip_sheet = ft.BottomSheet(
        # ✅ 뒤 배경 안 까맣게
        barrier_color=ft.Colors.TRANSPARENT,

        size_constraints=ft.BoxConstraints( # ✅ 높이를 크게
            max_height=700,   # 필요하면 450, 500으로 더 키워도 됨
            min_height=430,
        ),

      content=ft.Container(
          padding=20,
          content=ft.Column(
              tight=True,
            controls = [
                  ft.Text("사료 선택", size=25, weight='bold'),
                  ft.Divider(),
                  ft.Text("하림 가맛시"),
                  ft.Text("하림 가맛시"),
                  ft.Text("하림 가맛시"),
                  ft.Text("하림 가맛시"),
                  ft.Text("하림 가맛시"),
                  ft.Container(height=10),
            ],
          ),
      )
    )

    # 앱이 시작될때 bottomSheet을 띄우기
    def show_inital_tip(e=None):
      harim_bottom_tip_sheet.open = True
      page.update()



    body = ft.Container(
                      padding=ft.padding.only(top=0), # 🔥 (1) 전체 레이아웃을 아래로 내림 음수 제거
                      content=ft.Column(
                          width=350, # 🔥 (2) Column 자체의 너비를 고정
                          spacing=12, 
                          horizontal_alignment=ft.CrossAxisAlignment.START, # center를 start로 바꿈
                          scroll=ft.ScrollMode.AUTO,
                          controls=[
                              arrow_back(),
                              ft.Container(
                                  margin=ft.margin.only(top=50),
                                  content=about_dog(),
                              ),
                              ft.Text("현재 급여 중인 사료", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                              input_box("현재 급여 중인 사료를 적어주세요"),

                              ft.Text("현재 급여 중인 사료 잔여량", weight=ft.FontWeight.W_500, color=ft.Colors.BLACK),
                              input_box("현재 급여 중인 사료 잔여량을 적어주세요"),

                              bottom_continue_button(),
                          ],
                        ),
                      )
                  
              
  ### 페이지에 BottomSheet를 등록하기
    page.overlay.append(harim_bottom_tip_sheet)
    show_inital_tip()
    page.add(body) 



if __name__ == "__main__":
    import webbrowser
    import os

    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    ft.app(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )