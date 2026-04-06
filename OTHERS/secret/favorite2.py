import flet as ft
import urllib.request
import urllib.parse
import json
import webbrowser

# 네가 캐낸 마스터키!
CLIENT_ID = "HLEBvq30Qitnio590Y_1"
CLIENT_SECRET = "XoAlGygeSa"

def get_naver_images(query):
    """네이버 API로 사진만 50장씩 쏙쏙 뽑아오는 함수"""
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=50&sort=sim"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            data = json.loads(response_body.decode('utf-8'))
            return [item['link'] for item in data['items']]
    except Exception as e:
        print(f"데이터 캐내기 실패 ㅠㅠ: {e}")
    return []

def main(page: ft.Page):
    page.title = "✨ 나만의 전용 포토 검색기 ✨"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK 

    gallery = ft.GridView(
        expand=1,
        runs_count=4, 
        max_extent=300, 
        child_aspect_ratio=0.7, 
        spacing=15,
        run_spacing=15,
    )

    def search_click(e):
        if not name_input.value:
            name_input.error_text = "이름을 입력해주세요!"
            page.update()
            return
        
        name_input.error_text = None
        gallery.controls.clear()
        page.update()
        
        # 💡 입력창의 이름 + 드롭다운의 행사를 합쳐서 검색!
        query = f"{name_input.value} {event_dropdown.value}"
        image_urls = get_naver_images(query)
        
        for url in image_urls:
            clickable_image = ft.Container(
                content=ft.Image(
                    src=url,
                    fit="cover",
                    border_radius=ft.BorderRadius.all(12),
                    error_content=ft.Text("사진 없음😥", color="red", size=15)
                ),
                on_click=lambda e, link=url: webbrowser.open(link)
            )
            gallery.controls.append(clickable_image)
            
        page.update()

    # 💡 [변경] 드롭다운 대신 직접 입력하는 텍스트 필드!
    name_input = ft.TextField(
        label="연예인 이름 입력",
        hint_text="예: 카리나, 권나라, 장원영...",
        width=200,
        on_submit=search_click # 엔터키 쳐도 검색되게 함
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
        width=150,
        label="행사 선택"
    )
    
    search_btn = ft.Button("사진 쫙 뽑기!", on_click=search_click, height=50)

    page.add(
        ft.Row(
            [name_input, event_dropdown, search_btn], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(height=20, color="transparent"),
        gallery
    )

if __name__ == "__main__":
    ft.run(main)