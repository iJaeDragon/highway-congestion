const requestUtil = {}

requestUtil.request = function(method, url, body, successCallback, failCallback) {
    const xhr = new XMLHttpRequest();
    xhr.open(method, url, true);

    // 요청을 보낼 때 Content-Type 헤더 설정
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {  // 요청 완료
            if (xhr.status >= 200 && xhr.status < 300) {  // 성공 범위의 상태 코드 (200~299)
                // 성공 콜백 호출
                successCallback(JSON.parse(xhr.responseText));
            } else {
                // 실패 콜백 호출
                failCallback(xhr.status, xhr.statusText);
            }
        }
    };

    // body가 있는 경우 JSON 문자열로 변환하여 전송
    xhr.send(body ? body : null);
};

requestUtil.asyncRequest = function(method, url, body) {
    return new Promise((resolve, reject) => {
        const loadingBar = new LoadingBar();

        const xhr = new XMLHttpRequest();
        xhr.open(method, url, true);

        // 요청을 보낼 때 Content-Type 헤더 설정
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {  // 요청 완료
                loadingBar.loadEnd();
                if (xhr.status >= 200 && xhr.status < 300) {  // 성공 범위의 상태 코드 (200~299)
                    // 성공 시 Promise resolve
                    resolve(JSON.parse(xhr.responseText));
                } else {
                    // 실패 시 Promise reject
                    reject({
                        status: xhr.status,
                        statusText: xhr.statusText
                    });
                }
            }
        };

        // body가 있는 경우 JSON 문자열로 변환하여 전송
        xhr.send(body ? body : null);

        loadingBar.load();
    });
};

class LoadingBar {
    constructor() {
        this.loadingBarDiv = document.createElement('div');
        this.loadingBarStyle = document.createElement('style');
    }
    load() {
        this.loadingBarDiv.style.position = 'fixed';
        this.loadingBarDiv.style.top = '0';
        this.loadingBarDiv.style.left = '0';
        this.loadingBarDiv.style.width = '100%';
        this.loadingBarDiv.style.height = '5px';
        this.loadingBarDiv.style.backgroundColor = '#3498db'; // 로딩바 색상
        this.loadingBarDiv.style.zIndex = '9999';
        this.loadingBarDiv.style.animation = 'loadingAnimation 2s ease-in-out infinite';

        this.loadingBarStyle.innerHTML = `
               @keyframes loadingAnimation {
                   0% { width: 0%; }
                   50% { width: 50%; }
                   100% { width: 100%; }
               }
           `;

        document.head.appendChild(this.loadingBarStyle);
        document.body.appendChild(this.loadingBarDiv);
    }

    loadEnd() {
        document.head.removeChild(this.loadingBarStyle);
        document.body.removeChild(this.loadingBarDiv);
    }
}