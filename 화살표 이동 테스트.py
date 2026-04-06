import flet as ft


def main(page: ft.Page):
    page.title = "추천 사료 화살표 기능만 테스트"
    page.padding = 20

    # ✅ 추천 사료 관련 함수
    # 추천사료 1개를 보여주는 작은 이미지 박스 함수
    def recommend_menu_box(image_src):
        return ft.Container(
            width=72,
            height=72,
            padding=0,
            margin=0,
            content=ft.Image(
                src=image_src,
                fit=ft.BoxFit.CONTAIN,
            ),
        )

    # ✅ 추천 사료 관련 변수
    # 추천 사료 이미지들을 페이지 단위로 저장한 2차원 리스트
    # 0번 페이지, 1번 페이지, 2번 페이지처럼 나뉘어 있음
    recommended_pages = [
        ["raw.png", "raw.png", "raw.png"],
        ["시저.png", "시저.png", "시저.png"],
        ["시저2.png", "시저2.png", "시저2.png"],
    ]

    # ✅ 상태값처럼 쓰이는 변수
    # 현재 몇 번째 추천사료 페이지를 보고 있는지 저장하는 값
    current_recommend_index = 0

    # ✅ 추천 사료 관련 함수
    # 현재 index에 맞는 추천 사료 3개를 한 줄(Row)로 만드는 함수
    def build_recommend_menu(index):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,
            controls=[
                recommend_menu_box(image_src)
                for image_src in recommended_pages[index]
            ],
        )

    # ✅ 추천 사료 관련 변수 / UI 구성 요소
    # 추천사료 가운데 실제 내용이 들어가는 컨테이너
    # 처음에는 current_recommend_index 값에 맞는 첫 페이지가 들어감
    recommend_content = ft.Container(
        content=build_recommend_menu(current_recommend_index)
    )

    # ✅ 추천 사료 관련 함수
    # 왼쪽 화살표 클릭 시 이전 추천 페이지로 이동하는 함수
    def show_prev_recommend(e):
        nonlocal current_recommend_index
        if current_recommend_index > 0:
            current_recommend_index -= 1  # ✅ 현재 추천 페이지 번호를 1 감소
            recommend_content.content = build_recommend_menu(current_recommend_index)  # ✅ 바뀐 index에 맞게 추천 영역 다시 생성
            page.update()  # ✅ 화면 갱신

    # ✅ 추천 사료 관련 함수
    # 오른쪽 화살표 클릭 시 다음 추천 페이지로 이동하는 함수
    def show_next_recommend(e):
        nonlocal current_recommend_index
        if current_recommend_index < len(recommended_pages) - 1:
            current_recommend_index += 1  # ✅ 현재 추천 페이지 번호를 1 증가
            recommend_content.content = build_recommend_menu(current_recommend_index)  # ✅ 바뀐 index에 맞게 추천 영역 다시 생성
            page.update()  # ✅ 화면 갱신

    # ✅ 기능 테스트용 최소 UI
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "추천사료",  # ✅ 추천사료 제목 텍스트
                    size=20,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Container(
                    width=350,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.Container(
                                width=36,  # ✅ 왼쪽 화살표 자리 고정폭
                                alignment=ft.Alignment(0, 0),
                                content=ft.IconButton(
                                    icon=ft.Icons.CHEVRON_LEFT,  # ✅ 이전 추천 페이지로 가는 왼쪽 화살표 버튼
                                    icon_color=ft.Colors.RED,
                                    on_click=show_prev_recommend,  # ✅ 클릭 시 show_prev_recommend 실행
                                ),
                            ),
                            ft.Container(
                                expand=True,
                                alignment=ft.Alignment(0, 0),
                                content=recommend_content,  # ✅ 추천사료 목록이 실제로 표시되는 가운데 영역
                            ),
                            ft.Container(
                                width=36,  # ✅ 오른쪽 화살표 자리 고정폭
                                alignment=ft.Alignment(0, 0),
                                content=ft.IconButton(
                                    icon=ft.Icons.CHEVRON_RIGHT,  # ✅ 다음 추천 페이지로 가는 오른쪽 화살표 버튼
                                    icon_color=ft.Colors.RED,
                                    on_click=show_next_recommend,  # ✅ 클릭 시 show_next_recommend 실행
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )