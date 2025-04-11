LangGraph와 MCP 기반 AI 에이전트 실습 코드
프로젝트 소개 🚀
본 저장소는 『비즈니스 자동화 AI 에이전트의 새로운 시대: LangGraph와 MCP의 강력한 시너지』 책에서 소개된 모든 실습 예제 코드를 포함합니다. 책의 내용을 직접 실행하고 응용해볼 수 있도록 구성된 멀티 에이전트 시스템 예제 모음으로, LangGraph 프레임워크와 MCP(Model Context Protocol)의 결합을 통해 차세대 비즈니스 자동화 AI 에이전트 구축 방법을 다룹니다.

LangGraph는 멀티 스텝 워크플로우를 그래프 상태 머신으로 구현하는 프레임워크이고, MCP는 외부 도구와 데이터를 AI에이전트가 표준화된 방식으로 연동할 수 있게 해주는 프로토콜입니다. 이 저장소의 코드를 통해 상태 기반 에이전트 그래프, MCP 툴 서버 연동, 그리고 전자상거래·트레이딩 등 도메인 특화 에이전트 시나리오까지 폭넓은 예제를 실습할 수 있습니다.

주요 예제 구성 📂
이 저장소에는 책의 각 장/절에서 개발한 핵심 예제들이 파이썬 스크립트 형태로 포함되어 있습니다. 주요 파일과 예제는 다음과 같습니다:

simple_agent.py – LangGraph를 이용한 가장 기본적인 에이전트 예제. 단일 QA 에이전트를 구성하고 실행하는 코드로, LangGraph 상태 그래프의 기본 구조(노드와 엣지 구성)를 보여줍니다.

memory_agent.py – 대화 메모리를 갖춘 에이전트 예제. LangGraph의 상태 유지와 Persistence 기능을 활용하여 이전 대화 맥락을 기억하고 활용하는 챗봇 구현을 다룹니다.

hitl_agent.py – Human-in-the-Loop 검증 단계가 포함된 에이전트 예제. LangGraph 그래프 실행 중간에 체크포인트를 걸고 사용자의 확인/승인을 받는 흐름을 구현합니다 (HITL 패턴).

two_qa_agent.py – 두 개의 에이전트 협업 예제. 하나의 질문을 두 에이전트가 나누어 처리하는 간단한 멀티에이전트 시나리오로, 검색 담당 에이전트와 답변 생성 에이전트가 순차 협업하는 구조를 보여줍니다.

project_agent.py – 복잡한 멀티에이전트 워크플로우 예제. 여러 전문 에이전트가 비동기적으로 협업하고 Supervisor 에이전트가 전체 흐름을 조율하는 시나리오를 다룹니다. 브레인스토밍 → 자료조사(병렬 수행) → 요약 생성의 단계로 이루어진 프로젝트 아이디어 도우미 에이전트 구현을 예시로, LangGraph로 복잡한 그래프(workflow)를 구성하는 방법을 보여줍니다.

chatbot_server.py / chatbot_client.py – MCP 통신을 활용한 대화형 AI 에이전트 예제 (표준 입출력 모드). chatbot_server.py는 MCP 서버로서 외부 도구 함수를 정의하고(@mcp.tool 데코레이터 사용) 표준입출력(stdio) 기반 MCP 통신을 수행합니다. 검색 기능과 OpenAI API를 통한 답변 생성 기능을 툴로 제공하며, .env 파일에 저장된 API 키(예: OpenAI, SerpAPI)를 불러와 사용합니다. chatbot_client.py는 LangGraph 에이전트가 MCP 서버에 클라이언트로 연결하여 툴을 호출하는 코드입니다. LangChain MCP 어댑터(langchain_mcp_adapters)를 통해 서버의 툴 목록을 불러오고, 상태 그래프 내에서 원격 툴 (search_web, generate_answer)을 호출하여 사용자 질문에 대한 답변을 얻습니다.

chatbot_server_sse.py / chatbot_client_sse.py – MCP SSE(Server-Sent Events) 통신 방식 예제. 웹 환경에서 MCP를 활용하는 방식으로, chatbot_server_sse.py는 FastAPI 기반의 MCP 서버를 실행하여 HTTP SSE 엔드포인트(/sse)를 제공합니다. chatbot_client_sse.py는 aiohttp를 이용해 SSE 스트림으로 서버 툴을 호출하는 클라이언트입니다. 이 구조를 통해 브라우저나 외부 애플리케이션과도 연동할 수 있는 REST API 형태의 MCP 활용을 보여줍니다.

