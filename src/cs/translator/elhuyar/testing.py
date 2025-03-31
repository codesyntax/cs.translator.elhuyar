# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import cs.translator.elhuyar


class CsTranslatorElhuyarLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cs.translator.elhuyar)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cs.translator.elhuyar:default')


CS_TRANSLATOR_ELHUYAR_FIXTURE = CsTranslatorElhuyarLayer()


CS_TRANSLATOR_ELHUYAR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CS_TRANSLATOR_ELHUYAR_FIXTURE,),
    name='CsTranslatorElhuyarLayer:IntegrationTesting',
)


CS_TRANSLATOR_ELHUYAR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CS_TRANSLATOR_ELHUYAR_FIXTURE,),
    name='CsTranslatorElhuyarLayer:FunctionalTesting',
)


CS_TRANSLATOR_ELHUYAR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CS_TRANSLATOR_ELHUYAR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CsTranslatorElhuyarLayer:AcceptanceTesting',
)
