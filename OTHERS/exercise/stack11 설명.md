체중기록 메뉴 클릭
        ↓
go_weight_page()
        ↓
render_weight_page()
        ↓
page.clean()   ← 기존 홈화면 삭제
        ↓
weight_page 생성
        ↓
page.add(weight_page)
        ↓
지금 보이는 화면