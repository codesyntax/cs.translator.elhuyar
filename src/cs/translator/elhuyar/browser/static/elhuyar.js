const elhuyarTranslate = (selector) => {
  const portalUrl = document.querySelector('body').getAttribute('data-portal-url')
  const content = document.querySelector(selector)
  if (content.getHTML()){
    postTranslation(`${portalUrl}/@elhuyar-translator`, {"language_pair":"eu-es", "text": content.getHTML()})
    .then(data => {
      if(data.translated_text){
        content.innerHTML = data.translated_text
      }
    });
  }
}

async function postTranslation(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    credentials: 'same-origin',
    headers: {'Content-Type': 'application/json','Accept': 'application/json'},
    body: JSON.stringify(data)
  });
  if (response.ok){
    return response.json();
  }else{
    return {}
  }
}