그 외에도 requirements.txt (필수 패키지 목록)와 env.example (환경변수 설정 예시 파일)가 포함되어 있습니다. 예제 코드들은 대부분 Python 3.11 환경에서 작성되었으며, VSCode에서 편리하게 실습할 수 있도록 일부 설정(.vscode/)이 제공될 수 있습니다.

설치 방법 🛠
실습 코드를 실행하기 위한 환경을 세팅하는 방법은 다음과 같습니다:

Python 버전 확인: Python 3.11 이상의 버전이 설치되어 있는지 확인하세요 (가능하면 3.11 권장).
저장소 클론: 터미널에서 저장소를 클론하고 디렉토리로 이동합니다.

git clone https://github.com/netschool-kr/langgraph-mcp.git
cd langgraph-mcp
가상환경 생성: 의존성 충돌을 피하기 위해 가상환경을 생성하고 활성화합니다.

python3 -m venv .venv   # 가상환경 생성 (.venv 폴더)
source .venv/bin/activate   # 가상환경 활성화 (Windows에서는 .venv\Scripts\activate)
필수 패키지 설치: requirements.txt 파일에 명시된 파이썬 패키지를 설치합니다.

pip install -r requirements.txt
이 때 LangGraph, MCP SDK, LangChain MCP 어댑터, FastAPI, aiohttp 등 필요한 모든 라이브러리가 설치됩니다.

환경 변수 설정: OpenAI API 키 등 외부 API 사용을 위해 환경 변수를 설정해야 합니다. 저장소의 env.example 파일을 참고하여 프로젝트 루트에 .env 파일을 만들고 필요한 키 값을 입력하세요. 예시:
text

OPENAI_API_KEY=<여러분의 OpenAI API 키>
SERPAPI_API_KEY=<여러분의 SerpAPI 키>

책의 예제를 실행하려면 OpenAI GPT API 키와 SerpAPI 검색 API 키가 반드시 필요합니다. (SerpAPI는 구글 검색 결과를 가져오는 서비스입니다.) .env 파일에 위 키들을 포함하고, 필요한 경우 GitHub Personal Access Token 등 추가 키를 설정합니다 (예: 프로젝트에 따라 GPT 외에 GitHub 데이터 활용 툴이 있을 경우).
VSCode 환경 설정: VSCode로 프로젝트를 열 경우, Python 인터프리터를 가상환경의 인터프리터로 선택합니다. .env 파일에 설정한 환경변수는 VSCode에서 자동으로 로드되도록 설정할 수도 있습니다. (예: VSCode의 Run/Debug 설정에서 **"envFile": "${workspaceFolder}/.env"**로 지정)

실행 방법 ▶️

이 저장소의 예제 코드는 독립적인 파이썬 스크립트로 제공되며, 각각 개별적으로 실행 가능합니다. VSCode 기준으로 각 예제 파일을 열고 Run 버튼을 누르거나, 터미널에서 직접 python 파일명.py 명령으로 실행하면 됩니다. 아래는 주요 예제 실행 방법과 유의사항입니다:

단일 에이전트 예제 실행: simple_agent.py 등의 기본 예제들은 터미널에서 곧바로 실행하면 콘솔 출력으로 결과를 확인할 수 있습니다. 예를 들어:
(venv) $ python simple_agent.py

실행 시 에이전트가 초기화되고 (필요한 경우 프롬프트가 표시되거나) 미리 정의된 질의를 처리하여 결과를 출력합니다. 기본 예제는 코드 내에 샘플 질의가 하드코딩되어 실행되거나, 콘솔 입력을 받아 동작합니다. 코드를 열어 필요한 경우 user_input 부분을 수정하거나 프롬프트에 질문을 입력하여 테스트해보세요.

