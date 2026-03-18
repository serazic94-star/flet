import flet as ft
import urllib.request
import urllib.parse
import json
import webbrowser
import asyncio

# 네가 캐낸 마스터키!
CLIENT_ID = "HLEBvq30Qitnio590Y_1"
CLIENT_SECRET = "XoAlGygeSa"

current_start = 1
scroll_pos = 0 

def get_naver_images(query, start_index):
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/image?query={encText}&display=50&start={start_index}&sort=sim"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            return [item['link'] for item in data['items']]
    except Exception as e:
        print(f"데이터 캐내기 실패: {e}")
    return []

async def main(page: ft.Page):
    global current_start, scroll_pos
    page.title = "✨ 무한 최애 갤러리 (진짜 최종!) ✨"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"

    # 스크롤바 테마
    page.scrollbar_theme = ft.ScrollbarTheme(
        thickness=12,
        radius=10,
        thumb_color={
            ft.ControlState.HOVERED: ft.Colors.BLUE_ACCENT,
            ft.ControlState.DEFAULT: ft.Colors.WHITE38,
        },
    )

    # 맨 위로 올리기 함수
    async def scroll_top(e):
        global scroll_pos
        scroll_pos = 0 
        await page.scroll_to(offset=0, duration=1000) 
        page.update()

    # 💡 에러 해결 지점: BOTTOM_LEFT 대신 START_FLOAT 사용!
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_UPWARD,
        bgcolor=ft.Colors.BLUE_700,
        on_click=scroll_top,
        tooltip="맨 위로 가기"
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.START_FLOAT

    # 키보드 스크롤 처리
    async def on_keyboard(e: ft.KeyboardEvent):
        global scroll_pos
        if e.key == "Arrow Down":
            scroll_pos += 300
        elif e.key == "Arrow Up":
            scroll_pos = max(0, scroll_pos - 300)
        
        await page.scroll_to(offset=scroll_pos, duration=300)
        page.update()

    page.on_keyboard_event = on_keyboard

    gallery = ft.GridView(
        expand=False, 
        runs_count=4, 
        max_extent=300, 
        child_aspect_ratio=0.7, 
        spacing=15,
        run_spacing=15,
    )

    def add_images_to_gallery(image_urls):
        for url in image_urls:
            gallery.controls.append(
                ft.Container(
                    content=ft.Image(
                        src=url,
                        fit="cover",
                        border_radius=ft.BorderRadius.all(12),
                        error_content=ft.Text("사진 없음😥", color="red")
                    ),
                    on_click=lambda e, link=url: webbrowser.open(link)
                )
            )
        page.update()

    async def search_click(e):
        global current_start, scroll_pos
        if not name_input.value:
            name_input.error_text = "이름을 입력해주세요!"
            page.update()
            return
        
        current_start = 1
        scroll_pos = 0 
        gallery.controls.clear()
        load_more_btn.visible = False
        page.update()
        
        query = f"{name_input.value} {event_dropdown.value}"
        image_urls = await asyncio.to_thread(get_naver_images, query, current_start)
        
        if image_urls:
            add_images_to_gallery(image_urls)
            load_more_btn.visible = True
            current_start += 50
        page.update()

    async def load_more_click(e):
        global current_start
        query = f"{name_input.value} {event_dropdown.value}"
        image_urls = await asyncio.to_thread(get_naver_images, query, current_start)
        
        if image_urls:
            add_images_to_gallery(image_urls)
            current_start += 50
            if current_start > 1000:
                load_more_btn.visible = False
        else:
            load_more_btn.visible = False
        page.update()

    name_input = ft.TextField(
        label="연예인 이름", 
        width=200, 
        on_submit=search_click
    )
    
    event_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("인천공항"), 
            ft.dropdown.Option("공항패션"), 
            ft.dropdown.Option("VIP시사회"), 
            ft.dropdown.Option("쇼케이스"),
            ft.dropdown.Option("행사")
        ],
        value="공항패션",
        width=150
    )
    
    search_btn = ft.Button("검색", on_click=search_click)
    
    load_more_btn = ft.FilledButton(
        "사진 더 가져오기 (50장+)", 
        on_click=load_more_click, 
        visible=False,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE, 
            bgcolor=ft.Colors.BLUE_700
        )
    )

    page.add(
        ft.Row([name_input, event_dropdown, search_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color="transparent"),
        gallery,
        ft.Container(
            content=ft.Row([load_more_btn], alignment=ft.MainAxisAlignment.CENTER),
            padding=ft.Padding.only(top=20, bottom=80) # 버튼에 가리지 않게 아래 여백 충분히
        )
    )

if __name__ == "__main__":
    ft.run(main)