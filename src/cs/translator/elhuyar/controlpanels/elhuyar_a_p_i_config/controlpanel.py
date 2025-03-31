# -*- coding: utf-8 -*-
from cs.translator.elhuyar import _
from cs.translator.elhuyar.interfaces import ICsTranslatorElhuyarLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope.component import adapter
from zope.interface import Interface
from zope import schema

class IElhuyarAPIConfig(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class ElhuyarAPIConfig(RegistryEditForm):
    schema = IElhuyarAPIConfig
    schema_prefix = "cs.translator.elhuyar.elhuyar_a_p_i_config"
    label = _("Elhuyar A P I Config")


ElhuyarAPIConfigView = layout.wrap_form(
    ElhuyarAPIConfig, ControlPanelFormWrapper
)



@adapter(Interface, ICsTranslatorElhuyarLayer)
class ElhuyarAPIConfigConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IElhuyarAPIConfig
    configlet_id = "elhuyar_a_p_i_config-controlpanel"
    configlet_category_id = "Products"
    title = _("Elhuyar A P I Config")
    group = ""
    schema_prefix = "cs.translator.elhuyar.elhuyar_a_p_i_config"
