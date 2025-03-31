from cs.translator.elhuyar import _
from zope.i18n import translate
from plone.restapi.services import Service
from plone import api
import requests
from plone.restapi.deserializer import json_body


HEADERS = {"Accept": "application/json"}
TIMEOUT = 7


class Translator(Service):
    def reply(self):
        api_base_url = api.portal.get_registry_record(
            "cs.translator.elhuyar.elhuyar_a_p_i_config.api_base_url"
        )
        api_id = api.portal.get_registry_record(
            "cs.translator.elhuyar.elhuyar_a_p_i_config.api_id"
        )
        api_key = api.portal.get_registry_record(
            "cs.translator.elhuyar.elhuyar_a_p_i_config.api_key"
        )
        translation_engine = api.portal.get_registry_record(
            "cs.translator.elhuyar.elhuyar_a_p_i_config.translation_engine"
        )
        body = json_body(self.request)
        language_pair = body.get("language_pair", None)
        text = body.get("text", None)
        if not language_pair or not text:
            self.request.response.setStatus(400)
            return {
                "message": translate(
                    _("Incorrect params, language_pair and text are required"),
                    context=self.request,
                ),
            }
        try:
            result = requests.post(
                f"{api_base_url}/translate_string",
                json={
                    "api_id": api_id,
                    "api_key": api_key,
                    "translation_engine": translation_engine,
                    "language_pair": language_pair,  # Language of the original text and objective language for the translation: es-eu | eu-es | etc
                    "content_type": "html",  # hardcoded: Content type of the text: txt | html | xml
                    "text": text,
                },
                headers=HEADERS,
                timeout=TIMEOUT,
            )
            if result.ok:
                # Ignoring keys:
                # - "execution_time"
                # - "glossary_active_words"
                # - "interactive"
                # - "original_text"
                # - "source_sentences"
                # - "translated_sentences"
                # - "words"
                return result.json().get("translated_text", "")
            else:
                try:
                    self.request.response.setStatus(result.status_code)
                    return result.json()
                except Exception:
                    return {
                        "message": translate(
                            _("Unexpected Error"), context=self.request
                        )
                    }

        except requests.exceptions.Timeout:
            self.request.response.setStatus(500)
            return {"message": translate(_("Timeout"), context=self.request)}