상태 유지/체크포인트 예제: memory_agent.py, hitl_agent.py와 같은 예제들은 실행하면 이전 대화를 기억하는 답변을 생성하거나, 중간에 사용자 확인을 요구하는 흐름을 시뮬레이션합니다. 이러한 스크립트도 단순 실행으로 테스트할 수 있으며, 출력 로그를 통해 상태 저장 및 HITL 흐름을 확인할 수 있습니다.

복수 에이전트 협업 예제: two_qa_agent.py를 실행하면 두 개의 에이전트가 순차적으로 협력하여 답변을 도출하는 과정을 콘솔에 출력합니다. 마찬가지로 project_agent.py (복잡한 시나리오 예제)는 다수의 에이전트가 병렬/비동기로 작업하고 최종 요약을 만드는 흐름을 구현합니다. 이 코드는 논리 구조와 일부 핵심 동작을 예시한 것으로, 실행 시 로그를 통해 Supervisor의 조율, 병렬 작업 등의 워크플로우 진행 방식을 학습할 수 있습니다.


※ VSCode 팁: 예제 파일을 실행할 때 VSCode의 Run(▶) 버튼이나 디버그 모드를 사용하면 중단점 설정, 변수 상태 확인 등이 가능하여 코드 이해에 도움이 됩니다. 단, VSCode로 직접 실행 시 워킹 디렉토리가 프로젝트 루트가 아닐 수 있으므로, 상대 경로로 다른 파일을 호출하는 코드가 있다면 제대로 작동하지 않을 수 있습니다. 이러한 경우 통합 터미널에서 프로젝트 루트 디렉토리에서 실행하거나, .env에 EXEC_ENV=vscode 변수를 설정하는 등 코드에 맞게 경로를 조정해야 합니다 (예제 코드에서는 VSCode 환경을 감지하여 경로를 설정하는 처리가 있습니다). 기본적으로 터미널에서 실행하면 경로 문제가 없도록 구현되어 있습니다.

MCP 서버/클라이언트 예제 실행 💡
MCP를 활용하는 챗봇 예제(chatbot_server/client)는 서버-클라이언트 구조이므로 실행 순서에 유의해야 합니다. 제공된 두 가지 방식(표준입출력 모드와 SSE 모드)에 따라 실행 방법을 안내합니다:

1) STDIO 모드 (내장 MCP 서버 연동):
이 모드에서는 별도의 서버를 수동으로 띄울 필요 없이, 클라이언트 스크립트가 MCP 서버를 서브프로세스로 실행합니다.

실행 방법: chatbot_client.py 파일을 실행하세요.
(venv) $ python chatbot_client.py

그러면 내부에서 chatbot_server.py를 파이썬 subprocess로 실행하여 MCP 서버(툴 제공자)를 시작합니다. 이어서 클라이언트는 서버와 표준입출력 파이프로 연결된 세션을 초기화한 뒤, 서버로부터 툴 목록을 받아옵니다. 코드에서는 search_web 툴과 generate_answer 툴을 불러와 LangGraph의 그래프 노드에 매핑하고, 샘플 질문 ("서울의 내일 날씨는?")을 초기 상태로 그래프를 실행합니다.

실행 완료 후 터미널에는 다음과 같은 결과가 출력됩니다:

질문: 서울의 내일 날씨는?
검색 결과 요약: [ '...검색 결과 내용...' ]
답변: "...최종 답변 내용..."
(실제 출력은 OpenAI API와 SerpAPI의 응답에 따라 달라집니다.) 이 모드의 장점은 클라이언트 코드 하나만 실행하면 자동으로 MCP 서버까지 구동되어 편리하다는 점입니다. 또한 서버와 클라이언트가 같은 프로세스 그룹 내에 있으므로 빠르게 통신할 수 있습니다.

3) SSE 모드 (웹 서버 연동):
이 모드에서는 MCP 서버가 FastAPI 웹 서버로 동작하며, HTTP를 통해 툴을 호출합니다. SSE (Server-Sent Events)는 서버->클라이언트 방향으로 실시간 응답 스트림을 보내는 HTTP 프로토콜이므로, LLM의 토큰 생성 결과를 스트리밍하는데도 활용할 수 있습니다.

실행 방법: 두 개의 터미널이 필요합니다. 한쪽에서 MCP 서버를 실행하고, 다른 한쪽에서 클라이언트를 실행합니다.

