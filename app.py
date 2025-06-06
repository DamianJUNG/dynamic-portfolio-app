import streamlit as st

st.set_page_config(page_title="Dynamic Portfolio Backtest", page_icon="📈")

st.title("📈 동적 자산배분 전략 백테스트")
st.write("""
이 웹앱은 파이썬 기반 동적 자산배분 전략을 실험하고 백테스트하는 도구입니다.  
CSV 파일을 업로드하여 전략을 시뮬레이션하고, 이동평균선을 기준으로 매매신호를 확인할 수 있도록 구성될 예정입니다.
""")

st.info("🛠 향후 기능 업데이트 예정: CSV 업로드 → 전략 적용 → 그래프 시각화 → 수익률 요약")
