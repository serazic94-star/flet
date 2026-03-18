import sys
import flet
from flet.controls.border_radius import horizontal
# ↑ 사실 이 horizontal 은 현재 코드에서 사용되지 않음
#   없어도 동작하는 불필요한 import


# =========================================================
# 참고용 명령어 / 메모
# =========================================================
# pip install watchfiles "flet==0.81.0"
# flet build apk --split-per-abi
# test address http://ip:port
# flet icon search page https://examples.flet.dev/icons_browser/


# =========================================================
# 공통 설정값 모음 클래스
# =========================================================
# 이 클래스는 "화면에서 반복해서 쓸 크기, 글자크기, 테두리" 등을
# 한 곳에 모아두는 역할을 함
# 쉽게 말해 "디자인 기본값 저장소"라고 보면 됨
class Default:
    # 실행 중인 운영체제에 따라 기본 화면 너비를 다르게 잡으려는 의도
    if sys.platform == "ios":
        view_width = 375
    elif sys.platform == "android" or "linux":
        # 주의:
        # 이 조건은 파이썬 문법상 사실상 항상 True처럼 동작할 가능성이 있음
        # 왜냐하면 "linux" 문자열 자체가 참으로 취급되기 때문
        # 원래 의도는:
        # elif sys.platform == "android" or sys.platform == "linux":
        view_width = 360
    elif sys.platform == "win32":  # Hot Reload Test
        view_width = 360
    else:
        view_width = 380

    # 프로필 이미지 크기
    image_size = view_width / 1.8  # width, height 둘 다 같은 정사각형

    # 섭취량 / 음수량 박스 크기
    data_width = view_width / 2.1
    data_height = data_width / 2

    # 기록 요약 박스 크기
    history_width = view_width
    history_height = view_width / 10

    # 오른쪽 세로 정보 박스들(이름, 상태, 나이) 크기
    side_width = view_width / 3
    side_height = view_width / 10

    # 아래쪽 6개 버튼 박스 크기
    tail_btn_size = view_width / 3.3  # width, height

    # 공통 텍스트 스타일
    text_size = 20
    text_weight = "bold"

    # 공통 테두리 스타일
    container_border = flet.border.all(color=flet.Colors.BLACK)


# =========================================================
# 재사용 가능한 UI 부품 함수들
# =========================================================
# 이 코드의 중요한 특징:
# "같은 모양의 박스"를 여러 번 쓰기 위해 함수로 빼놨음
# 그래서 main()에서는 길게 다 안 쓰고 간단히 조립만 하면 됨


def image_container(event, src: str, size=Default.image_size):
    """
    원형 프로필 이미지 컨테이너를 만들어주는 함수
    event: 클릭했을 때 실행할 함수
    src: 이미지 주소
    size: 가로/세로 크기
    """
    return flet.Container(
        width=size,
        height=size,
        bgcolor=flet.Colors.BLACK,
        shape=flet.BoxShape.CIRCLE,  # 컨테이너 자체를 원형으로 만듦
        on_click=event,
        image=flet.DecorationImage(
            src=src,
            fit=flet.BoxFit.COVER  # 이미지가 원을 꽉 채우도록 자르면서 채움
        ),
    )


def side_container(text, event, width=Default.side_width, height=Default.side_height):
    """
    오른쪽 세로 정보 박스(이름, 상태, 나이)를 만드는 함수
    """
    return flet.Container(
        content=flet.Text(text, size=Default.text_size, weight=Default.text_weight),
        alignment=flet.Alignment.CENTER,  # 박스 안에서 글자 가운데 정렬
        on_click=event,
        width=width,
        height=height,
        border_radius=10,
        border=Default.container_border,
    )


def data_container(text, event, width=Default.data_width, height=Default.data_height):
    """
    섭취량 / 음수량 같은 큰 데이터 박스를 만드는 함수
    내부에 Text + 작은 막대 모양 Container 가 들어있음
    """
    return flet.Container(
        width=width,
        height=height,
        padding=15,
        content=flet.Column(
            # 엄밀히 말하면 horizontal_alignment에는
            # CrossAxisAlignment 값을 넣는 게 일반적이지만,
            # 여기서는 가운데 정렬 의도로 작성된 코드라고 보면 됨
            horizontal_alignment=flet.MainAxisAlignment.CENTER,
            controls=[
                flet.Text(text, size=Default.text_size, weight=Default.text_weight),

                # 안쪽 작은 막대 박스
                # 나중에 진행률 표시, 수치 표시 영역 등으로 확장 가능
                flet.Container(
                    width=width / 1.5,
                    height=height / 10,
                    border_radius=10,
                    border=Default.container_border
                )
            ]
        ),
        alignment=flet.Alignment.CENTER,
        border_radius=10,
        on_click=event,
        border=Default.container_border,
    )


