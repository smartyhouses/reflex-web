import reflex as rx
from pcweb.styles.tailwind_config import tw_config

config = rx.Config(
    port=8080,
    app_name="pcweb",
    deploy_url="http://0.0.0.0:8080",
    frontend_packages=[
        "chakra-react-select",
        "@radix-ui/react-navigation-menu",
        "@inkeep/uikit",
    ],
    telemetry_enabled=False,
    tailwind=tw_config,
)
