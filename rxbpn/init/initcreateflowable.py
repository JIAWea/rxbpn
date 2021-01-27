from rxbp.mixins.flowablemixin import FlowableMixin

from rxbpn.impl.createflowableImpl import CreateFlowableImpl


def init_create_flowable(
        underlying: FlowableMixin,
):
    return CreateFlowableImpl(
        underlying=underlying,
    )
