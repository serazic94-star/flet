1. import 구문

2. main(page) 시작 / 상태 변수

3. 공통 UI 함수들
   - top_appbar()
   - bottom_nav()
   - show_message()
   - create_tooltip()

4. 화면 전환 함수
   - render_home()
   - render_weight_page()

5. 체중 그래프/저장 관련 함수
   - build_weight_chart()
   - save_weight()

6. 처음 실행할 화면 지정
   - render_home()
   
7. 프로그램 실행 구문
   - if __name__ == "__main__":

main()
├─ 기본 설정
├─ 상태 변수
├─ 공통 함수
│  ├─ top_appbar()
│  ├─ bottom_nav()
│  ├─ show_message()
│  └─ create_tooltip()
├─ 홈 화면 함수
│  └─ render_home()
├─ 체중 기능 함수
│  ├─ build_weight_chart()
│  ├─ save_weight()
│  └─ render_weight_page()
└─ 처음 화면 실행
   └─ render_home()