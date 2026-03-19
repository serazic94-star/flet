import flet as ft
import requests
import time

def main(page: ft.Page) -> None:
    # =======================================
    # 1단계) 페이지 초기의 세팅
    # =======================================
    page.title = '주소 검색기'
    page.window.width = 500
    page.window.height = 700
    page.padding = 20

    API_URL = "https://business.juso.go.kr/addrlink/addrLinkApi.do"
    API_KEY = 'devU01TX0FVVEgyMDI2MDMxNzExNDQwNzExNzc0MjM='

    # =======================================
    # 2단계) 단일UI요소 준비하기
    # =======================================
    result_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    search_input = ft.TextField(label="도로명 주소, 건물명 검색", expand=True, autofocus=True)
    search_button = ft.ElevatedButton("검색", icon="search")

    # =======================================
    # 3단계) 기능 정의 (유효성 검사 및 클릭 이벤트)
    # =======================================

    #주소 팁 닫기
    def close_tip(e=None):
      address_bottom_tip_sheet.open = False
      page.update()

# 주소 팁 bottomsheet 정의하기
    address_bottom_tip_sheet = ft.BottomSheet(
      content=ft.Container(
          padding=20,
          content=ft.Column(
              tight=True,
            controls = [
                  ft.Text("tip", size=25, weight='bold'),
                  ft.Divider(),
                  ft.Text("아래와 같은 조합으로 입력 시 더욱 상세한 결과가 검색됩니다!"),
                  ft.Text('도로명 + 건물번호', size=17),
                  ft.Text('ex) 오리로 158', size=14, color='blue'),
                  ft.Text('지역명(동/리) + 건물명', size=17),
                  ft.Text('ex) 철산 하늘채 2차', size=14, color='blue'),
                  ft.Container(height=10),
                  ft.ElevatedButton("확인했어요!", on_click=lambda _: close_tip())
            ],
          ),
      )
    )

    # 앱이 시작될때 bottomSheet을 띄우기
    def show_inital_tip(e=None):
      address_bottom_tip_sheet.open = True
      page.update()

    # 기존 검색창에에서 주소를 클릭하면 상세주소입력모드로 변경하기
    def on_address_select(e):
      address_data = e.control.data
      base_address = address_data['road']

      # send_page 전송 목저으로 data를 준비해준다.
      search_input.data = address_data

      # 기존 검색창 -> 선택한 주소를 미리 작성 후 띄어쓰기 1칸 추가하기
      search_input.value =''

      # 안내문구를 변경시켜주기
      search_input.label = "상세 주소(ex. 한라원앤디 타워 A동 306동)"
      #search_input.bgcolor = ft.Colors.GREY_500

      # 버튼 또한 검색에서 완료로 변경하기
      search_button.text = "확인"
      search_input.icon ='search'
      search_button.on_click = send_page
      search_input.on_submit = send_page

      # 밑의 검색 결과를 지우고 메시지를 출력시킨다.
      result_column.controls.clear()
      result_column.controls.append(ft.Text("상세 주소를 입력하시고 [확인] 혹은 Enter를 눌러주세요!"))
      page.update()
      search_input.focus() # 사용자가 타자 입력하게 커서를 이동

    # 최종 입력한 데이터를 print하는 함수
    def send_page(e):
      # search_input의 3가지 데이터 정보 꺼내기
      save_data = search_input.data
      #  사용자가 입력한 '상세 주소'만 분리해주기
      full_text = search_input.value
      detail_addr = full_text.replace(save_data['road'],"").strip()

      ## 데이터 출력
      print(f"우편번호: {save_data['zip']}")
      print(f"지번주소: {save_data['jibun']}")
      print(f"상세주소: {detail_addr}")
      print("모든 작업 완료, 종료시작")
      #wait page.window.destroy()
      import os
      os._exit(0)
      page.update()

    def validation_test_keyword(keyword):
        if not keyword:
            search_input.error_text = '검색어를 입력하지 않았습니다. 검색어를 입력해주세요!'
            result_column.controls.append(ft.Text("검색어를 입력하지 않았습니다. 다시 입력해주세요", size=15, color='red'))
            page.update()
            return False 
        
        # 문법 오류 수정: " " not in keyword and keyword[-1] in [...]
        if " " not in keyword and keyword[-1] in ['시', '도', '군', '구']:
            search_input.error_text = '시/도/군/구로 입력할 수 없습니다. 상세히 입력해주세요.'
            result_column.controls.append(ft.Text("시/도/군/구로 입력하실수 없습니다. 다시 입력하세요", size=15, color='red'))
            page.update()
            return False 

        search_input.error_text = None 
        return True

    def click_event(e):
        click_keyword = search_input.value.strip()

        if not validation_test_keyword(click_keyword):
            return
        
        result_column.controls.clear()
        result_column.controls.append(ft.ProgressRing()) 
        page.update()
  
        try:
            params = { 
                'confmKey': API_KEY,
                'currentPage': 1,
                'countPerPage': 50,
                'keyword': click_keyword,
                'resultType': 'json'
            }
            response = requests.get(API_URL, params=params)
            data = response.json()
            common = data.get('results', {}).get('common', {}) 

            total_result_len = int(common.get('totalCount', 0))

            if total_result_len > 5000:
                error_message = f"결과가 너무 많습니다. ({total_result_len}개) 상세하게 입력해주세요."
                search_input.error_text = error_message
                result_column.controls.clear()
                page.update() 
                return
            
            if common.get('errorCode') != '0':
                error_message_common = f"API에러 발생 {common.get('errorMessage')} ({common.get('errorCode')})"
                search_input.error_text = "API 에러 발생! 다시 입력하세요"
                result_column.controls.clear()
                result_column.controls.append(ft.Text(error_message_common, size=15, color='red'))
                page.update() 
                return

            page_juso = data.get('results', {}).get('juso', [])
            result_column.controls.clear()

            if not page_juso:
                result_column.controls.append(ft.Text("검색 결과가 없습니다.", size=15, color='red'))
            else: 
                for juso in page_juso:
                    result1 = juso['zipNo']
                    result2 = juso['bdNm'] if juso['bdNm'] else f"도로명 | {juso['roadAddr']}"
                    result3 = f"지번 | {juso['jibunAddr']}" 

                    # 들여쓰기 완벽 교정: for문 안쪽에 맞춰서 컨테이너 조립
                    result_column.controls.append(
                        ft.Container(
                            data = {
                                'zip': juso['zipNo'],
                                'road': juso['roadAddr'],
                                'jibun': juso['jibunAddr'],
                            },
                            on_click=on_address_select,
                            padding=15,
                            content=ft.Column([
                                ft.Text(result1, size=20, color='red'),
                                ft.Text(result2, size=16, weight='bold'),
                                ft.Text(result3, size=13, color='gray')
                            ], tight=True, spacing=5)
                        )
                    )
                    result_column.controls.append(ft.Divider(height=1, color='grey300'))
                    
        except Exception as ex:
            result_column.controls.clear()
            result_column.controls.append(ft.Text("시스템 오류입니다. 다시 검색하세요.", size=15, color='red'))
            print(f'서버API오류 발생: {ex}')  
        page.update() 

    # =================================
    # 4단계) 화면에 배치하기 (이 구역의 들여쓰기를 모두 정상화했습니다)
    # =================================
    search_button.on_click = click_event
    search_input.on_submit = click_event
    #search_button = ft.ElevatedButton("검색", icon="search", on_click=click_event)
    #search_input.on_submit = click_event 

  ### 페이지에 BottomSheet를 등록하기
    page.overlay.append(address_bottom_tip_sheet)

    # 에러 원인 제거: ft.Column()으로 묶지 않고 콤마로 직접 나열합니다.
    page.add(
        ft.Text("주소 검색", size=25, weight='bold'),
        ft.Row([search_input, search_button]),
        ft.Divider(),
        result_column
    )
    page.update()
    time.sleep(0.1)
    show_inital_tip()
  
if __name__ == '__main__':
    ft.app(target=main)


    ### 도로명 / 우편주소 print