터미널 1 – 서버 실행:
(venv) $ python chatbot_server_sse.py
이 명령으로 FastAPI 서버가 localhost:8000에서 시작됩니다. 서버 콘솔에 출력된 로그를 통해 Uvicorn 서버가 기동된 것을 확인할 수 있습니다. 서버는 search_web 및 generate_answer 두 가지 툴을 등록해 둔 상태이며, /sse 경로로 들어오는 POST 요청을 대기합니다.

터미널 2 – 클라이언트 실행:
(venv) $ python chatbot_client_sse.py
클라이언트 스크립트는 aiohttp를 사용해 http://localhost:8000/sse 엔드포인트로 요청을 보내게 됩니다. 내부 코드에서 "tool"과 "params"를 포함한 JSON payload를 전송하면, 서버는 해당 툴 함수를 호출한 뒤 결과를 SSE 스트림으로 돌려줍니다. chatbot_client_sse.py 실행 시 마찬가지로 샘플 질문을 전송하고 결과를 받아 출력합니다. 응답은 SSE 규격에 맞춰 data: ... 형태로 스트리밍되며, 클라이언트는 첫 번째 이벤트를 수신하여 최종 답변을 표시합니다.

SSE 모드의 장점은 웹 표준 인터페이스를 사용하기 때문에, 웹 브라우저나 다른 HTTP 클라이언트에서도 동일한 MCP 서버에 접근할 수 있다는 점입니다. 예를 들어, /sse 엔드포인트에 적절한 요청을 보내면 웹 애플리케이션에서도 AI 에이전트 툴을 활용할 수 있습니다. 다만 이 예제에서는 간단히 한 번의 요청-응답으로 완료되도록 하였으며, 멀티턴 대화나 스트림 처리 등의 확장은 개발자가 추가 구현해야 합니다.

(참고) MCP 서버 코드 (chatbot_server.py)에서는 OpenAI API 호출과 SerpAPI 검색 호출 부분에 예외 처리를 포함하고 있습니다. API 키가 올바르게 설정되지 않았거나 호출 제한에 걸린 경우 오류 메시지가 반환되니, 실행 중 오류가 발생하면 터미널 출력을 확인하세요. 또한, 기본 OpenAI 모델은 "gpt-3.5-turbo"로 지정되어 있으므로 해당 API 접근 권한이 있는지 확인해야 합니다. 필요에 따라 모델이나 프롬프트를 변경해 가면서 실험해보는 것도 권장됩니다.

참고 자료 📖
책: 비즈니스 자동화 AI 에이전트의 새로운 시대: LangGraph와 MCP의 강력한 시너지 – 본 프로젝트의 이론적 배경과 상세 구현 해설을 담은 도서입니다. 각 예제에 대한 설명과 추가적인 비즈니스 사례(고객 지원 자동화, 업무 프로세스 최적화 등)가 수록되어 있습니다.

LangGraph 공식 문서: LangGraph Documentation – LangGraph 프레임워크의 개념과 사용 방법에 대한 공식 가이드입니다. 노드/엣지로 구성되는 에이전트 워크플로우, 상태 관리, Persistence 등의 개념을 자세히 볼 수 있습니다.

MCP (Model Context Protocol) 공식 사이트: Model Context Protocol Introduction – Anthropic이 주도하는 MCP의 개념과 사양에 대한 문서입니다. MCP의 클라이언트-서버 아키텍처, 툴 등록과 호출, 전송 방식(stdio, HTTP 등) 등에 대한 정보를 제공합니다.

LangChain MCP Adapters: langchain-ai/langchain-mcp-adapters (GitHub) – LangGraph 에이전트가 다중 MCP 서버에 쉽게 연결할 수 있도록 도와주는 경량 어댑터 라이브러리입니다. 본 예제 코드에서도 load_mcp_tools 등의 기능을 활용하고 있으니, LangChain이나 LangGraph와 MCP의 연계에 관심이 있다면 참고하시기 바랍니다.

以上의 자료와 예제 코드를 바탕으로, 다양한 멀티에이전트 AI 애플리케이션을 직접 구축해보실 수 있습니다. 궁금한 사항이나 개선 아이디어가 있다면 이슈를 통해 공유해 주세요. Happy coding! 
