def get_youtube_link(concept):
    # 실제 YouTube Data API를 쓰거나, 검색 결과 페이지 링크를 동적으로 생성
    search_query = f"리눅스 마스터 2급 {concept}".replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={search_query}"