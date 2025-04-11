import json
import requests

def create_markdown_post(filename):
    """
    a.json 파일을 읽어 Markdown 형식의 게시글 문자열을 생성합니다.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        news_list = json.load(file)

    markdown_output = "# 오늘의 주요 뉴스\n\n"
    for idx, article in enumerate(news_list, start=1):
        markdown_output += f"### {idx}. {article['title']}\n"
        markdown_output += f"URL: {article['url']}\n"
        markdown_output += f"요약: {article['summary']}\n\n"
    return markdown_output

def post_to_tistory(content, access_token, blog_name, title, category=0, visibility=3):
    """
    Tistory API를 호출하여 게시글을 업로드합니다.
    
    매개변수:
      - content: 게시글 내용 (HTML 또는 Markdown)
      - access_token: Tistory API access token
      - blog_name: 블로그 이름 (tistory 블로그의 도메인에 해당하는 부분)
      - title: 게시글 제목
      - category: 게시글 카테고리 ID (기본값 0)
      - visibility: 공개여부 (예: 3: 공개, 0: 비공개)
    """
    url = "https://www.tistory.com/apis/post/write"
    params = {
        "access_token": access_token,
        "output": "json",
        "blogName": blog_name,
        "title": title,
        "content": content,
        "category": category,
        "visibility": visibility,
        "acceptComment": 1  # 댓글 허용 여부 (1: 허용)
    }
    response = requests.post(url, data=params)
    return response.json()

if __name__ == '__main__':
    # 1. a.json 파일을 읽어 Markdown 형식 게시글 생성
    markdown_content = create_markdown_post('./news_summary.json')
    print(markdown_content)
    # 2. Tistory API에 필요한 변수 설정 (각자 본인의 정보를 입력)
    tistory_access_token = "YOUR_TISTORY_ACCESS_TOKEN"  # 본인의 Tistory access token
    tistory_blog_name = "agentx"                # 블로그 이름 (예: 'myblog')
    post_title = "오늘의 주요 뉴스"
    
    # 3. Tistory에 게시글 업로드
    result = post_to_tistory(markdown_content, tistory_access_token, tistory_blog_name, post_title)
    
    # 결과 출력
    print(result)
