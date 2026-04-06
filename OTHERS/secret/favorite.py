import flet as ft
import urllib.request
import urllib.parse
import json
import webbrowser # 💡 파이썬 기본 모듈! Flet이 아무리 업데이트 돼도 이건 절대 에러 안 남!

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
    page.title = "✨ 나의 최애 전용 갤러리 ✨"
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
        gallery.controls.clear()
        page.update()
        
        query = f"{celeb_dropdown.value} {event_dropdown.value}"
        image_urls = get_naver_images(query)
        
        for url in image_urls:
            clickable_image = ft.Container(
                content=ft.Image(
                    src=url,
                    fit="cover",
                    border_radius=ft.BorderRadius.all(12),
                    error_content=ft.Text("사진 없음😥", color="red", size=15)
                ),
                # 💡 Flet 명령어 대신, 파이썬 기본 웹브라우저 열기 기능으로 교체!
                on_click=lambda e, link=url: webbrowser.open(link)
            )
            gallery.controls.append(clickable_image)
            
        page.update()

    celeb_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option("권나라"), ft.dropdown.Option("카리나")],
        value="권나라",
        width=150,
        label="최애 선택"
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
        ft.Row([celeb_dropdown, event_dropdown, search_btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=20, color="transparent"),
        gallery
    )

if __name__ == "__main__":
    ft.run(main)