def history_container(text, event, width=Default.history_width, height=Default.history_height):
    """
    기록 요약 박스를 만드는 함수
    """
    return flet.Container(
        content=flet.Text(text, size=Default.text_size, weight=Default.text_weight),
        alignment=flet.Alignment.CENTER,
        on_click=event,
        width=width,
        height=height,
        border_radius=10,
        border=Default.container_border,
    )


def tail_btn_container(text, event, size=Default.tail_btn_size):
    """
    아래쪽 정사각형 기능 버튼(밥주기, 물주기 등)을 만드는 함수
    """
    return flet.Container(
        content=flet.Text(text, size=Default.text_size, weight=Default.text_weight),
        width=size,
        height=size,
        alignment=flet.Alignment.CENTER,
        on_click=event,
        border_radius=10,
        border=Default.container_border,
    )


# =========================================================
# 메인 함수
# =========================================================
# Flet 앱은 보통 main(page) 형태로 시작함
# page는 "전체 앱 화면"이라고 생각하면 됨
def main(page: flet.Page):
    # 현재 페이지 너비 출력
    print(page.width)

    # 화면 너비를 page 기준으로 다시 계산
    # page.width가 0이면 기본값 360 사용
    Default.view_width = page.width if page.width > 0 else 360

    # 너무 넓어지지 않도록 최대 너비를 360으로 제한
    if Default.view_width > 360:
        Default.view_width = 360

    print(Default.view_width)

    # 앱의 테마 모드: 시스템 설정(다크모드/라이트모드)에 따름
    page.theme_mode = flet.ThemeMode.SYSTEM

    # 페이지 전체 가로축 정렬
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    # -----------------------------------------------------
    # 공통 클릭 처리 함수
    # -----------------------------------------------------
    # 여러 버튼/박스를 눌렀을 때 콘솔에 무엇을 눌렀는지 출력하고
    # AppBar 제목도 바꾸는 역할
    def click_print(e, index=None):
        # index가 따로 전달되지 않으면
        # 네비게이션바 selected_index 값을 사용
        if not index:
            index = f"Nav Bar Page: {e.control.selected_index}"

        print(index)

        # appbar가 존재하면 제목을 바꿈
        # 현재 title이 TextButton("DogDog!") 이므로
        # title.content 에 문자열을 넣어 텍스트를 바꾸려는 의도
        if page.appbar.page:
            page.appbar.title.content = index

    # -----------------------------------------------------
    # 상단 앱바
    # -----------------------------------------------------
    page.appbar = flet.AppBar(
        leading=flet.IconButton(
            flet.Icons.MENU,
            on_click=lambda e: click_print(e, "Menu")
        ),  # 왼쪽 햄버거 메뉴 버튼

        title=flet.TextButton(
            "DogDog!",
            on_click=lambda e: click_print(e, "LOGO")
        ),  # 가운데 로고 버튼

        center_title=True,

        actions=[
            flet.IconButton(
                flet.Icons.SETTINGS,
                on_click=lambda e: click_print(e, "Settings")
            )
        ]  # 오른쪽 설정 버튼
    )

    # -----------------------------------------------------
    # 본문 화면 구성
    # -----------------------------------------------------
    # 전체 내용을 세로(Column)로 쌓아 만든 메인 영역
    test = flet.Column(
        scroll=flet.ScrollMode.AUTO,   # 내용이 길면 자동 스크롤
        horizontal_alignment=flet.MainAxisAlignment.CENTER,
        expand=True,
        controls=[
            # 맨 위 여백
            flet.Container(height=5),

            # -----------------------------
            # 1) 프로필 영역
            # 왼쪽: 원형 이미지
            # 오른쪽: 이름/상태/나이
            # -----------------------------
            flet.Row(
                controls=[
                    image_container(
                        event=lambda e: click_print(e, "Images"),
                        src="https://content.lyka.com.au/f/1016262/1104x676/e36872ce32/beagle.png"
                    ),
                    flet.Column(
                        horizontal_alignment=flet.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            side_container("뽀찌", event=lambda e: click_print(e, "이름")),
                            side_container("살쪘어요..", event=lambda e: click_print(e, "상태값")),
                            side_container("3짤", event=lambda e: click_print(e, "나이")),
                        ]
                    )
                ]
            ),

            flet.Container(height=10),

            # -----------------------------
            # 2) 요약 데이터 영역
            # 섭취량 / 음수량
            # -----------------------------
            flet.Row(
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    data_container(text="섭취량", event=lambda e: click_print(e, "섭취량")),
                    data_container(text="음수량", event=lambda e: click_print(e, "음수량")),
                ]
            ),

            # -----------------------------
            # 3) 기록 요약 영역
            # 현재는 예시로 운영체제 표시
            # -----------------------------
            flet.Row(
                alignment=flet.MainAxisAlignment.CENTER,
                controls=[
                    history_container(
                        text=f"OS: {sys.platform}",
                        event=lambda e: click_print(e, "기록요약")
                    ),
                ]
            ),

            flet.Container(height=10),

            # -----------------------------
            # 4) 빠른 기능 버튼 1행
            # -----------------------------
            flet.Row(
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    tail_btn_container(text="밥주기", event=lambda e: click_print(e, "밥주기")),
                    tail_btn_container(text="물주기", event=lambda e: click_print(e, "물주기")),
                    tail_btn_container(text="약먹이기", event=lambda e: click_print(e, "약먹이기")),
                ]
            ),

            # -----------------------------
            # 5) 빠른 기능 버튼 2행
            # -----------------------------
            flet.Row(
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    tail_btn_container(text="대소변기록", event=lambda e: click_print(e, "대소변기록")),
                    tail_btn_container(text="체중기록", event=lambda e: click_print(e, "체중기록")),
                    tail_btn_container(text="관찰기록", event=lambda e: click_print(e, "관찰기록")),
                ]
            ),
        ]
    )

    # -----------------------------------------------------
    # 본문을 감싸는 바깥쪽 Row
    # -----------------------------------------------------
    # 보통 "전체 콘텐츠 폭 제한" 용도로 감싸는 구조
    content = flet.Row(
        width=Default.view_width,
        expand=True,
        controls=[
            flet.Container(
                # bgcolor=flet.Colors.BROWN,  # 디버깅용 배경색 흔적
                expand=True,
                content=test
            ),
        ]
    )

    # -----------------------------------------------------
    # 플로팅 액션 버튼 (우하단 + 버튼)
    # -----------------------------------------------------
    page.floating_action_button = flet.FloatingActionButton(
        icon=flet.Icons.ADD,
        on_click=lambda _: print("Nyang!"),
    )

    # -----------------------------------------------------
    # 하단 네비게이션 바
    # -----------------------------------------------------
    page.navigation_bar = flet.NavigationBar(
        on_change=lambda e: click_print(e),
        destinations=[
            flet.NavigationBarDestination(label="Home", icon=flet.Icons.HOME),
            flet.NavigationBarDestination(label="log", icon=flet.Icons.HISTORY),
            flet.NavigationBarDestination(label="SHOP", icon=flet.Icons.SHOP),
            flet.NavigationBarDestination(label="AI", icon=flet.Icons.STARS_SHARP),
            flet.NavigationBarDestination(label="My Page", icon=flet.Icons.EMOJI_EMOTIONS),
        ]
    )

    # 최종적으로 페이지에 content 추가
    page.add(content)


# =========================================================
# 실행부
# =========================================================

# build test
# app name = project name
# if __name__ == "__main__":
#     flet.app(target=main, assets_dir="assets")

if __name__ == "__main__":
    import webbrowser, os

    # 특정 환경변수(FLET_NO_BROWSER)가 있으면 자동으로 브라우저 열지 않게 함
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None

    # 웹 브라우저 모드로 실행
    # assets_dir="assets" : 정적 파일 폴더
    # port=34636 : 접속 포트
    flet.app(
        target=main,
        assets_dir="assets",
        view=flet.AppView.WEB_BROWSER,
        port=34636
    )