let original_data = null
const elhuyarTranslate = (selector, destination_language) => {
  const portal_url = document.querySelector('body').getAttribute('data-portal-url')
  const lang = document.querySelector('html').getAttribute('lang')
  const content = document.querySelector(selector)
  const active = document.querySelector('button.elhuyar.active')

  if (!original_data){
    original_data = content.getHTML()
  }
  if(active){
    active.classList.remove('active');
  }
  if (original_data){
    content.classList.add('elhuyar-loader-spinner')
    document.querySelector(`#elhuyar-translate-${destination_language}`).classList.add('loading')
    postTranslation(`${portal_url}/@elhuyar-translator`, {"language_pair":`${lang}-${destination_language}`, "text": original_data})
    .then(data => {
      if(data.translated_text){
        const current = document.querySelector(`#elhuyar-translate-${destination_language}`)
        content.innerHTML = data.translated_text
        content.classList.remove("elhuyar-loader-spinner")
        current.classList.remove('loading')
        current.classList.add('active')
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
