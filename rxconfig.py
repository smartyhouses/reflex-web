import reflex as rx
from pcweb.styles.tailwind_config import tw_config

config = rx.Config(
    port=3000,
    app_name="pcweb",
    deploy_url="http://0.0.0.0:3000",
    frontend_packages=[
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
        "@inkeep/uikit",
    ],
    telemetry_enabled=False,
    tailwind=tw_config,
)
